# Implement a stack that accepts the following commands and performs the operations
# described:
# push v: Push integer v onto the top of the stack
# pop: Pop the top element from the stack
# inc i v: Add v to each of the bottom i elements of the stack
# After each operation, print the value at the top of the stack. If the stack is empty, print the
# string 'EMPTY'.
class Stack:
    def __init__(self) -> None:
        self.data = []
        self.length = 0

    def print_top(self):
        if self.length == 0:
            print("EMPTY")
        else:
            print(self.data[-1])

    def push(self, v: int) -> None:
        if not isinstance(v, int):
            raise TypeError("Only integers can be pushed into the stack")
        self.length += 1
        self.data.append(v)
        self.print_top()

    def pop(self) -> int:
        value = self.data.pop()
        self.length -= 1
        self.print_top()
        return value

    def inc(self, i: int, v: int):
        self.data[:i] = list(map(lambda x: x + v, self.data[:i]))
        self.print_top()


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.inc(4, 5)
    print(s.data)
    s.pop()
    s.pop()
    s.pop()
    print(s.data)
