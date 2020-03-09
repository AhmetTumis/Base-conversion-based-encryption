#!/usr/bin/env python3

import random
import math

islemKey = [] #islem numaralarini tutan liste


def decimalToBin(sayi):
    print("this works1")
    islemKey.append(1)

def decimalToOct(sayi):
    print("this works2")
    islemKey.append(2)
def decimalToHex(sayi):
    print("this works3")
    islemKey.append(3)
def binToDecimal(sayi):
    print("this works4")
    islemKey.append(4)
def binToHex(sayi):
    print("this works5")
    islemKey.append(5)
def binToOct(sayi):
    print("this works6")
    islemKey.append(6)
def octToDecimal(sayi):
    print("this works7")
    islemKey.append(7)
def octToBin(sayi):
    print("this works8")
    islemKey.append(8)
def octToHex(sayi):
    print("this works9")
    islemKey.append(9)
def hexToDecimal(sayi):
    print("this works10")
    islemKey.append(10)
def hexToBin(sayi):
    print("this works11")
    islemKey.append(11)
def hexToOct(sayi):
    print("this works12")
    islemKey.append(12)


conversionFuncs = [ 
    decimalToBin, 
    decimalToHex,
    decimalToOct,
    binToDecimal,
    binToHex,
    binToOct,
    octToDecimal,
    octToBin,
    octToHex,
    hexToBin,
    hexToDecimal,
    hexToOct]

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
    




print(aList)
print(islemKey)


