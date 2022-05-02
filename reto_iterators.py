from time import sleep 

class fiboIter:

    def __init__(self, max = None):
        self.max = max

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
        if not self.max:
            if self.counter == 0:
                self.counter += 1
                return self.n1

            elif self.counter == 1:
                self.counter += 2
                return self.n2

            else:
                self.aux = self.n1 + self.n2
                #self.n1 = self.n2
                #self.n2 = self.aux
                self.n1, self.n2 = self.n2, self.aux
                self.counter += 1
                return self.aux
        else:
            if self.counter == 0 and self.n1 <= self.max:
                self.counter += 1
                return self.n1
            elif self.counter == 1 and self.n2 <= self.max:
                self.counter += 1
                return self.n2
            elif self.counter > 1:
                self.aux = self.n1 + self.n2
                self.n1, self.n2 = self.n2, self.aux
                if self.aux >= self.max:
                    raise StopIteration
                self.counter += 1
                return self.aux

if __name__ == "__main__":
    fibonacci = fiboIter(int(input("cual es el numero maximo del iterador? ")))
    for element in fibonacci:
        print(element)
        sleep(0.5)