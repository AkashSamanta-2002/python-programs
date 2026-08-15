# d = {1: "Akash", 2: 10}
# print(d)

# d = {
#     "name": "",
#     "address": "",
#     "ph": None
# }

# print(d)

# def set_user():
#     name = input("Enter your name: ")
#     add = input("Enter your full address: ")
#     ph = int(input("Enter your ph number: "))

#     d["name"] = name
#     d["address"] = add
#     d["ph"] = ph

# set_user()
# print(d)


d = {
    "name": "Akash Samanta",
    "address": {
        "vill": "Mankur",
        "post": "Mankur",
        "p.s": "Bagnan",
        "pin": 711303
    },
    "ph": 8001974980
}

# list = []
# for key in d:
#     print(f"{key}: {d[key]}")
#     list.append(key)

# print(f"\n\n{list}")

for key in d.keys():
    print(key)

for val in d.values():
    print(val)

if "name" in d:
    print(f"Present: {d["name"]}")
else: 
    print(f"Not present")

if "dist" not in d:
    print("not present")
else:
    print(f"Present: {d["name"]}")


    