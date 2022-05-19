from Crypto.Cipher import AES


key = b'SIXTEEN BYTE KEY'
def encrypt(message):
    cipher = AES.new(key , AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext,tag=cipher.encrypt_and_digest(message.encode('ascii'))
    return nonce, ciphertext, tag

def decrypt(nonce , ciphertext,tag):
    cipher=AES.new(key , AES.MODE_EAX , nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    try:
        cipher.verify(tag)
        return plaintext.decode('ascii')
    except:
        return False

pt = input("Enter the Message -> ")
nonce,ciphertext,tag=encrypt(pt)
print("\n------------------------------")
print("\n\t\t\t\t\t-- !! AES ENCRYPTION !! --")
print(f"\n\tCipher Text of '{pt}' -> "+str(ciphertext))
print("\n-------------------------")
plaintext = decrypt(nonce,ciphertext,tag)
if not plaintext:
    print("Corrupted Message")
else:
    print("\n----------------------------------------------------------------------")
print("\n\tPlain Test Decrypted -> "+str(plaintext))
print("\n-------------------------------------------------------")