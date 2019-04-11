import json

number = 1
primes = []
x = False         # to set the limit of the loop (False = no limit)
printRate = 1000  # to set the printing rate of the new prime numbers
isPrime = True


def save(fileName):
    with open(fileName,'w') as outfile:
        json.dump(primes, outfile)


while 1:
    if type(x) is not bool:
        if number >= x:
            break
        
    number += 1

    for prime in range(int(len(primes)/2)):
        prime = primes[prime]

        if number % prime != 0:
            isPrime = True
        else:
            isPrime = False
            break

    if isPrime:
        #print(number, "  √")   # print each prime number
        primes.append(number)

        if len(primes) % printRate == 0:
            print("you have ",len(primes)," primes numbers !")
            print("between : 0 and ",number,".")
            save('save.json')
    #else:
        #print(number, "  X")   # print each not prime number


print("you have ",len(primes)," primes numbers !")
print("between : 0 and ",number)
save('save.json')
