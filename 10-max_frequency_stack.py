import statistics

class Freqstack():

    def __init__(self):
        self.stack = []

    def push(self , value: int):
        self.stack.append(value)
        # print(self.stack)

    def pop(self):
        self.stack.reverse()
        self.stack.remove(statistics.mode(self.stack))
        self.stack.reverse()
        print(self.stack)

x = Freqstack()
x.push(5)
x.push(7)
x.push(5)
x.push(7)
x.push(4)
x.push(5)
x.pop()
x.pop()
x.pop()
x.pop()
x.pop()