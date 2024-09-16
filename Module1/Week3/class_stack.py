class MyStack:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__stack = []

    def is_empty(self):
        return not bool(len(self.__stack))

    def is_full(self):
        return not bool(self.__capacity - len(self.__stack))

    def pop(self):
        if not self.is_empty():
            top = self.__stack[-1]
            self.__stack.pop()
            return top

    def push(self, value):
        if self.is_full():
            return False
        self.__stack.append(value)
        return True

    def top(self):
        if not self.is_empty():
            return self.__stack[-1]
