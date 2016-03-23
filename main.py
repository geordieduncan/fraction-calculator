class Fraction:
    def __init__(self, num, den):

        self.num = num
        self.den = den

    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    def __add__(self, a):
        self.num = self.num * a.den + self.den * a.num
        self.den = self.den * a.den
        return self.simplify(self.num, self.den)

    def return_num(self):
        return self.num

    def return_den(self):
        return self.den

    def simplify(self, num, den):
        self.num = num
        self.den = den
        i = 2
        while i <= self.den:
            if self.num % i == 0:
                if self.den % i == 0:
                    self.num /= i
                    self.den /= i
                    i = 1
            i += 1
        return str(self.num) + '/' + str(self.den)


fractionA = Fraction(3, 5)
fractionB = Fraction(4, 5)

print fractionA + fractionB
