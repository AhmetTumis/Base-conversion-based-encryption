#!/usr/bin/env python3

import math

def isBinCompatible(sayi):
    
    sayac = 0 
    kontrol = int(math.log10(sayi))+1

    while(sayi>0):
        
        if(int(sayi)% 10 <= 1):
            
            sayac +=1

        sayi -= sayi%10
        sayi/=10
        print(int(sayi), sayac)

    if(sayac == kontrol):
        return True
    else:
        return False



deger = int(input("sayi giriniz: "))

sonuc = isBinCompatible(deger)
if(sonuc == True):
    print("sayi bin compatible..")
else:
    print("sayi bin compatible degil")
