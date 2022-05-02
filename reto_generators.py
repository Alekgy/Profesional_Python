import time

def fibo_gen(max):
    n1 = 0
    n2 = 1
    counter = 0
    while True:
        if counter == 0 and n1 <= max:
            counter += 1
            yield n1
        elif counter == 1 and n2 <= max:
            counter += 1
            yield n2
        elif counter > 1: 
            aux = n1 + n2 
            n1, n2 = n2, aux
            if aux >= max:
                raise StopIteration
            counter += 1
            yield aux

if __name__ == "__main__":
    user = int(input("cual es el numero maximo de la iteracion? "))
    fibonacci = fibo_gen(user)
    for element in fibonacci:
        print(element)
        time.sleep(0.5)