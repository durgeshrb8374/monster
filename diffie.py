#Diffie_hellman key exchange algortihtm

#step 1: consider one prime number
p = int(input("Enter global value P:"))

#step 2: consider one generator
g = int(input("Enter global value g:"))

#step 3: take one private of user A as Xa
Xa = int(input("Enter private key of user A:"))

#step 4: take private key from user B as Xb
Xb = int(input("Enter private key of user B:"))

#now consider public key of user A is Ya and public key of user B is Yb

#now finding public key of users
print("calculating public keys Ya and Yb")
#User A public key
Ya = (g**Xa) % p
print("Ya = :",Ya)
#User B public key
Yb = (g**Xb) % p
print("YB = :",Yb)

#...............................................................
#now finding Ka and Kb to verify that the key exchange done successfully
#finding Ka
Ka = (Yb**Xa) % p

#finding Kb
Kb = (Ya**Xb) % p

if Ka == Kb:
    print("ka = {} \nkb = {}".format(Ka,Kb))
    print("Key exchange done successfully")
