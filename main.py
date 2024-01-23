import random
password=''
symbols='+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
length=int(input('Длина строки:'))
for i in range(length):
    password+=random.choice(symbols)
print(password)
    
