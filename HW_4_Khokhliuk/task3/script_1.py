
a = int(input("Enter A: "))
b = int(input("Enter B: "))


class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return print(self.a + self.b)

    def sub(self):
        return print(self.a - self.b)

    def mul(self):
        return print(self.a * self.b)

    def div(self):
        if b == 0:
            raise ZeroDivisionError("The divisor must not be zero")
        return print(self.a / self.b)


if __name__ == '__main__':
    calc = Calculator(a, b)
    calc.add()
    calc.sub()
    calc.mul()
    calc.div()


