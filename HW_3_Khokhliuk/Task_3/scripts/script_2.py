from math import sqrt

a = int(input("Enter side A: "))
b = int(input("Enter side B: "))
c = 0


def decor(pythagorean_theorem):
    def wrap(*args, **kwargs):
        res = pythagorean_theorem(*args, **kwargs)
        print("With sides", a, "and", b, "side C is:", res)
        return res
    return wrap


@decor
def pythagorean_theorem_():
    c = sqrt(a**2 + b**2)
    return c


print(pythagorean_theorem_())
