import time
import bz2


def test1():
    text = "hello,bz2!" * 100000
    data = bz2.compress(text)
    print('length of text {}'.format(len(text)))
    print('length of compressed data {}'.format(len(data)))
    print('length of compress rate {:.2%}'.format(len(data)*1.0/len(text)))
    print("data: {}".format(repr(data)))  # repr is a function to convert obj to str

    text = bz2.decompress(data)
    print('data: {}\ntext: {}...'.format(repr(data), text[:50]))


def q8():
    un = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
    pw = 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
    
    print(bz2.decompress(un), bz2.decompress(pw))



if __name__ == "__main__":
    url = 'http://www.pythonchallenge.com/pc/def/integrity.html'
    # bee.html -> 'and she is BUSY'
    # busy.html -> 'all bees sound busy too.'
    # hint: bz2
    # given:
    #un: 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
    #pw: 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
    t0 = time.time()
    test1()
    q8()
    print('[finished in {:.5f} s]'.format(time.time()-t0))
