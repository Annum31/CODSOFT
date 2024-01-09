from socket import if_nameindex
import string
import random

# asking from user to generate a password or not
if __name__ == "__main__":
    while True:
        userschoice = input(
            "please enter 'yes' if you want to generate a password else type 'no' to exit: ")
        if userschoice == 'yes':
            break
# password length
password_length = int(input("Enter the length of the password: "))      

#user coice for complexity
choice=input('''choose complexity options for generating random password:
             1.lower case letters
             2.upper case letters
             3.digits
             4.symbols
             5.both(lower and upper case)
             6.quit\n''')

characterList = ""
#Getting character set for password:
while(True):
    choice = int(input("select a option"))
    if (choice == 1):
        #adding lowe-case letters to possible characters
        characterList += string.ascii_lowercase
    elif(choice == 2):
        #adding lowercase_letters to possible characters
     characterList  += string.ascii_uppercase
    elif(choice ==3):
        #adding digits to possible
     characterList += string.digits
    elif(choice == 4):
        #adding symbols to positive characters
     characterList += string.punctuation
    elif(choice == 5):
        #adding all alphabets lower and upper case
     characterList += string.ascii_letters
    elif (choice == 6):
     break
#if user put invalid option
    else :
       print("Invalid option\n please select a valid option")
password = []
#using for loop
for i in range(password_length):
    
    #pinking a random character from our character list
    randomchar = random.choice(characterList)

    #appending a random character to password
    password.append(randomchar)

# printing password as a string
print("The random password is " + "".join(password))
print("Thankyou!")





