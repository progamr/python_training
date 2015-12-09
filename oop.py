# simple fibonacci series
class Fibonacci:

    def __init__(self, a, b):
        self.a, self.b = a, b

    def series(self):
        while True:
            yield(self.b)
            self.a, self.b = self.b, self.b + self.a

f = Fibonacci(0, 1)
for r in f.series():
    if r > 100: break
    print(r)


