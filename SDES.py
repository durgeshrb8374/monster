from crypto.Cipher import DES
from secrets import token_bytes


key = token_bytes(8)
def encrypt(message):
    cipher = DES.new(key , DES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext,tag=cipher.encrypt_and_digest(message.encode('ascii'))
    return nonce, ciphertext, tag

def decrypt(nonce , ciphertext,tag):
    cipher=DES.new(key , DES.MODE_EAX , nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    try:
        cipher.verify(tag)
        return plaintext.decode('ascii')
    except:
        return False

pt = input("Enter the Message -> ")
nonce,ciphertext,tag=encrypt(pt)
print("\n\t\t\t\t\t-- !! DES ENCRYPTION !! --")
print(f"\n\tCipher Text of '{pt}' ->"+str(ciphertext))
plaintext = decrypt(nonce,ciphertext,tag)
if not plaintext:
    print("Corrupted Message")
else:
    print("\n\tPlain Test Decrypted ->"+str(plaintext))