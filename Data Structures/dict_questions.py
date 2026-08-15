# userDetails = {
#     "name": "Akash Samanta",
#     "ph": 8001974980
# }

# address = {
#     "vill": "Mankur",
#     "post": "Mankur",
#     "p.s": "Bagnan",
#     "pin": 711303
# }

# for key in address:
#     userDetails[key] = address[key]

# print(userDetails)


# help(dict)


list = [1,1,1,2,1,2,2,3,3,2,1,5,6,2,3,5,6,5,2,3,6,5]

d = {}

for item in list:
    if item in d:
        d[item] += 1
    else:
        d[item] = 1

print(d)