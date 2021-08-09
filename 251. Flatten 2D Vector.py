class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.l = []
        self.index = 0
        for i in vec:
            self.l.extend(i)
        self.count = len(self.l)

    def next(self) -> int:
        self.index += 1
        self.count -= 1
        return self.l[self.index - 1]

    def hasNext(self) -> bool:

        if self.count:
            return True
        return False

# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()