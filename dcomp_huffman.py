#*******************************************************************************
#                                                                              *
#    program: Huffman Descompresor                                             *
#    author : Patricia Ribes Metidieri                                         *
#                                                                              *
#*******************************************************************************

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%    LIBRARIES     %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

import time
import json


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%    FUNCTIONS     %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def dict_invert(dict):
    inv = {}
    for key,value in dict.items():
        inv[value] = key.encode("utf-8")
    return inv

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%    MAIN    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def main():
    start_time = time.time()
    with open('quijote_huffman.txt',"r") as data_file:
        data = json.load(data_file)

    codes = data["codes"]
    encoded = data["text"]
    inv_codes = dict_invert(codes)

    code = []
    with open("decoded_huffman.txt","w") as out_file:
        for i in encoded:
            code.append(i)
            code = ["".join(code)]
            if code[0] in codes.values():

                out_file.write("%s".encode("utf-8")%(inv_codes[code[0]]))
                code = []

    print "Time =", time.time() - start_time, "s"

if __name__ == "__main__":
    main()