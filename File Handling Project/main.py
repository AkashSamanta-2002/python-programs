from pathlib import Path
import os

def read_all_files():
    path = Path('')
    files = list(path.rglob('*'))

    for i, items in enumerate(files):
        print(f"{i + 1}: {items}")

def create_file():
    try:
        read_all_files()
        file_name = input("Enter file name: ")
        p = Path(file_name)

        if not p.exists():
            with  open(p, 'w') as fs:
                data = input("What you want to write in this file:\n")
                fs.write(data)

            print("FILE CREATED SUCCESSFULLY")
        else:
            print("File already exists")
    except Exception as err:
        print(f"An error occured as {err}")

def read_file():
    try:
        read_all_files()
        file_name = input("Enter file name you want to read: ")
        p = Path(file_name)

        if p.exists() and p.is_file():
            with open(p, 'r') as fs:
                data = fs.read()
                print(data)

            print("FILE READED SUCCESSFULLY")
        else:
            print("The file does not exist")
    except Exception as err:
        print(f"An error occured as {err}")

def update_file():
    try:
        read_all_files()
        file_name = input("Enter which file you want to update: ")

        p = Path(file_name)

        if p.exists() and p.is_file():
            print("press 1 for change the name of the file")
            print("press 2 for overwriting the file")
            print("press 3 for appending in the file")

            response = int(input("Enter your response :- "))

            if response == 1:
                new_file_name = input("Enter new file name: ")
                new_path = Path(new_file_name)
                p.rename(new_path)

            if response == 2:
                with open(p, 'w') as fs:
                    data = input("What you want to write in this file this will overwrite the existing data:\n")
                    fs.write(data)

            if response == 3:
                with open(p, 'a') as fs:
                    data = input("What you want to write in this file this will append with the existing data:\n")
                    fs.write(data)

            print("FILE UPDATED SUCCESSFULLY")
    except Exception as err:
        print(f"An error occured as {err}")

def delete_file():
    try:
        read_all_files()
        file_name = input("Enter which file you want to delete: ")
        
        p = Path(file_name)

        if p.exists() and p.is_file():
            os.remove(p)
            print("FILE DELETED SUCCESSFULLY")
        else:
            print("No such file exists")

    except Exception as err:
        print(f"An error occured as {err}")

print("press 1 for creating a file")
print("press 2 for reading a file")
print("press 3 for updating a file")
print("press 4 for deleting a file")

response = int(input("Enter your response :- "))

if response == 1:
    create_file()

elif response == 2:
    read_file()

elif response == 3:
    update_file()

elif response == 4:
    delete_file()