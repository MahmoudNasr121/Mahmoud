# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 00:49:12 2020

@author: mahmoud
"""

import sys

def gcd(a,b): 
    if (b == 0): 
         return a 
    return gcd(b, a%b)
        
def encrypt(cipher_type,operation_type,inpput_file,output_file,k):
    with open(inpput_file,'r') as reader:
        inp=reader.read();    
    cipher_type=cipher_type.lower()
    operation_type=operation_type.lower()
    out = ""
    if (cipher_type=="shift" ):
        if (len(k)!=1):
            sys.exit("key is not valid")
        k[0]=int(k[0])
        if (operation_type=="encrypt"):
            
            for i in range(len(inp)): 
                char = inp[i]
                if(char==" "):
                    out +=" "
                elif (char.isupper()): 
                    out += chr((ord(char) + k[0] - 65) % 26 + 65)  
                else: 
                    out += chr((ord(char) + k[0] - 97) % 26 + 97)
        elif (operation_type=="decrypt"):
            for i in range(len(inp)): 
                char = inp[i]
                if(char==" "):
                    out +=" "
                elif (char.isupper()): 
                    out += chr((ord(char) - k[0] - 65) % 26 + 65)  
                else: 
                    out += chr((ord(char) - k[0] - 97) % 26 + 97)
        else:
            print("not valid input")
    elif (cipher_type=="affine"):
        if (len(k)!=2):
            sys.exit("keys are not valid")
        k[0]=int(k[0])
        k[1]=int(k[1])
        if (operation_type=="encrypt"):
            for i in range(len(inp)): 
                char = inp[i]
                if(char==" "):
                    out +=" "
                elif (char.isupper()): 
                    out += chr(( ((ord(char) * k[0]) + k[1] )- 65) % 26 + 65)  
                else: 
                    out += chr(( ((ord(char) * k[0]) + k[1] )- 97) % 26 + 97)
        elif (operation_type=="decrypt"):
            j=0
            if(gcd(k[0],26)!=1):
                sys.exit("key not have inverse")
            for i in range(26):  
                if((k[0]*i)%26==1):
                    j= i
                    break
            a=j
            b=26-k[1]
            for i in range(len(inp)):
                char=inp[i]
                if(char==" "):
                    out +=" "
                elif (char.isupper()):
                    out += chr(( ((a*(ord(char)+b))- 65) % 26 + 65 ))
                else:
                    out += chr(( ((a*(ord(char)+b))- 97) % 26 + 97 ))
        else:
            print("not valid input")
    elif (cipher_type=="vigenere"):
        if (len(k)!=1):
            sys.exit("key is not valid")
        key=k[0]
        if (operation_type=="encrypt"):
            
            if len(inp) != len(key):  
                for i in range(len(inp)-len(key)):
                    key+=key[i % len(k[0])]
            for i in range(len(inp)): 
                char = inp[i]
                if(char==" "):
                    out +=" "
                elif (char.isupper()): 
                    out += chr((ord(inp[i])+ord(key[i])) % 26 + 65)  
                else: 
                    out += chr((ord(inp[i])+ord(key[i])) % 26 + 97)
        elif (operation_type=="decrypt"):
              if len(inp) != len(key):  
                  for i in range(len(inp)-len(key)):
                      key+=key[i % len(k[0])]
              for i in range(len(inp)): 
                  char = inp[i]
                  if(char==" "):
                     out +=" "
                  elif (char.isupper()): 
                      out += chr((ord(inp[i])-ord(key[i])) % 26 + 65)
                  else: 
                      out += chr((ord(inp[i])-ord(key[i])) % 26 + 97)
        else:
             print("not valid input")
    else:
        print("not valid input")
    with open (output_file,'w') as writer:
        writer.write(out)
    return out 

if(len(sys.argv)==6):
    encrypt(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],[sys.argv[5]])
elif(len(sys.argv)==7):
    encrypt(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],[sys.argv[5],sys.argv[6]])
