class Stack():
    list1 = []
    def size(self):
        length = 0
        for x in list1:
            length += 1
        return length
    def push(self, element):
        self.list1 += [element]
    def pop(self):
        last = self.list1[-1]
        listwol = self.list1[:-1]
        self.list1 = listwol
        return last

stack1 = Stack()
stack1.push(3)
stack1.push(7)
stack1.push(8)
print(stack1.pop())
print(stack1.list1)
