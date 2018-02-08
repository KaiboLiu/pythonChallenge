import string

def q1(s):
    res = ''
    for c in s:
        if c in 'abcdefghijklmnopqrstuvwx':
            res += chr(ord(c)+2)
        elif c in 'yz':
            res += chr(ord(c)-24)
        else: res += c
    return res


def newhint(s):
    transtab = string.maketrans('abcdefghijklmnopqrstuvwxyz','cdefghijklmnopqrstuvwxyzab')
    #s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    return s.translate(transtab)

def myapproach(s):
    a = 'abcdefghijklmnopqrstuvwxyz'
    b = 'cdefghijklmnopqrstuvwxyzab'
    tran = dict(zip(a,b))    
    res = ""
    for c in s: 
        if c in a: res += tran[c]
        else : res += c
    return res

if __name__ == "__main__":
    s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    print(q1(s))
    print(newhint(s))
    print(myapproach(s))

    url  = 'http://www.pythonchallenge.com/pc/def/map.html'
    word0 = 'map'
    word = newhint(word0)
    new_url = url.replace(word0,word) # not inplace
    print(new_url)
    
    