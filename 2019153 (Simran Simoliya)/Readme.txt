//Simran Simoliya(2019153)

Explaination of the Assignment:

There are 6 files :

client_main.py: For the client  
serer_main.py: For the server
aes_encryption.py: Has the functions to implement Simplified AES encryption.
aes_decryption.py: Has the functions to implement Simplified AES decryption.
hashalgo.py: Has the function to implement the hash algorithm.
rsa_algo.py: Has the function to implement the RSA algorithm.

Module / Libraries Used - 
    - socket : The socket module is used for building full-fledged network applications including client and server programs.
    - sys : The sys module in Python provides various functions and variables that are used to manipulate different parts of the Python runtime environment.
    - json : (the transformation of data into a series of bytes ) the JSON library in Python uses dump() function to convert the Python objects into their respective JSON object, 
             so it makes easy to write data to files.

    - rsa : It is an asymmetric cryptographic algorithm which means that there are two different keys i.e., the public key and the private key.
    - digest : A message digest is a sequence of bits produced for an input string, using an one-way function. 

    - hashlib : The core purpose of this module is to use a hash function on a string, and encrypt it so that it is very difficult to decrypt it.


Function used in client_main.py only:

    - client(s): Main function for client ,
                 which start the connection between client & server.


Function used in server_main.py only:

    - server(conn): Main function for server,
                    which start the connection between client & server.


Functions used in aes_decryption.py are:

    - multiply(p1,p2): This function is used to multiply two polynomials in GF(2^4),i.e, x^4+x+1
    - InttoVec(n): It converts 2-byte (8 bits integer) into a vector of 4 elements.
    - VecToInt(n): It converts a 4-element vector into a 2-byte integer.
    - addKey(s1,s2): used to add two keys in GF(2^4)
    - NibSub(sbox,s): function used for Nibble Substitution
    - shiftRow(s): ShiftRow function
    - keyExp(key): To generate the three round keys
    - sub2nib(b): Swap each nibble and substitute it using sbox
    - mixCol(s): mix columns according to encryption method
    - aes_encrypt(val,key): encrypting the plain text with 2 rounds of simplified aes.

Functions used in aes_decryption.py are:

    - multiply(p1,p2): This function is used to multiply two polynomials in GF(2^4),i.e, x^4+x+1
    - InttoVec(n): It converts 2-byte (8 bits integer) into a vector of 4 elements.
    - VecToInt(n): It converts a 4-element vector into a 2-byte integer.
    - addKey(s1,s2): used to add two keys in GF(2^4)
    - NibSub(sbox,s): function used for Nibble Substitution
    - shiftRow(s): ShiftRow function
    - keyExp(key): To generate the three round keys
    - sub2nib(b): Swap each nibble and substitute it using sbox
    - mixCol(s): mixing columns accordig to decryption method
    - aes_decrypt(val): decrypting the cipher text received from the client.

Function used in hashalgo.py only:

    - digest(message): To calculate the digest formed by md5 hash algorithm

Function used in rsa_algo.py only:

    - rsa(base,exponent,mod): Calulate  based on simple function (base**exponent) % mod.

