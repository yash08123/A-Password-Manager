"""Password Manager by Yash Nagarkar"""

from cryptography.fernet import Fernet

#Generating Key
key  = Fernet.generate_key()
fernet = Fernet(key)

#Retrieving Data
def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            User, passw = data.split("||")
            print("Account: ", fernet.decrypt(User).decode(), "Password: ", fernet.decrypt(passw).decode() + "\n")

#Adding Data
def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    with open('password.txt', 'ab') as f:
        f.write(fernet.encrypt(name.encode()))
        f.write(b'||') 
        f.write(fernet.encrypt(pwd.encode()))

# Main operation
while True:
        
    mode = str(input("Add new password or retrieve old password? (Add ➕/Retrieve) or Quit 'Quit🔙' : ")).lower()

    if mode == "quit":
        break
    elif mode == "add":
        add()
    elif mode == "retrieve":
        view()
    else:
        print("Invalid input")
        continue
