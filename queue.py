class Queue:
    elements = []

    def __init__(self, elements):
        self.elements = elements

    def push(self, elem):
        self.elements.append(elem)

    def pop(self):
        return self.elements.pop(0)

    def print(self):
        if not self.elements:
            print(" Нет элементов в очереди")
        else:
            print("Элементы в очереди:")
        print(self.elements[::-1])


q = Queue([1,2,4,5,88])
q.push(7)
q.print()
q.pop()
q.print()
