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

    def __sub__(self, a):
        self.num = self.num * a.den - self.den * a.num
        self.den = self.den * a.den
        return self.simplify(self.num, self.den)

    def __mul__(self, a):
        self.num = self.num * a.num
        self.den = self.den * a.den
        return self.simplify(self.num, self.den)

    def __div__(self, a):
        self.num = self.num * a.den
        self.den = self.den * a.num
        return self.simplify(self.num, self.den)

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
        
    def __pow__(self, power):
        newnum = self.num**power
        newden = self.den**power
        simplify(newnum, newden)
    
    def decimal(self, accuracy):
        return round(float(self.num)/float(self.den), accuracy)
