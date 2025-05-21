from fbchat import Client, ActiveStatus
from fbchat.models import User

# Assuming 'client' is an instance of fbchat.Client
user: User = client.fetchUserInfo("user_id")["user_id"]

if user.active_status == ActiveStatus.ACTIVE:
    print("User is active")
elif user.active_status == ActiveStatus.IDLE:
    print("User is idle")
elif user.active_status == ActiveStatus.OFFLINE:
    print("User is offline")
else:
    print("User active status is unknown")
