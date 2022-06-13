import random
import string

digit=[1,2,3,4,5,6,7,8,9,0]
alphabet_lower=list(string.ascii_lowercase)
alphbet_capital=list(string.ascii_uppercase)
symbols=['!','@','#','$','%']

user_input=input("Enter the level of passowrd Ex. High Medium Low")
password=[]
for i in range(4):
    if user_input == "High":
        password.append(random.choice(alphabet_lower))
        password.append(random.choice(symbols))
        password.append(random.choice(alphbet_capital))
        password.append(random.choice(digit))
        random.shuffle(password)
    if user_input == "Low":
        password.append(random.choice(alphabet_lower))
        password.append(random.choice(digit))
        random.shuffle(password)
    if user_input == "Medium":
        password.append(random.choice(alphbet_capital))
        password.append(random.choice(digit))
        password.append(random.choice(alphabet_lower))
        random.shuffle(password)

print("".join(map(str,password)))