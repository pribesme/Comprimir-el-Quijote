#*******************************************************************************
#                                                                              *
#    program: Compresor                                                        *
#    author : Patricia Ribes Metidieri                                         *
#                                                                              *
#*******************************************************************************


"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%    LIBRARIES     %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
import numpy as np
import collections


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%    FUNCTIONS     %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
class huffman_node(object):
    def __init__(self, value, key =  None,  left=None, right = None):
        self.left = left
        self.right = right
        self.key = key
        self.value = value

    def children(self):
        return ((self.left, self.right))

def frequencies(text):
    freq = collections.OrderedDict()
    for key in text:
        freq[key] = freq.get(key,0) + 1

    norm = float(sum(freq.values()))
    for key,value in freq.items():
        freq[key]=value/norm
    freq = sorted(freq.items(), key=lambda t: t[1])
    return freq

def walk_huffman_tree(node,num_elements):
    codes = {}
    code = []
    childrens = ()
    while len(codes) < num_elements:
        for i in range(2):
            if node.children()[i].key != None:


            code[i] = string(code[i]) + string(i)
            walk_huffman_tree(node.children()[i],num_elements-1)








#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%    MAINN    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
dict= collections.OrderedDict()
dict["o"] = 3
dict["b"] = 1
dict["p"] = 1
dict["'"] = 2
dict["m"] = 2
dict["j"] = 3
dict[" "] = 12
dict["d"] = 3
dict["i"] = 4
dict["r"] = 5
dict["u"] = 5
dict["a"] = 4
dict["l"] = 6
dict["s"] = 6
dict["e"] = 8

ex =  collections.OrderedDict()

ex["1"] = 0.25
ex["2"] = 0.25
ex["3"] = 0.20
ex["4"] = 0.15
ex["5"] = 0.15
ex = sorted(ex.items(), key=lambda t: t[1])
print ex
forest = []
for key,value in ex:
    print key,value
    forest.append(huffman_node(value,key))

print len(forest)

while len(forest)>1:
    left = forest.pop(0)
    right = forest.pop(0)
    forest.append(huffman_node(left.value+right.value,left = left, right = right))
    forest.sort( key=lambda x: x.value)


