# !/usr/bin/env python
# -*- coding: utf-8 -*-
#*******************************************************************************
#                                                                              *
#    program: Lempel-Ziv Compresor                                             *
#    author : Patricia Ribes Metidieri                                         *
#                                                                              *
#*******************************************************************************

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%    LIBRARIES     %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
import bitstring
import time
import pickle
import codecs
#http://stackoverflow.com/questions/6834388/basic-lzw-compression-help-in-python

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%    FUNCTIONS     %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def LZW_compression(text):

    # Create a dictionary with all UTF-8 characters
    #text = "TOBEORNOTTOBE#"
    dict = {chr(i): format(i,'#011b')[2:] for i in range(256)}
    dict["\0"] = "100000000"

    symbol = ""
    result = []
    dict_num= int("0b"+"100000000",2)

    num_bits = 9

    for c in text:
        string = symbol + c
        if string in dict:
            symbol = string
        else:
            result.append(dict[symbol])

            dict[string] = format(dict_num,"#%ib"%(num_bits+2))[2:]
            dict_num += 1
            symbol = c


            if bin(dict_num)[2:] == num_bits*"1":
                num_bits += 1

    # Output the code for symbol.
    if symbol:
        result.append(dict[symbol])

    result = "".join(result)
    return result


def write_binary_file(text):
    text = bitstring.Bits(bin=text)
    pickleFile = open("quijote_LZW.txt", 'wb')
    pickle.dump(text, pickleFile, pickle.HIGHEST_PROTOCOL)
    pickleFile.close()


def LZW_decoder(encoded):
    dict = {format(i, '#011b')[2:] : chr(i) for i in range(256)}
    dict["100000000"] = "\0"

    text= []
    dict_num = int("0b" + "100000000", 2)

    num_bits = 9
    while len(encoded)>num_bits:
        symbols= encoded[0:num_bits]
        encoded= encoded[num_bits:]

        text.append(dict[symbols])

        dict[format(dict_num,"#%ib"%(num_bits+2))[2:]]=dict[symbols] + dict[encoded[0:num_bits]]
        dict_num +=1
        if bin(dict_num)[2:] == num_bits * "1":

            num_bits += 1
    text = "".join(text)
    return text









#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%    MAIN     %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def main():
    start_time = time.time()
    text = []

    with codecs.open('quijote.txt', "rb") as f:
        text = f.read().decode("utf8")


    print "time_read_file = ", time.time() - start_time, "s"

    t_LWZ = time.time()
    codeLWZ = LZW_compression(text)
    print "time_LWZ =", time.time()- t_LWZ, "s"
    t_write = time.time()
    write_binary_file(codeLWZ)
    print "time_write = ", time.time() - t_write, "s"
    print "Total time compression=", time.time() - start_time, "s"

    with open('quijote_LZW.txt',"r") as data_file:
        encoded = pickle.load(data_file)

    t_desc = time.time()
    encoded = bitstring.Bits(encoded).bin




    #text = LZW_decoder(encoded)
    print "time_decomp = ", time.time()-t_desc
    t_write = time.time()
    #output = open("quijote_desc_LZW.txt", 'wb')
    #pickle.dump(text, output, pickle.HIGHEST_PROTOCOL)
    #output.close()
    print "time_write =", time.time()-t_desc
    print "Total descompresion time = ", time.time()-t_desc

if __name__ == "__main__":
    main()