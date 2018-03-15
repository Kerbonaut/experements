import random
import math
#print('0'*64, '1'*64, '2'*10, sep = '\n')

#print('0/'*64, '3/'*10)
for i in range(10):
    for i in range(64):
        print(round((random.random()-0.5) * 2, 1), end = ' ')
        #print(1.0, end=' ')
    print('')
#print(2.4**(-321))