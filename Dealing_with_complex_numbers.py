

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    def __add__(self, no):
        return Complex(self.real+no.real,self.imaginary+no.imaginary)
    def __sub__(self, no):
        return Complex(self.real-no.real,self.imaginary-no.imaginary)
    def __mul__(self, no):
        return Complex(self.real*no.real-self.imaginary*no.imaginary,       self.real*no.imaginary+self.imaginary*no.real)
    def __truediv__(self, no):
       # x = Complex(self.real*no.real-self.imaginary*no.imaginary + self.real*no.imaginary+self.imaginary*no.real)
        #y = Complex(no.real*no.real + no.imaginary*no.imaginary)
       # return (x)/y
        a = self.real
        b = self.imaginary
        c = no.real
        d = no.imaginary
        real_numerator = a * c + b * d
        imag_numerator = b * c - a * d
        denom = c * c + d * d
        real_div = real_numerator / denom
        imag_div = imag_numerator / denom
        return Complex(real_div, imag_div)
    def mod(self):
        a = self.real
        b = self.imaginary
        return Complex(math.sqrt(a**2+b**2),0)
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

