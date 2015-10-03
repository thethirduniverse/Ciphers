import re
from fractions import gcd

cipher="IYMEC GOBDO JBSNT VAQLN BIEAO YIOHV XZYZY LEEVI PWOBB OEIVZ HWUDE AQALL KROCU WSWRY SIUYB MAEIR DEFYY LKODK OGIKP HPRDE JIPWL LWPHR KYMBM AKNGM RELYD PHRNP ZHBYJ DPMMW BXEYO ZJMYX NYJDQ WYMEO GPYBC XSXXY HLBEL LEPRD EGWXL EPMNO CMRTG QQOUP PEDPS LZOJA EYWNM KRFBL PGIMQ AYTSH MRCKT UMVST VDBOE UEEVR GJGGP IATDR ARABL PGIMQ DBCFW XDFAW UWPPM RGJGN OETGD MCIIM EXTBE ENBNI CKYPW NQBLP GIMQO ELICM RCLAC MV"

cipher = [c for c in cipher if c != " "]
cipher = "".join(cipher)

for length in range(2,10):
    for i in xrange(0,len(cipher)-length+1):
        tok = cipher[i:i+length]
        occurrance = [i+m.start() for m in re.finditer(tok,cipher[i:])]
        if len(occurrance)>2:
            #for j in xrange(len(occurrance)-1)
            gap = [occurrance[i+1]-occurrance[i] for i in xrange(len(occurrance)-1)]
            g = gap[0]
            for i in xrange(len(gap)):
                g = gcd(g,gap[i])
            if g>1:
                print "occurance of {}, at {}, gcd:{}".format(tok, occurrance,g)
