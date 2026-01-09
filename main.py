# ADD
class MySet:
    def __init__(self):
        self.data = []

    def add(self, value):
        if value not in self.data:
            self.data.append(value)

    def show(self):
        print(self.data)

s = MySet()

s.add(10)
s.add(20)
s.add(10)  

s.show()    
