cipher="IYMEC GOBDO JBSNT VAQLN BIEAO YIOHV XZYZY LEEVI PWOBB OEIVZ HWUDE AQALL KROCU WSWRY SIUYB MAEIR DEFYY LKODK OGIKP HPRDE JIPWL LWPHR KYMBM AKNGM RELYD PHRNP ZHBYJ DPMMW BXEYO ZJMYX NYJDQ WYMEO GPYBC XSXXY HLBEL LEPRD EGWXL EPMNO CMRTG QQOUP PEDPS LZOJA EYWNM KRFBL PGIMQ AYTSH MRCKT UMVST VDBOE UEEVR GJGGP IATDR ARABL PGIMQ DBCFW XDFAW UWPPM RGJGN OETGD MCIIM EXTBE ENBNI CKYPW NQBLP GIMQO ELICM RCLAC MV"

cipher = [c for c in cipher if c != " "]

print "cipher:{}, length:{}".format(cipher,len(cipher))

from collections import Counter

counter = Counter(cipher)

print counter

ic_num=0
for c in counter:
    a = counter[c]
    ic_num += a*(a-1)

len_cipher = len(cipher)

ic = float(ic_num)/(len_cipher * (len_cipher-1))

print "ic is {}/{} = {}".format(ic_num,(len_cipher * (len_cipher-1)),ic)
