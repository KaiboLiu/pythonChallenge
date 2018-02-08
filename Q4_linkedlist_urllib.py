import urllib
import re

def get_next(n):
    url0 = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
    url = url0 + n
    content = urllib.urlopen(url).read()
    result = re.findall('nothing is (\d+)',content) # return a list
    next_n = ''.join(result)    # result can be either [], or something like ['44827'], do not use result[0]
    return next_n, url, content

def q4():
    #n, steps = '12345', 0
    n, steps = '8022', 86
    while True:
        steps += 1
        n, url, content = get_next(n)
        #print steps, n, content
        if n == '' or steps > 400:
            print steps, url, content
            break


#def better():
    
if __name__ == "__main__":
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
    q4()
