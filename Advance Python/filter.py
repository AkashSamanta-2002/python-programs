l = [1,2,3,4,5,6,7,8,9,11,12,10]

# even_list = list(filter(lambda ele: ele % 2 == 0, l))
even_list = list(filter(lambda ele: True if ele % 2 == 0 else False, l))

print(even_list)