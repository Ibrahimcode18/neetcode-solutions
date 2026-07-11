class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum_value = []
        

    def push(self, val: int) -> None:
        if self.stack and self.minimum_value:
            if val < self.minimum_value[-1]:
                self.minimum_value.append(val)
            else:
                self.minimum_value.append(self.minimum_value[-1])
        else:
            self.minimum_value.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minimum_value.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum_value[-1]
