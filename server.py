import socket
import threading
import queue
import json

messages = queue.Queue()
clients = []
chat_users = []
text = ""
text_number = 0
messages_history = []

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("localhost", 8888))

with open('history.json', 'r', newline="\n") as f:
    history_json = json.load(f)
    history = json.loads(history_json)
    print(history)

print("Server started.")


def receive():
    while True:
        try:
            message, addr = server.recvfrom(1024)
            messages.put((message, addr))
        except:
            pass


def broadcast():
    while True:
        while not messages.empty():
            message, addr = messages.get()
            print(message.decode())
            text = message.decode()
            if addr not in clients:
                clients.append(addr)
            for client in clients:
                try:
                    if message.decode().startswith("SIGNUP_TAG:"):
                        name = message.decode()[message.decode().index(":") + 1:]
                        server.sendto(f"{name} entered the chat!".encode(), client)
                        text = f"{name} entered the chat!"
                        chat_users.append(name)
                        if len(chat_users) == 2:
                            for chat in history:
                                if chat["chat_users"] == chat_users:
                                    server.sendto(chat["text"].encode(), clients[0])
                                    server.sendto(chat["text"].encode(), clients[1])
                    else:
                        server.sendto(message, client)
                except:
                    clients.remove(client)
            messages_history.append({'chat_users': list(chat_users), 'text': text})
            with open('history.json', 'w+') as f:
                fin = len(history_json) - 1
                json.dump(history_json[:fin] + ", " + json.dumps(messages_history)[1:], f)


thread1 = threading.Thread(target=receive)
thread2 = threading.Thread(target=broadcast)

thread1.start()
thread2.start()
