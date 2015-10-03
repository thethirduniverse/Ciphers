from collections import Counter

cipher = "RSZWO RSZCK CSGPS GVRTP CKCSG PRSJP YOGVR NPZND ZWOCHZCROC GZWOR SZWOR SZCKS XQNHX VNDWJ YNZWO PCPSG VHOSPNGBTZ ZWOCG GOHXC DONDZ WOCHS HZPCP CGZWO QNHXV NDDNHRPCGZ WOYHN KOPPN DVCSX OKZCK SGVCZ PSHLT ROGZB JROZSYWNH"
cipher = [c for c in cipher if c != " "]
print "Cipher Text:"
print "".join(cipher)

counter = Counter(cipher)
shiftmap = {
'R':'m',
'S':'a',
'Z':'t',
'W':'h',
'O':'e',
'K':'c',
'C':'i',
'S':'a',
'G':'n',
'X':'l',
'H':'r',
'Q':'w',
'N':'o',
'V':'d',
'D':'f',
'Y':'p',
'P':'s',
'T':'u',
'J':'y',
'B':'b',
'L':'g'
}

plain = [shiftmap[c] for c in cipher if c in shiftmap or c]
print "Plain Text:"
print "".join(plain)
