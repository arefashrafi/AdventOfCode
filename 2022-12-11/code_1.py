class Monkey:
    def __init__(self, items: list, operation: list, test: dict) -> None:
        self.items = items
        self.operation = operation
        self.test = test

    def __str__(self) -> str:
        return str(self.__dict__)


lines = open('testinput.txt').readlines()
monkeys = list()
current_monkey = Monkey(None, None, None)
index_current_monkey = 0
for index, line in enumerate(lines[:6]):
    if "Monkey" in line:
        monkeys.append(current_monkey)
        index_current_monkey = index
    if "Starting items" in line:
        key, value = line.split(":")
        current_monkey.items = [int(item) for item in value.split(',')]
    if "Operation" in line:
        key, value = line.split(":")
        current_monkey.operationn m = [int(item) for item in value.split(',')]
    print(current_monkey)
