# Удовиченко

class triangle:
    def __init__(self, color = "blue", a = 3, b = 4, c = 5):
            self.color = color
            self.a = a
            self.b = b
            self.c = c

    def square(self):
        return (self.a + self.b + self.c) / 1/2, (self.a + self.b +self.c), (self.a + self.b + self.c) / 3

trial1 = triangle()

print(trial1.color)
print(trial1.square())
