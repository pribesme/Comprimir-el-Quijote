# !/usr/bin/python
# -*- coding: utf-8 -*-
#*******************************************************************************
#                                                                              *
#    program: Huffman Compresor                                                *
#    author : Patricia Ribes Metidieri                                         *
#                                                                              *
#*******************************************************************************


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%    LIBRARIES     %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#from __future__ import unicode_literals

import collections
import time
import bitstring
import pickle
import codecs

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%    CLASSES      %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
class Huffman_node(object):
    def __init__(self, value, key =  None,  left=None, right = None):
        self.left = left
        self.right = right
        self.key = key
        self.value = value

    def children(self):
        return ((self.left, self.right))


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%    FUNCTIONS     %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""
def frequencies(text):
    length = float(len(text))
    #freq = {x: text.count(x)/length for x in text}
    freq = collections.Counter(text)
    freq = sorted(freq.items(), key=lambda t: t[1])
    print freq

    return freq
"""
def frequencies(text):
    txt = list(set(text))
    num = []
    length = float(len(text))
    for i in range(len(txt)):
        num.append(text.count(txt[i])/length)
    d = dict(zip(txt,num))
    freq = sorted(d.items(), key=lambda t: t[1])
    print len(freq)
    return freq

def build_huffman_tree(freq):
    forest = []
    for key, value in freq:
        forest.append(Huffman_node(value, key))

    while ( len(forest) > 1 ):
        left = forest[0]
        right = forest[1]
        del forest[0], forest[0]
        forest.append(Huffman_node(left.value + right.value, left = left, right = right))
        forest.sort(key = lambda x: x.value)

    huffman_tree = forest[0]
    return  huffman_tree


def get_path(node,path=[],codes={}):
    if node.key == None:
        """
        for i in range(2):
            path.append("%i"%(int(not i)))
            get_path(node.children()[i], path, codes)
            path.pop()
        """
        path.append("0")
        get_path(node.children()[0], path, codes)
        path.pop()
        path.append("1")
        get_path(node.children()[1], path, codes)
        path.pop()

    elif node.key not in codes.keys():
        codes[node.key] = "".join(path)
        return get_path(node, path, codes)

    return codes

def huffman_codification(text):
    t = time.time()
    freq = frequencies(text)
    print "\t t_freq = ", time.time() - t
    t = time.time()
    huffman_tree = build_huffman_tree(freq)
    print "\t t_huffman tree = ", time.time() - t
    t = time.time()
    codes = get_path(huffman_tree)
    print "\t t_backtracking = ", time.time() - t
    return codes


def write_binary_file(codes, text):

    data = {}
    data["codes"] = codes
    encoded = []
    for char in text:
        encoded.append(codes[char])

    encoded= "".join(encoded)
    data["text"] = bitstring.Bits(bin = encoded)

    pickleFile = open("quijote_huffman.txt", 'wb')
    pickle.dump(data, pickleFile, pickle.HIGHEST_PROTOCOL)
    pickleFile.close()


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%    MAIN    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def main():
    start_time = time.time()
    text = []

    with codecs.open('quijote.txt', "rb") as f:
        text = f.read().decode("utf8")


    print "time_read_file = ", time.time() - start_time, "s"

    t_huffman_code = time.time()
    codes = huffman_codification(text)
    print "time_huffman_code =", time.time()- t_huffman_code , "s"
    t_write = time.time()
    write_binary_file(codes, text)
    print "time_write = ", time.time() - t_write, "s"
    print "Total time =", time.time() - start_time, "s"
    print codes

if __name__ == "__main__":
    main()


