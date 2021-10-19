# Simran Simoliya (2019153)

import socket
import sys
import json

#substitution boxes
S_Box=[0xa,0x5,0x9,0xb,0x1,0x7,0x8,0xf,
      0x6,0x0,0x2,0x3,0xc,0x4,0xd,0xe]
# Inverse S-Box
S_Box_a=[0x9,0x4,0xa,0xb,0xd,0x1,0x8,0x5,
      0x6,0x2,0x0,0x3,0xc,0xe,0xf,0x7]



# Round keys: K0 = w0 + w1; K1 = w2 + w3; K2 = w4 + w5
w=[None]*6

def multiply(p1,p2):
      '''Multiply two polynomials in GF(2^4),i.e, x^4+x+1'''
      p=0
      while p2:
          if p2 & 0b1:
              p^=p1
          p1<<=1
          if p1 & 0b10000:
              p1^= 0b11
          p2 >>=1
      return p & 0b1111


def IntToVec(n):
      '''Function IntToVec to convert the integer into state vector'''
      return [n>>12,(n>>4) & 0xf, (n>>8) & 0xf, n & 0xf]


def VecToInt(n):
      '''Now convert the state vector back to integer'''
      return (n[0]<<12)+(n[2]<<8)+(n[1]<<4)+n[3]
 

def addKey(s1,s2):
      '''Now add the two keys in GF(2^4)'''
      return [i^j for i,j in zip(s1,s2)]


def NibSub(S_Box,s):
      '''function used for Nibble Substitution'''
      return [S_Box[e] for e in s]


def shiftRows(s):
      '''Function to shift the rows of state'''
      return [s[0],s[1],s[3],s[2]]

#swapping each nibble and substituting it using s-box
def sub2Nib(b):
    return S_Box_a[b >>4]+(S_Box_a[b & 0x0f]<<4)

#To generate the keys for encryption and decryption
def keyExp(key):
    Rcon1,Rcon2 =0b10000000, 0b00110000
    w[0]=(key & 0xff00) >> 8
    w[1]=key & 0x00ff
    w[2]=w[0]^Rcon1^sub2Nib(w[1])
    w[3]=w[2]^w[1]
    w[4]=w[2]^Rcon2^sub2Nib(w[3])
    w[5]=w[4]^w[3]


def mixCol(s):
      '''Function to columns according to the decryption method'''
      return [multiply(9,s[0])^ multiply(2,s[2]), multiply(9,s[1])^ multiply(2,s[3]),
              multiply(9,s[2])^ multiply(2,s[0]), multiply(9,s[3])^ multiply(2,s[1])]


def aes_decrypt(data,key):
      '''Function to decrypt the cipherText received from client'''
      keyExp(key)
      state=IntToVec(((w[4] << 8)+w[5]) ^ data)
      state=NibSub(S_Box,shiftRows(state))
      state=mixCol(addKey(IntToVec((w[2]<<8)+w[3]),state))
      state=NibSub(S_Box,shiftRows(state))
      return VecToInt(addKey(IntToVec((w[0] << 8)+w[1]),state))


# Code used from : https://jhafranco.com/2012/02/11/simplified-aes-implementation-in-python/