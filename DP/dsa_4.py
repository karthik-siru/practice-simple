'''
idea :  You just want to know that .. 

Cn =  1/(n+1)*( 2nCn )

'''

from dsa_2 import binomialCoeff

def Catalan_Number (n) :
    c = binomialCoeff(2*n , n)
    return int(c//(n+1))