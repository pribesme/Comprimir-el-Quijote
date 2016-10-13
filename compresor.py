#*******************************************************************************
#                                                                              *
#    program: Huffman Compresor                                                *
#    author : Patricia Ribes Metidieri                                         *
#                                                                              *
#*******************************************************************************


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%    LIBRARIES     %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
import collections
import time
import bitstring
import pickle

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%    CLASSES      %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
class huffman_node(object):
    def __init__(self, value, key =  None,  left=None, right = None):
        self.left = left
        self.right = right
        self.key = key
        self.value = value

    def children(self):
        return ((self.left, self.right))


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%    FUNCTIONS     %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def frequencies(text):
    freq = collections.OrderedDict()
    for key in text:
        freq[key] = freq.get(key,0) + 1

    norm = float(sum(freq.values()))
    for key,value in freq.items():
        freq[key]=value/norm
    freq = sorted(freq.items(), key=lambda t: t[1])
    return freq

def build_huffman_tree(freq):
    forest = []
    for key, value in freq:

        forest.append(huffman_node(value, key))

    while len(forest) > 1:
        left = forest.pop(0)
        right = forest.pop(0)
        forest.append(huffman_node(left.value + right.value, left=left, right=right))
        forest.sort(key=lambda x: x.value)

    huffman_tree = forest[0]
    return  huffman_tree


def get_path(node,path=[],codes={}):
    if node.key == None:
        for i in range(2):
            path.append("%i"%(int(not i)))
            get_path(node.children()[i],path,codes)
            path.pop()

    elif node.key not in codes.keys():
        codes[node.key] = "".join(path)
        return get_path(node, path, codes)

    return codes

def huffman_codification(text):
    freq = frequencies(text)
    huffman_tree = build_huffman_tree(freq)
    codes = get_path(huffman_tree)
    return codes


def write_binary_file(codes,text):

    data = {}
    data["codes"] = codes
    encoded = []
    for char in text:
        encoded.append(codes[char])

    encoded= "".join(encoded)
    data["text"] = bitstring.Bits(bin=encoded)

    pickleFile = open("quijote_huffman.txt", 'wb')
    pickle.dump(data, pickleFile, pickle.HIGHEST_PROTOCOL)
    pickleFile.close()


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%    MAIN    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def main():
    start_time = time.time()
    text = []

    #f = codecs.open('Twenty-Thousand-Leagues-Under-the-Sea-by-Jules-Verne.txt', encoding='utf-8')
    with open('Twenty-Thousand-Leagues-Under-the-Sea-by-Jules-Verne.txt',"r") as f:
        for lines in f:
            text.extend(list(lines))


    codes = huffman_codification(text)

    write_binary_file(codes, text)

    print "Time =", time.time() - start_time, "s"

if __name__ == "__main__":
    main()

