import json
import os
from datetime import datetime

f1 = open("history.json", "w")
json.dump({"name": os.getlogin(), "date": datetime.now().strftime('%H:%M:%S')},f1)
f1.close()
    
print("Save successfully!")

f2 = open("history.json", "r")
history = json.load(f2)
print(history)
if history["name"] == "ec2-user":
    print("The {} have login at {}".format(history["name"],history["date"]))
else:
    print("The key ""name"" is not found.")