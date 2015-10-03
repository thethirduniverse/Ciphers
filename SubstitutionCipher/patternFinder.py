import json

#returns true if string matches pattern exactly
#for example, APPLE would match pattern 'ABBCD'
#
#returns True if match
#returns Fale if doesn't match
def exact_match(string,pattern):
    if len(string) != len(pattern):
        return False
    dic = {}
    for i in xrange(len(pattern)):
        if pattern[i] not in dic:
            if string[i] in dic.values():
                return False
            else:
                dic[pattern[i]] = string[i]
        else:
            if string[i] != dic[pattern[i]]:
                return False
    return True

#match the entire string for a pattern
#
#return format:
#None if pattern not found. Otherwise
#an array of tuples, each containing:
#start index, end index(inclusive), matched ciphertext
def match(string,pattern):
    if len(string)<len(pattern):
        return None
    res = []
    for i in xrange(len(string)-len(pattern)+1):
        subString = string[i:i+len(pattern)]
        if exact_match(subString,pattern):
            res.append((i, i+len(pattern)-1, subString))
    return res


#load the pattern file into memory to match the cipher text
#due to the strange format the input file
#some of the values cannot be easily loded, so I discarded them
#user can specify limit, to filter out those patterns with too many candidates
#(>limit)
def read_pattern_file(filename,limit):
    t = 0
    f = open(filename,"r")
    dic = {}
    for line in f:
        t+=1
        i = line.index(',')
        k = line[:i]
        try:
            v = json.loads(line[i+1:])
            if len(v)<=limit:
                dic[k]=v
        except:
            pass
    print "loaded {} of {} entries".format(len(dic),t)
    return dic

#given a string and a pattern dictionary
#match all pattens against the string!
def match_all(string, dic, outfile):
    for pattern in dic:
        res = match(string,pattern)
        if res is not None and len(res)>0:
            outfile.write("***************\n")
            for s,e,c in res:
                outfile.write("index:{}-{} cipher:{}\n".format(s,e,c))
            outfile.write("pattern:{} candidates:{}\n".format(pattern,dic[pattern]))


dic = read_pattern_file("dict.csv",3)
cipher = "RSZWO RSZCK CSGPS GVRTP CKCSG PRSJP YOGVR NPZND ZWOCHZCROC GZWOR SZWOR SZCKS XQNHX VNDWJ YNZWO PCPSG VHOSPNGBTZ ZWOCG GOHXC DONDZ WOCHS HZPCP CGZWO QNHXV NDDNHRPCGZ WOYHN KOPPN DVCSX OKZCK SGVCZ PSHLT ROGZB JROZSYWNH"
cipher = [c for c in cipher if c != " "]
cipher = "".join(cipher) 
print "cipher text is {}".format(cipher)
print "results will be dumped in to patternMatches.txt"
print "please be patient as this can take a long time"
outfile = open("patternMatches.txt","w")
match_all(cipher,dic,outfile)

