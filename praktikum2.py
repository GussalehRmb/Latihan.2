
bil1 = int(input("masukan bilangan pertama:" ))
bil2 = int(input("masukan bilangan kedua:" ))
bil3 = int(input("masukan bilangan ketiga:" ))
bil4 = int(input("masukan bilangan keempat:" ))

if   (bil1 > bil2 and bil1 > bil4 and bil1 > bil3):
  terbesar = bil1
elif (bil2 > bil1 and bil2 > bil3 and bil2 > bil4):
  terbesar = bil2
elif (bil3 > bil1 and bil3 > bil2 and bil3 > bil4):
  terbesar = bil3
else :
  terbesar = bil4
  
print ("bilangan besar adalah", terbesar)