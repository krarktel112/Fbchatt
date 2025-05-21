from fbchat import Client
from fbchat.models import Message

# Replace with your Facebook credentials
USERNAME = "Krarktel@yahoo.com"
PASSWORD = "Yuka338"

# Replace with the thread ID you want to search in
THREAD_ID = "thread_id"

try:
    client = Client(USERNAME, PASSWORD)
    messages = client.fetchThreadMessages(THREAD_ID, limit=20)  # Fetch last 20 messages
    messages.reverse() #messages are reversed to show the oldest message first

    target_message_content = "specific message content" # replace with the message you are looking for
    user_id_found = None
    
    for message in messages:
        if message.text == target_message_content:
            user_id_found = message.author_id
            print(f"User ID from the message '{target_message_content}': {user_id_found}")
            break # Exit the loop after finding the message
    
    if user_id_found is None:
        print(f"Message '{target_message_content}' not found in the last 20 messages.")

    client.logout()

except Exception as e:
    print(f"An error occurred: {e}")
