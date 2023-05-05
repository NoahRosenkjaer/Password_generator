import pyperclip as clip# pip install pyperclip
import random
import string

character = string.ascii_letters + string.punctuation + string.digits
password = ""


pass_num = input("How long do you want the password to be? ")


for i in range(int(pass_num)):
    y = random.choice(character)
    password = str(password) + str(y)
    temp = list(password)
random.shuffle(temp)
shuffled_password = ''.join(temp)

print(f"\n -- Your new password --\n\n - {shuffled_password} -\n")
clip.copy(shuffled_password)
print(" - Your password has been copied to the clipboard!")

