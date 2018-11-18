class Stack:
    elements = []

    def __init__(self, elements):
        self.elements = elements

    def push(self, elem):
        self.elements.append(elem)

    def pop(self):
        return self.elements.pop()

    def print(self):
        if not self.elements:
            print("Стек пуст")
        else: 
            print("Элементы в стеке:")
        print(self.elements[::-1])


st = Stack([1, 1, 2, 3])
st.print()
st.pop()
st.print()
st.push(7)
st.print()
