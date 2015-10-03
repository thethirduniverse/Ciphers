from collections import Counter

cipher="IYMEC GOBDO JBSNT VAQLN BIEAO YIOHV XZYZY LEEVI PWOBB OEIVZ HWUDE AQALL KROCU WSWRY SIUYB MAEIR DEFYY LKODK OGIKP HPRDE JIPWL LWPHR KYMBM AKNGM RELYD PHRNP ZHBYJ DPMMW BXEYO ZJMYX NYJDQ WYMEO GPYBC XSXXY HLBEL LEPRD EGWXL EPMNO CMRTG QQOUP PEDPS LZOJA EYWNM KRFBL PGIMQ AYTSH MRCKT UMVST VDBOE UEEVR GJGGP IATDR ARABL PGIMQ DBCFW XDFAW UWPPM RGJGN OETGD MCIIM EXTBE ENBNI CKYPW NQBLP GIMQO ELICM RCLAC MV"

cipher = [c for c in cipher if c != " "]
cipher = "".join(cipher)

print "cipher text: {}".format(cipher)
print "length: {}".format(len(cipher))

#a substitution of correlationShift
#this represents the simplest way to decipher a shift cipher
#that is you find the character with the most number of occurrances
#and set it to come from the letter 'e'
#and then you can get all the other plaintexts as well
#
#param: a list of chars or a string
#return: a string
def simpleShift(chars):
    ctr = Counter(chars)
    maxKey,maxValue = None,0
    for k in ctr:
        if ctr[k]>maxValue:
            maxKey = k
            maxValue = ctr[k]
    shift_back = (ord(maxKey) - ord('E'))%26
    res = []
    for c in chars:
        ncord = ord(c) - shift_back
        if ncord < 65:
            ncord+=26
        res.append(chr(ncord))
    return "".join(res)

#print simpleShift("ABCDEFFGHIJKLMNOPQRSTUVWXYZ")

#26 letters, A-Z, frequency in natural English language
P=[8.2, 1.5, 2.8, 4.3, 12.7, 2.2, 2.0, 6.1, 7.0, 0.2, 0.8, 4.0, 2.4, 6.7, 7.5, 1.9, 0.1, 6.0, 6.3, 9.1, 2.8, 1.0, 2.4, 0.2, 2.0, 0.1]

#a substitution of simpleShift
#this represents a correlation attack on shift cipher
#instead of simply setting the most frequent letter to be 'e'
#this method runs through all 26 possibilities
#and computes the correlation of the frequencies of plaintext and ciphertext
#and then it picks the one with highest correlation
#
#param: a list of chars or a string
#return: a string
def correlationShift(chars):
    ctr = Counter(chars)

    #frequencies of the cipher text
    for k in xrange(65,65+26):
        #if some letter cannot be found in the cipher text
        #set its frequency to 0
        if ctr.get(chr(k)) is None:
            ctr[chr(k)]=0
    for k in ctr:
        ctr[k] = float(ctr[k])/len(chars)*100
    Q=[]
    keys = ctr.keys()
    keys.sort()
    for k in keys:
        Q.append(ctr[k])
    
    maxCor,maxKey = None,None
    for k in range(26):
        s=0.0
        i=[e for e in range(26)]
        ik=[(e+k)%26 for e in i]
        for j in range(26):
            s += P[i[j]]*Q[ik[j]]    
        #print "{}:{}:{}".format(k,s,maxCor)
        if s>maxCor:
            maxCor=s
            maxKey=k
        #print "{};{}".format(maxKey,maxCor)
    shift_back = (maxKey)%26
    print "shift back by {}".format(shift_back)
    res = []
    for c in chars:
        ncord = ord(c) - shift_back
        if ncord < 65:
            ncord+=26
        res.append(chr(ncord))
    return "".join(res)

#for each column, run a correlation shift 
#to decide the key for that column 
#and then merge the columns letter by letter
#to try to assemble the plain text
def decode_cols(cols):
    cols_res = []
    for col in cols:
        #print "on col {}".format(i)
        cols_res.append(correlationShift(col))
    str_res = []
    for i in xrange(max([len(col) for col in cols_res])):
        for j in xrange(len(cols_res)):
            try:
                str_res.append(cols_res[j][i])
            except:
                pass
    return "".join(str_res)

#given a cipher and period
#this function splits the cipher in to several columns
#determined by period, and calls decode_cols to decode 
#each column
#then it prints out the result returned by decode_cols
def decode(cipher,period):
    sub = []
    for i in range(period):
        sub.append([])
    for i,c in enumerate(cipher):
        sub[i%period].append(c)
    print decode_cols(sub)

#try different periods
#a good guess would be from 2 to 9,
#but different length could be possible
for i in range(2,10):
    print "when block size is: {}".format(i)
    decode(cipher,i)
