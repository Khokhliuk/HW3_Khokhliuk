d = int(input("d: "))
def gener(d):
    n = 0
    while True:
        yield n
        n += d
gen = gener(d)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))