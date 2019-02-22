#!/usr/bin/env python3

import numpy as np

def utf16_decimals(char, chunk_size=2):
    # This function just get the decimal values for UTF-16
    encoded_char = char.encode('utf-16-be')
    decimals = []
    for i in range(0, len(encoded_char), chunk_size):
        chunk = encoded_char[i:i+chunk_size]
        decimals.append(int.from_bytes(chunk, 'big'))
    return decimals

def cipheredKey(text):
  # Here we create a 1x3 array with our decimal values, so we can multiply by inversed matrix and get the decrypted value
  text = text.replace(" ", "")
  decimal_unicode = []
  [decimal_unicode.append([utf16_decimals(text[i]), utf16_decimals(text[i + 1]), utf16_decimals(text[i + 2])]) for i in range(0, len(text), 3)]
  return decimal_unicode

def decrpt(invMtrx, cipheredMtrx):
  slicedArray = []
  # For to multiply inverse matrix (3x3) x our letter in decimals (1x3)
  for i in range(0, len(cipheredMtrx)):
    mtx = np.matrix(cipheredMtrx[i])
    slicedArray.append(np.matmul(invMtrx, mtx))
  
  decimals = np.concatenate(slicedArray)
  finalAnswer = ""

  # Here we get the decrypted letter
  for i in range(0, len(decimals)):
    finalAnswer  += chr(decimals[i][0])
  return finalAnswer

def hillCipher (key, cipheredText):
  # Generates the matrix for the giver array
  keymatrix = np.matrix(key)
  #Inverting matrix for further use
  invKeyMatrix = np.linalg.inv(keymatrix)
  # Get our decimal values (unicode), so we can multiply by our inversed matrix
  cphTxt = cipheredKey(cipheredText)
  # Decrypting :D
  return decrpt(invKeyMatrix, cphTxt)

keyArr = [[1,0,0],[1,3,1],[1,2,0]]
ciphTxt = "S Ţ Õ V ŝ Ø O ƙ ó M Ţ Ï E Ű á"

print(hillCipher(keyArr, ciphTxt))
