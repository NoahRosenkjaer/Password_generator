import pyperclip as clip
import random
import string
import re


def new_pass(num):
    pattern = "(?=.*?[A-Z])(?=.*?[a-z])(?=.+?[0-9])(?=.*?[!'#$%&'()*+,-./:;<=>?@[\]^_`{|}~]).{8,}$"
    character = string.ascii_letters + string.punctuation + string.digits
    password = ""
    
    for i in range(num):
        y = random.choice(character)
        password = str(password) + str(y)
        temp = list(password)
    random.shuffle(temp)
    shuffled_password = ''.join(temp)
    
    matches = re.match(pattern, shuffled_password)
    if not matches:
        print("\nThe password must be at least 10 characters long\n")
        exit()
    else:
        pass

    print(f"\n -- Your new password --\n\n - {shuffled_password} -\n")
    clip.copy(shuffled_password)
    print(" - Your password has been copied to the clipboard!")

def check(word):
    pattern = "(?=.*?[A-Z])(?=.*?[a-z])(?=.+?[0-9])(?=.*?[!'#$%&'()*+,-./:;<=>?@[\]^_`{|}~]).{9,}$"
    matches = re.match(pattern, word)
    if not matches:
        print("The password did not pass the requirements")
    else:
        print("The password passed the requirements!")

def terminal():
    start = input("* List current passwords with: ls \n* Create a new random password with: np \n* Check you current paswords with: check\n> ")

    if start == "np":
        pass_num = input("How long do you want the password to be? ")
        new_pass(int(pass_num))
        start = ""
    elif start == "check":
        check(input("Enter password: "))
        start = ""

terminal()