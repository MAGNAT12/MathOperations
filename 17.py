class MathOperations:

    def __init__(self, c=0 ,a=0, b=0) -> None:
        self.a = a
        self.b = b
        self.c = c

    def add_numbers(self):
        if self.c == '+':
            print(self.a + self.b)
        elif self.c == '-':
            print(self.a - self.b)
        elif self.c == '*':
            print(self.a * self.b)
        elif self.c == '/':
            print(self.a / self.b)
        else:
            print('Ошибка')
        


v = MathOperations(c='', a=5, b=6)
v.add_numbers()