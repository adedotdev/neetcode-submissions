class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        if not self.min_stack or self.getMin() >= val:
            self.min_stack.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        if self.top() == self.getMin():
            self.min_stack.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]


    
        
