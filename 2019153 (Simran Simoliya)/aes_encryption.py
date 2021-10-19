#Simran Simoliya(2019153)

import socket
import sys
import json

#Substitution Box
S_Box=[0x9,0x4,0xa,0xb,0xd,0x1,0x8,0x5,
      0x6,0x2,0x0,0x3,0xc,0xe,0xf,0x7]

#Round Keys
w=[None]*6


def multiply(p1, p2):
    """Multiply two polynomials in GF(2^4)/x^4 + x + 1"""
    p = 0
    while p2:
        if p2 & 0b1:
            p ^= p1
        p1 <<= 1
        if p1 & 0b10000:
            p1 ^= 0b11
        p2 >>= 1
    return p & 0b1111


def IntToVec(n):
      '''Function to convert integer into state vector'''
      return [n>>12,(n>>4) & 0xf, (n>>8) & 0xf, n & 0xf]


def VecToInt(n):
      '''Function to convert state vector to integer'''
      return (n[0]<<12)+(n[2]<<8)+(n[1]<<4)+n[3]
 

def addKey(s1,s2):
      '''Adding two keys in GF(2^4)'''
      return [i^j for i,j in zip(s1,s2)]


def NibSub(S_Box,s):
      ''' Function used as Nibble Substitution'''
      return [S_Box[e] for e in s]


def shiftRows(s):
      '''Function to shift rowws of state'''
      return [s[0],s[1],s[3],s[2]]


def sub2Nib(b):
      '''Swapping each nibble and substituting it using s-box'''
      return S_Box[b >>4]+(S_Box[b & 0x0f]<<4)


def keyExp(key):
      '''To generate the keys for encryption and decryption'''
      Rcon1,Rcon2 = 0b10000000, 0b00110000
      w[0]=(key & 0xff00) >> 8
      w[1]=key & 0x00ff
      w[2]=w[0]^Rcon1^sub2Nib(w[1])
      w[3]=w[2]^w[1]
      w[4]=w[2]^Rcon2^sub2Nib(w[3])
      w[5]=w[4]^w[3]


def mixCol(s):
      '''Function to mix columns according to the encryption method'''
      return [s[0] ^ multiply(4,s[2]), s[1] ^ multiply(4,s[3]),
              s[2]^multiply(4,s[0]),s[3]^ multiply(4,s[1])]


def aes_encrypt(data,key):
    '''Function to encrypt the plainText'''
    keyExp(key)
    state=IntToVec(((w[0]<<8)+w[1])^data)
    state=mixCol(shiftRows(NibSub(S_Box,state)))
    state= addKey(IntToVec((w[2]<< 8)+w[3]),state)
    state= shiftRows(NibSub(S_Box,state))
    return VecToInt(addKey(IntToVec( (w[4] << 8) + w[5]),state))

# Code used from : https://jhafranco.com/2012/02/11/simplified-aes-implementation-in-python/