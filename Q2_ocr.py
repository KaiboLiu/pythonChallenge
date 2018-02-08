import string

def q2():
    s = file("Q2_data.txt").read()
    chars = set(s)
    for char in chars:
        print(char,':',s.count(char))
    #news = "".join(set(s))
    #print(news)
    
    #alph = "abcdefghijklmnopqrstuvwxyz"
    
    '''
    res = ''
    for c in s:
        #if c in alph: res += c
        if c in string.letters: res += c
    '''

    res = [c for c in s if c.isalpha()]
    return ''.join(res)


    
if __name__ == "__main__":
    url = 'http://www.pythonchallenge.com/pc/def/ocr.html'
    word0 = 'ocr'
    new_url = url.replace(word0,q2())
    print(new_url)
    