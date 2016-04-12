# python2
class RollingHash:
    def __init__(self, string, size):
        self.str = string
        self.hash = 0

        for i in xrange(0, size):
            self.hash += ord(self.str[i])
        self.init = 0
        self.end = size

    def update(self):
        if self.end <= len(self.str) - 1:
            self.hash -= ord(self.str[self.init])
            self.hash += ord(self.str[self.end])
            self.init += 1
            self.end  += 1

    def digest(self):
        return self.hash

    def text(self):
        return self.str[self.init:self.end]

def read_input():
    return (raw_input().rstrip(), raw_input().rstrip())

def get_occurrences(pattern, text):
    result = ""
    hashP = RollingHash(pattern, len(pattern))
    hashT = RollingHash(text, len(pattern))

    for i in range(len(text) - len(pattern) + 1 ):
        if hashP.digest() == hashT.digest():
            if hashT.text() == pattern:
                result += str(i) + " "
        hashT.update()
    return result

if __name__ == '__main__':
    print(get_occurrences(*read_input()))
