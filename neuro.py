from PIL import Image
import math
import os

def load_neuronet(fin, num):
    config = fin.readline()
    lairs = list(map(str, config.split()))
    first_lair = list(map(int, lairs[0].split('/')))
    net = neuronet([lair(len(first_lair), 0, [neuron(i, 0, first_lair[i], []) for i in range(len(first_lair))], 0)], num, config)
    for j in range(1, len(lairs)):
        lair_a = lairs[j]
        lair_i = list(map(int, lair_a.split('/')))
        net.lairs.append(lair(len(lair_i), j, [neuron(i, 0, lair_i[i], list(map(float, fin.readline().split()))) for i in range(len(lair_i))], num))
    return net

def save_neuronet(net, fout):
    fout.write(net.config)
    for i in net.lairs[1:]:
        for j in i.neurons:
            print(j.weights_in)
            for l in j.weights_in:
                fout.write(str(l) + ' ')
            fout.write('\n')

def activate(net, input_data):
    temp = [input_data]
    for i in net.lairs[1:]:
        temp += [[]]
        for j in range(len(i.neurons)):
            temp[-1] += [0]
            for l in range(len(temp[-2])):
                temp[-1][-1] += temp[-2][l] * i.neurons[j].weights_in[l]
            temp[-1][-1] = math.tanh(temp[-1][-1])
    return temp[-1]

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
    def __init__(self, lairs, num, config):
        self.lairs = lairs
        self.num = num
        self.config = config

chek_cmd = 1 #if 0 - exit, if 1 - continue, if 2 - training
fin = open('save_oldv02.txt', 'r')
fout = open('save_newv02.txt', 'w')
net0 = load_neuronet(fin, 0)
while chek_cmd != 0:
    chek_cmd = int(input())
    if chek_cmd == 1:
        #input_data = list(map(int, input().split()))
        im = Image.open("test.png")
        inp = list(im.getdata())
        input_data = [(i[0] + i[1] + i[2]) / 777 for i in inp]
        print(*activate(net0, input_data))
    elif chek_cmd == 2:
        training_pics = os.listdir(path = "training_pics")
        fin_anss = open('training_anss.txt', 'r')
        training_anss = list(map(int, fin_anss.readline().split()))
        for i in range(len(training_anss)):
            im = Image.open('training_pics/' + training_pics[i])
            inp = list(im.getdata())
            input_data = [(i[0] + i[1] + i[2]) / 777 for i in inp]
            ans = activate(net0, input_data)
            target_ans = [-1.0] * 10
            target_ans[training_anss[i]] = 1.0
            #print(ans, target_ans)
            ers = [target_ans[j] - ans[j] for j in range(len(target_ans))]
            error = 0
            for j in ers:
                error += j ** 2
            error /= 2
            print(error) #to be continued...
        fin_anss.close()
save_neuronet(net0, fout)
fin.close()
fout.close()