import random
import math

def function(input):
    global a, b, c
    x = input[0]
    y = input[1]
    return a * ((y - x ** 4) ** 2) + b * ((1 - x) ** 2) + c * y

def rand(input):
    i = random.randrange(0, len(input))
    input[i] += (random.randint(0, 1) - 0.5) / 5000
    return input

temperature = 100
#minans = 10000000
a, b, c = map(int, input().split())
ans_now = [1, 1]
now = function(ans_now)
while temperature > 2.4 ** (-321):
#for gg in range(10000000):
    temperature *= 0.96
    ans_nextgen = rand(ans_now)
    nextgen = function(ans_nextgen)
    print((now - nextgen) / temperature)
    if nextgen < now or random.random() < math.exp((now - nextgen) / temperature):
        #if nextgen < minans:
        #    minans = nextgen
        #    ansb = ans_nextgen
        ans_now = ans_nextgen
        now = nextgen
print(*ans_now)
#print(*ansb)