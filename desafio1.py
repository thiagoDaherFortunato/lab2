from urllib.request import urlopen
import hashlib


hash = "trinity:$6$neo2024$r7SohmtacsW79Zbno//eHNka5kbhY9Riw/3MH0qX8viVM7U0bfCS9sZF7gMGQoMJmuFPGsVf.BPomhLGefhfb/:17337:0:99999:7:::"
myListHash = []
if ":" in hash:
    myListHash = hash.split(':')
password = myListHash[1].split("$")
passwordHash =  password[3]
LIST_OF_COMMON_PASSWORDS = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt').read(), 'utf-8')
salt =  password[2]
for guess in LIST_OF_COMMON_PASSWORDS.split('\n'):
    concatPassword =  guess+ salt
    if password[1] == '6':
        hashedGuess = hashlib.sha512(concatPassword.encode('utf-8'))
        if hashedGuess == passwordHash:
            print("Senha encontrada:", guess)
            break
        elif hashedGuess != passwordHash:
            print("Password guess", str(guess), "does not match, trying next...")
