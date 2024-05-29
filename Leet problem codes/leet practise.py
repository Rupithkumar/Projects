class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class SLL1:
    def __init__(self, start=None):
        self.start = start
        self.number = 0

    def insert_element(self, data):
        if self.start is None:
            self.start = Node(data)
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = Node(data)

    def store(self):
        if self.start is None:
            print('List is empty.')
        else:
            temp = self.start
            a = []
            while temp is not None:
                a.append(temp.item)
                temp = temp.next
            print(a)
            a.reverse()
            self.number = int(''.join(map(str, a)))
            print(self.number)

    def __iter__(self):
        return SLLIterable(self.start)

class SLL2:
    def __init__(self, start=None):
        self.start = start
        self.number = 0

    def insert_front(self, data):
        if self.start is None:
            self.start = Node(data)
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = Node(data)

    def store_val(self):
        if self.start is None:
            print('List is empty.')
        else:
            temp = self.start
            b = []
            while temp is not None:
                b.append(temp.item)
                temp = temp.next
            print(b)
            b.reverse()
            self.number = int(''.join(map(str, b)))
            print(self.number)

    def __iter__(self):
        return SLLIterable(self.start)

class SLLIterable:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data

class Addition:
    def __init__(self):
        self.start = None

    def sum(self, num1, num2):
        result = str(num1 + num2)
        print('sum: ',result)
        s=[]
        for x in result:
            s.append(x)
        s.reverse()
        print('Final answer is: ',s)


    def __iter__(self):
        return SLLIterable(self.start)

s1 = SLL1()
s2 = SLL2()

s1.insert_element(9)
s1.insert_element(9)
s1.insert_element(9)
s1.insert_element(9)
s1.insert_element(9)
s1.insert_element(9)
s1.insert_element(9)
s1.store()

s2.insert_front(9)
s2.insert_front(9)
s2.insert_front(9)
s2.insert_front(9)
s2.store_val()

adder = Addition()
adder.sum(s1.number, s2.number)