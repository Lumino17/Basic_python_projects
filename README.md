# Basic_python_projects
This repository has been created to show how basic python skills can be used to create small but usefull projects. 

## A. Python 4 layer encryption algorithm
### Uniqueness
  1. 4 layer encryption used.
  2. A key is generated everytime during encryption and only this key can be used to decrypt the message.
  3. The key generated is always random and after 24 tries the same key will be generated.
  4. Only one library that is random has been used in the script, which can be installed by using 'pip install random' in terminal.

The python script can be divided into different parts.

### 1. Primary functions:
     These are the main functions that are used to encrypt and decrypt messages. These functions are used
     to run the encrytion functions in a random manner so that everytime a new key is generated.
### 2. Encryption/Decryption functions:
     These are the main algorithms that have transformed a normal message to encrypted one.
     Also each one of them is followed by a reverse function to reverse the function.
### 3. Code Necessity:
     This part of the code consists of the message and other data to run code like,
     the metadata, it is used to store the place where the whitespaces are in the message
     for the insert_spaces function. It also has a dictionary that is used in one of the encryption functions.
### 4. Space function:
     The strip_space and insert_space functions have been used on the message before
     encryption and at end of decryption to make encryption more complex.

-> The encryption and decryption functions used are:

   1. reverse function : reverses the message
   2. rotate function : shifts the position of characters in the message by 7.
   3. mirror function : cuts the message in half, mirrors it and stitches it back.
   4. replacement function : every alphabet gets replaced by another defined character.
      
-> While the function used as a single might not give a proper encryption but using all of them at once in an indefinite order which generates a random key makes this algorithm really powerfull.
### Learning Outcomes:
1. Learning basic flow of code using functions.
2. Use of the library random.
3. Understanding of loops.
4. Use of different methods on strings and python lists.
     
