#RSA algorithm

#Step 1: take 2 prime numbers as p and q
p=int(input("Enter value of first prime number:"))
q=int(input("Enter value of second prime number"))

#Enter message to be cipher
m = int(input("enter message(int form):"))


#Step 2: find n:    n = p*q
n = p*q
print("n = ",n)

#Step 3:finding value of fi(n)
fi_n = (p-1)*(q-1)
print ("fi_n = ",fi_n)

#Step 4:find public key "e"
lst_p = [2,3,5,7,11,13,17,19]
for i in lst_p:
    if fi_n % i !=0:
        e = i
        break


print("e = ",e)

#Step 5: find d
d= (fi_n +1) / e
if d.is_integer() == False:
    d = (fi_n*2 + 1)/e
print("d = ",d)

#Step 6:encrypting the givn massage
c = (m**e) % n
print("encrypted msg =",c)

#Step 7: decrypting encrypted message:
m = (c**d) % n
print("decrypted msg = ",m)


