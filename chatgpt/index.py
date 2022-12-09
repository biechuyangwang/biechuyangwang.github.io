# python3.9+

# from pychatgpt import Chat

# chat = Chat(email="biechuyangwang@gmail.com", password="li123456")
# chat.cli_chat()

from pychatgpt import Chat

# Initializing the chat class will automatically log you in, check access_tokens
chat = Chat(email="biechuyangwang@gmail.com", password="li123456")
# chat.cli_chat()
answer = chat.ask("你好!")
print(answer)