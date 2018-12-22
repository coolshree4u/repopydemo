class Complex:
    'This class simulates complex number'
    def __init__(self,real=0, imag=0):
        self.real =real
        self.imag = imag

    def get_real(self):
        return self.real

    def get_imag(self):
        return self.imag


    def set_real(self,real):
        self.real= real

    def set_imag(self,imag):
        self.imag= imag


c = Complex(1,1)
print(c)
print(c.real,c.imag)

c.set_imag(10)
c.set_real(10)

print(c.get_real(),c.get_imag())