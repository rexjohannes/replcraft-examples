import os
import threading

from replcraft.main import ReplCraft

token = os.environ['token']
client = ReplCraft(token)

client.login()

client.watch_all()


def listen_thread():
    while True:
        print(client.listen())


x = threading.Thread(target=listen_thread)
x.start()

# continue doing whatever else

client.disconnect()
