def fun1(a, b, c):   # positional arguments
    print(f"A: {a}\nB: {b}\nC: {c}")

fun1(10, 2, 312)

def fun2(a, b, c):   # keywords arguments
    print(f"A: {a}\nB: {b}\nC: {c}")

# fun2(c = 10, a = 2, b = 29)
# fun2(1, a = 12, b = 3)  # this will not work as a is already passed as a positional argument
fun2(1, c = 12, b = 3)