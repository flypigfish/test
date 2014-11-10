#from __future__ import print_function
import operator

def my_cmp(key1,key2):
    k1=key1[1:]
    k2=key2[1:]
    
    return int(k1)<int(k2)

if __name__=="__main__":
    
    d={'A10':5,'A13':13,'A1':2}
    print(d)
    d1=sorted(d.items(), cmp=my_cmp,key=lambda x:x[0])
    print(d1)