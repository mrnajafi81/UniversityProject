import hashlib


def isSamePass(password, hashedPassword):
    password = hashlib.sha1(password.encode()).hexdigest()
    if password == hashedPassword:
        return True
    else:
        return False


def decryptPass(hashedPassword):
    chars = [' ','0','1','2','3','4','5','6','7','8','9','\t','\n']
    password = ""
    for a in chars:
        password = a
        if isSamePass(password, hashedPassword):
            return password
        for b in chars:
            password = a + b
            if isSamePass(password, hashedPassword):
                return password
            for c in chars:
                password = a + b + c
                if isSamePass(password, hashedPassword):
                    return password
                for d in chars:
                    password = a + b + c + d
                    if isSamePass(password, hashedPassword):
                        return password
    return "!!!!!!!"

def isInvalidPass(password):
    chars = '0123456789'
    if len(password) != 4:
        return False
    for i in password:
        if i not in chars:
            return False
    return True

# part 2

from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from random import choice, choices, shuffle

lowercaseLetter = list(ascii_lowercase)
uppercaseLetter = list(ascii_uppercase)
digits = list(digits)
specialChars = list(punctuation)
chars = lowercaseLetter + uppercaseLetter + digits + specialChars


def createRandomPass(length):
    password = (
        choice(lowercaseLetter)
        + choice(uppercaseLetter)
        + choice(digits)
        + choice(specialChars)
    )
    password = list(password) + choices(chars, k=(length - 4))
    shuffle(password)
    password = "".join(password)
    return password