from __future__ import print_function
f = open("dict_ori.csv","r")
o = open("dict.csv","w")
for l in f:
    k = l[:l.index(',')]
    v = l[l.index(',')+1:]
    if v.find('\"') != -1:
        v = v[v.find("\"")+1:v.rfind('\"')]
    v = [c for c in v if c!='\n' and c!='\r']
    v = ["\"" if c == "\'" else c for c in v]
    v = "".join(v)
    print("{},{}".format(k,v), file=o)
