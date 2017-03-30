#!/usr/bin/python
import math

counter = 0

def fungsi(x):#definisikan fungsi
	return 16 * (x ** 3)- 22 * x + 9 # fungsi 16x^3 - 22x + 9

a = input('Masukkan Tebakan Awal 1 :')#selang awal
b = input('Masukkan Tebakan Awal 2 :')#selang akhir

#mengganti x. mencari nilai fungsi
fa = fungsi(a)
fb = fungsi(b)

e = 0.00001#galat

def cariC(a,b):
	return a + ((b - a) / 2)#mencari nilai c
c = cariC(a,b)#selang posisi tengah untuk membagi

fc = fungsi(c)

r = math.log(math.fabs(b-a)/e,2)

print "|  a  |  b  |  c  | f(a) | f(b) | f(c) |"
while counter < r: # Maksimal iterasi
    counter = counter + 1
    print "===== ", counter, " ====="
    if (fc == 0): break    
    if (counter == 1):
        print "|",a,"|",b,"|",c,"|",fa,"|",fb,"|",fc,"|"
    else:
        if (fc < e): break
        elif (fa * fc) < 0:
            b = c
            fb = fungsi(b)
            c = cariC(a, b)
            fc = fungsi(c)
            print "|",a,"|",b,"|",c,"|",fa,"|",fb,"|",fc,"|"
        elif (fc * fb) < 0:
            a = c
            fa = fungsi(a)
            c = cariC(a, b)
            fc = fungsi(c)
            print "|",a,"|",b,"|",c,"|",fa,"|",fb,"|",fc,"|"
    
print "\nHasil : ", c