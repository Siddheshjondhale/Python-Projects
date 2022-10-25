import random
import string

#logic if you write all lower_case,upper_case,specialcharacters manually but python provides all this characters in string package so will use that instead of manual work. Love you python !!!!!!!
# lower_case = ("abcdefghijklmnopqrstuvwxyz")
# upper_case = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
# specialcharacters = ("~`!@#$%^&*()_-+={[}]|\:;\"'<,>.?/")


lower_upper_case = string.ascii_letters #this will give you (abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ)
numbers = string.digits #this will give you (0123456789)
specialcharacters = string.punctuation #this will give you (!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~)

length = int(input("the length of password should be? : "))
#we dont accept length below 12 characters because I dont like :D
while(length < 12):
    print("We dont accept you since you are weak, go and do some workout")
    length = int(input("the length of password should be? : "))

#print(length)
password = random.choices(lower_upper_case+numbers+specialcharacters,k=length)
print("".join(password)) #to remove the bracket and commas from list
print("Password Length is " + str(len(password))) # to check the length of password






# password = random.choices(lower_case+upper_case+specialcharacters,k=18)
# print("".join(password))