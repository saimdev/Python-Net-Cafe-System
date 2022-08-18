import os
from datetime import datetime
import send2trash as s2t
import shutil

print("\tAdmin Portal")
def register():
    username = input("Enter username: ")
    username_new = username+"\n"
    users = []
    file = open("usernames.txt", "r")
    for line in file:
        users.append(line)
    #t(users)
    if username_new in users:
        print("Username already exists\n")
    else:
        file = open("usernames.txt", "a")
        file.write(username + "\n")
        file.close()
        password = input("Enter Password: ")
        file = open("passwords.txt", "a")
        file.write(password + "\n")
        file.close()
def login():
    Username = input("Enter your Username: ")
    username1 = Username+"\n"
    checku(username1)
    if found==1:
        Password = input("Enter your Password: ")
        password_new = Password+"\n"
        checkp(password_new)
        if access==1:
            print("You are Logged in!")
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            print("Starting date and time =", dt_string)
            file1 = open("PC1DateTime.txt", "a")
            file1.write("\nStarting date and time ="+dt_string)
            logout()

def logout():
    logout = int(input("TO LOG OUT, ENTER 0: "))
    if logout==0:
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print("Ending date and time =", dt_string)
        file1 = open("PC1DateTime.txt", "a")
        file1.write("\nEnding date and time ="+dt_string)
        target = 'C:\\Users\\Saim\\Desktop\\Download\\'
        for x in os.listdir(target):
            s2t.send2trash(target+x)
        original_path = r'E:\\$t3e!\\Order\\Admin Portal\\PC1DateTime.txt'
        target_path = r'C:\\Users\\Saim\\Desktop\\Downloads\\'
        shutil.copyfile(original_path, target_path)
    else:
        logout()


def checku(username):
    usernames = []
    file = open("usernames.txt", "r")
    for line in file:
        usernames.append(line)
    if username in usernames:
        global found
        found=1
        global index_user
        index_user = usernames.index(username)
    else:
        print("Username not found")
        login()
def checkp(password):
    passwords = []
    file = open("passwords.txt", "r")
    for line in file:
        passwords.append(line)
    if password in passwords:
        global index_pass
        index_pass = passwords.index(password)
        if index_pass==index_user:
            global access
            access=1
        else:
            print("Password not matched")
            login()
    else:
        print("Password not found")
        login()
while(1):
    print("1. Login in\n2. Sign up")
    option = int(input("Choose any option to proceed (1/2): "))

    if option==2:
        register()

    elif option==1:
        login()



