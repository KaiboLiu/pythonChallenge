import re

def q3():
    s = file('Q3_data.txt').read()
    a = 'abcdefghijklmnopqrstuvwxyz'
    b = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    res = []
    for i,c in enumerate(s[:-9]):
        if c.islower():
            if s[i+1].isupper() and s[i+2].isupper() and s[i+3].isupper():
                if s[i+5].isupper() and s[i+6].isupper() and s[i+7].isupper():
                    if s[i+4].islower() and s[i+8].islower():
                        #dis = ord(s[i+4])-ord('a')
                        #flag = True
                        #for cap in s[i+1:i+8]:
                        #    if ord(cap)-ord('A') < dis:
                        #        flag = False
                        #        break
                        #if flag: res.append(s[i+1:i+8])
                        res.append(s[i+1:i+8])
    return ''.join([st[3] for st in res])

def better():
    s = file('Q3_data.txt').read()
    a = 'abcdefghijklmnopqrstuvwxyz'
    b = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    pattern = "[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]"
    filt = re.findall(pattern, s)
    print(filt)
    return ''.join(filt)
    
if __name__ == "__main__":
    url = 'http://www.pythonchallenge.com/pc/def/equality.html'
    word0 = 'equality'
    #print(q3())
    new_url = url.replace(word0,q3())
    print(new_url)
    new_url = url.replace(word0,better())
    print(new_url)
    