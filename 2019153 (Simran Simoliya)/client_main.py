
# Simran Simoliya(2019153)

import socket
import json
from aes_encryption import aes_encrypt
from rsa_algo import rsa
from hashalgo import digest

def client_main(s):
  '''Main Function for Client'''
  
  #Take input from client for message and secret key
   
  message=int(input('Enter message :'),2)
  secret_key=int(input('Enter secret key:'),2)

  # Take input from client for its's public and private key 

  e_client_public,n_client_public=map(int,input("Enter the public keys of client: ").split())
  d_client_private=int(input('Enter the private key of client: '))
  
  # Client is requesting server for it's public key || TODO>> Request not made yet.
  ch=input('Enter \' y \' to request server for it \'s public key: ')
  s.send(ch.encode())

  keys=json.loads(s.recv(1025).decode())
  e_server_public=keys['e_server_public']
  n_server_public=keys['n_server_public']
  print('Public Key Received!')

  # Here encrypting the message with secret key using aes_encrypt 

  ciphertext=aes_encrypt(message,secret_key)

  #Here ,using RSA Algorithm, making the encrypted server key using public key parameters of server

  encrypted_secret_key=rsa(secret_key,e_server_public,n_server_public)

  # making hash digest

  hash_digest=digest(message)

  # making client signture using RSA algorithm using private key

  client_signature=rsa(int(hash_digest,16),d_client_private,n_client_public)

  # Arranging the data in dictionary and sending it to server

  data={'ciphertext':ciphertext,'encrypted_secret_key':encrypted_secret_key,'client_signature':client_signature,'e_client_public' : e_client_public,'n_client_public':n_client_public}
  s.send(json.dumps(data).encode())

  #OUTPUT ON THE CLIENT SIDE

  print('----Simran Simoliya(2019153)----')
  print('OUTPUT :')
  print('Encrypted Secret Key', encrypted_secret_key)
  print('Message',message)
  print('Public Key Parameters',e_client_public,'and',n_client_public)
  print('Private Key Parameters',d_client_private)
  print('Cipher Text',ciphertext)
  print('Digest',hash_digest)
  print('Digital Client Signature',client_signature)

  #Now here we're closing the Connection 

  s.close()



s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#port 
port=192
s.connect((socket.gethostname(),port))
print("Cennection Start : Client And Server are Connected")
client_main(s)

