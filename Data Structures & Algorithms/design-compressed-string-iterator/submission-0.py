class StringIterator:

    def __init__(self, compressedString: str):

        i = 0 
        self.pairs = []
        while i < len(compressedString):
            ch = compressedString[i]
            i += 1

            num = ""

            while i < len(compressedString) and compressedString[i].isdigit():
                num += compressedString[i]
                i +=1

            self.pairs.append((ch, int(num)))

        self.index = 0
        self.remaining = self.pairs[0][1] if self.pairs else 0

    def next(self) -> str:
        if not self.hasNext():
            return ""
        ch, count = self.pairs[self.index]
        self.remaining -=1 

        if self.remaining == 0:
            self.index += 1 
            if self.index < len(self.pairs):
                self.remaining = self.pairs[self.index][1]
        return ch


    def hasNext(self) -> bool:
        return self.index < len(self.pairs)
        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
