
users = {}

def registeruser(username):
  if username in users:
    print(f"Username '{username}' already exists. Please choose a different one.")
    return

  users[username] = {"username": username, "chat_history": []}
  print(f"Welcome, {username}! You are now registered.")

def sendmessage(sender, recipient, message):
  if recipient not in users:
    print(f"User '{recipient}' not found.")
    return

  users[sender]["chat history"].append(f"Sent to {recipient}: {message}")
  users[recipient]["chat history"].append(f"From {sender}: {message}")
  print(f"Message sent from {sender} to {recipient}.")

def viewmessages(username):
  if not users[username]["chat history"]:
    print(f"{username}, you have no messages in your history.")
    return

  print(f"Chat History for {username}:")
  for message in users[username]["chat history"]:
    print(message)

while True:
  action = input("Enter action (register, send, view, quit): ")
  if action == "register":
    username = input("Enter username: ")
    if username not in users: 
      registeruser(username)
  elif action == "send":
    sender = input("Enter your username: ")
    if sender in users:
      recipient = input("Enter recipient username: ")
      message = input("Enter message: ")
      sendmessage(sender, recipient, message)
  elif action == "view":
    username = input("Enter username to view history: ")
    if username in users:
      viewmessages(username)
  elif action == "quit":
    print("Exiting chat system.")
    break
  else:
    print(f"Invalid action. Please try again.")