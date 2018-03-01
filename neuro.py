class neuron:
    def __init__(self, num, lairnum, type, weights_in):
        self.num = num
        self.lairnum = lairnum
        self.type = type #type 0 - input, type 3 - output, type 1 - blackbox, type 2 - secret :D
        self.weights_in = weights_in

class lair:
    def __init__(self, width, num, vertices, netnum):
        self.width = width
        self.num = num
        self.neurons = vertices
        self.netnum = netnum

class neuronet:
    def __init__(self, lairs, num):
        self.lairs = lairs
        self.num = num

def activate(net, input_data):
    temp = [input_data]
    for i in net.lairs[1:]:
        temp += [[]]
        #print([i.neurons[j].num for j in range(len(i.neurons))])
        #print(i.neurons[10].num)
        for j in range(len(i.neurons)):
            temp[-1] += [0]
            for l in range(len(temp[-2])):
                #print(type(temp[-1]))
                #print([i.neurons[j].num for j in range(len(i.neurons))])
                #print(i.neurons[10].weights_in)
                #print(j)
                #print(i.neurons[j].num)
                temp[-1][-1] += temp[-2][l] * i.neurons[j].weights_in[l]
    return temp[-1]

chek_cmd = 1 #if 0 - exit, if 1 - continue, if 2 - training
fin = open('save_oldv01.txt', 'r')
fout = open('save_newv01.txt', 'w')
net0 = neuronet([lair(64, 0, [neuron(i, 0, 0, []) for i in range(64)], 0),
                 lair(64, 1, [neuron(i, 1, 1, list(map(int, fin.readline().split()))) for i in range(64)], 0),
                 lair(10, 2, [neuron(i, 2, 3, list(map(int, fin.readline().split()))) for i in range(64)], 0)], 0)
while chek_cmd != 0:
    chek_cmd = int(input())
    if chek_cmd == 1:
        input_data = list(map(int, input().split()))
        print(*activate(net0, input_data))
    elif chek_cmd == 2:
        training_data = open('training_data.txt', 'r')
for i in net0.lairs[1:]:
    for j in i.neurons:
        print(j.weights_in)
        for l in j.weights_in:
            #print(str(l) + ' ')
            fout.write(str(l) + ' ')
        fout.write('\n')
fin.close()
fout.close()