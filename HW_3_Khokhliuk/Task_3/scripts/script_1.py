import time

def decor(func):
    def wrap(*args, **kwargs):
        func()
    return wrap

@decor
def chek_time(*args, **kwargs):
    list_1 = list()
    while True:
        a = int(input("Enter a number: "))
        if a == 0:
            break
        else:
            list_1.append(a)
    print(list_1)
    print(sum(list_1) / len(list_1))
t1 = time.time()
chek_time()
print(time.time() - t1)