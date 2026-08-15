l = [1,2,3,4,5,6,7,8,9,10]

"""
def square(ele):
    return ele ** 2

squared_list = list(map(square, l))
"""
squared_list = list(map(lambda ele: ele ** 2, l))

print(squared_list)