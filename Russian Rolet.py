import os
import time
from time import sleep
import random


file_path = "/Users"

def delete_file(file_path):
    #delete_file(file_path)
    """Löscht eine Datei, wenn sie existiert."""
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Diractory {file_path} was deleted.")
    else:
        print(f"Directory {file_path} dont exist.")

while True:
    print("Hello let`s play a Game")
    time.sleep(1)
    print("I guss a number. If you guss the same I letete the /Users Diractory")
    time.sleep(1)
    randz = random.randint(1, 5)

    usr = int(input("Wat do you guss"))

    print("I guss ?")
    print(randz)
    time.sleep(2)
    
    if randz == usr:
        delete_file(file_path)
        time.sleep(2)
    
