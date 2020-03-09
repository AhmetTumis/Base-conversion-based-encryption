#!/usr/bin/env python3

import random
import math

islemKey = [] #islem numaralarini tutan liste

def decimalToBin(sayi):
    #print("this works1")
    convertedList.append(int(str(bin(sayi)[2:])))
    islemKey.append(1)

def decimalToOct(sayi):
    #print("this works2")
    convertedList.append(int(str(oct(sayi)[2:])))
    islemKey.append(2)

def binToDecimal(sayi):
    #print("this works3")
    convertedList.append(int(sayi))
    islemKey.append(3)

def binToOct(sayi):
    #print("this works4")
    convertedList.append(int(str(oct(sayi)[2:])))
    islemKey.append(4)

def octToDecimal(sayi):
    #print("this works5")
    convertedList.append(int(sayi))
    islemKey.append(5)

def octToBin(sayi):
    #print("this works6")
    convertedList.append(int(str(bin(sayi)[2:])))
    islemKey.append(6)

conversionFuncs = [ 
    decimalToBin, 
    decimalToOct,
    binToDecimal,
    binToOct,
    octToDecimal,
    octToBin
    ]

def isBinCompatible(sayi):
    
    sayac = 0 
    kontrol = int(math.log10(sayi))+1

    while(sayi>0):
        
        if(int(sayi)% 10 <= 1):  
            sayac +=1

        sayi -= sayi%10
        sayi/=10
        #print(int(sayi), sayac)

    if(sayac == kontrol):
        return True
    else:
        return False

def isOctCompatible(sayi):
    
    sayac = 0 
    kontrol = int(math.log10(sayi))+1

    while(sayi>0):
        
        if(int(sayi)% 10 <= 8):
            
            sayac +=1

        sayi -= sayi%10
        sayi/=10
        print(int(sayi), sayac)

    if(sayac == kontrol):
        return True
    else:
        return False



def changeListToDecimal(metin): #listedeki harfleri decimale çevir

    for i in range(len(metin)):
        metin[i] = ord(metin[i])

    return metin
    

##################################################main

girdi = list(input("string gir: "))   #metin
aList = changeListToDecimal(girdi)    #metin to ascii numbers 
convertedList = list()                #convertedlerin converted hali
#islemKey = list()          #islem numaralarini tutan liste


for i in range(len(aList)):

    randomConversionFuncs = random.choice(conversionFuncs)
    randomConversionFuncs(aList[i])
    
islemKey.append("asldkasdkasjl")




print(aList)

for i in range(len(convertedList)):
    print(convertedList[i])
    print("z")

print(islemKey)


