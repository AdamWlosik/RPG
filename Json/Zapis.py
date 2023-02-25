"""import json

from main import ninja, zninja

class Zapis:
    def __init__(self, data=None):

        if data is not None:
            self.__dict__ = data

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=False, indent=4)


test = Zapis(data=zninja)
print(test.toJSON())

file = open(r"C:\Users\adamw\OneDrive\Pulpit\zapis.txt", mode="w")
file.write(test.toJSON())
file.close()"""