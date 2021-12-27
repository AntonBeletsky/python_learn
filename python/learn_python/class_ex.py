class A:

    def __init__(self):
        self.count = 0
        self.data = [1, 3, 8, 7]
        self.print_data()

    def print_data(self):
        self.count = self.count + 1

        print('data :')
        print(self.data)
        print(' count :')
        print(self.count)

        return self.count

class B:

    def __init__(self):

        pass

    def sum(self, a, b):

        return a + b


obja = A()

A.print_data(A())

objb = B()

print ("a+b= ", objb.sum(2,3))
