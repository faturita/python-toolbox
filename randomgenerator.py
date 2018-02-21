#coding: latin-1

# Use me to generate random integers in the exact same way as java's
# RandomGenerator
class RandomGenerator:
    def __init__(self):
        self.seed = 1

    def setseed(self,s):
        self.seed = s ^ 25214903917 & 281474976710655

    def nextbyte(self):
        self.seed = self.seed * 25214903917 + 11 & 281474976710655;
        n = self.seed >> 48 - 31;

        nextnumber = 256*n >> 31

        return nextnumber


if __name__ == "__main__":
    r = RandomGenerator()
    r.setseed(35)

    for i in range(1,10):
        print r.nextbyte()
