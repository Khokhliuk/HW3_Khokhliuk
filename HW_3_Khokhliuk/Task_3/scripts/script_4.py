n = int(input("Enter number "))
list_1 = list(range(0, n))


def decor(res):
    def wrap(*args, **kwargs):
        result = res(*args, **kwargs)
        print(result)
        return result
    return wrap
@decor

def res():
    str_1 = "".join([str(i) for i in list_1])
    return str_1


print(res())


