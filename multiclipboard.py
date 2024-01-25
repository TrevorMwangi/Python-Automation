import sys
import clipboard
import json

def save_items(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)

data_save = {"key" : "value", "numbers" : [1,2,3]}
save_items("example.json", data_save)

if len(sys.argv) == 2:
    command = sys.argv[1].lower()
    if command == "save":
        print("save")
    elif command == "load":
        print("load")
    elif command == "list":
        print("load")
    else:
        print("Unknown command")

else:
    print("Please pass not more than one command!")