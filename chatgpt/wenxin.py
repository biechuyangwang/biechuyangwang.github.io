from paddlenlp import Taskflow

dialogue = Taskflow("dialogue")

while True:
    str = input("You:")
    print(f"小六:{dialogue([str])[0]}")