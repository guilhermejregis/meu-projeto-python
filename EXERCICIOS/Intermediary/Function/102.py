def fatorial(num):
    f = 1
    for c in range(num, 0, -1):
        f*=c
    return f


print(fatorial(5))