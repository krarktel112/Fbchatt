from fbchat import Client, ActiveStatus
from fbchat.models import User
from fbchat import Client
from getpass import getpass
    
email = input("Email: ")
password = getpass("Password: ")
    
client = Client(email, password)
    
if client.isLoggedIn():
    print("Logged in successfully!")
else:
    print("Login failed.")
        
# Assuming 'client' is an instance of fbchat.Client
user: User = client.fetchUserInfo("50403374")["user_id"]

if user.active_status == ActiveStatus.ACTIVE:
    print("User is active")
elif user.active_status == ActiveStatus.IDLE:
    print("User is idle")
elif user.active_status == ActiveStatus.OFFLINE:
    print("User is offline")
else:
    print("User active status is unknown")
