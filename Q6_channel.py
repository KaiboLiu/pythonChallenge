import zipfile
import re

def test1():
    zfile = zipfile.ZipFile("Q6_channel.zip")
    print zfile.read('readme.txt')



def q6(zfile,n,i,comment):
    filename = n+'.txt'

    content = zfile.read(filename)
    newn = ''.join(re.findall('nothing is (\d+)',content))
    c1 = zfile.getinfo(filename).comment
    print i, content, '--', c1

    if newn:
        q6(zfile,newn,i+1,comment+c1)
    else: 
        print newn
        print comment+zfile.getinfo(filename).comment

    
if __name__ == "__main__":
    url = 'http://www.pythonchallenge.com/pc/def/peak.html'
    #test1()
    zfile = zipfile.ZipFile("Q6_channel.zip")
    q6(zfile, '90052', 0, '')
    #test2()
    #q5()
