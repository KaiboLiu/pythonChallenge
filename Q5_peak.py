import urllib
import pickle

def test():
    import pprint
    data_url = 'http://www.pythonchallenge.com/pc/def/banner.p'
    data_file = urllib.urlopen(data_url)
    obj = pickle.load(data_file)
    print('type:', type(obj))
    print('len:', len(obj))
    pprint.pprint(obj,None,4)       # level-view, 4 is the indent for a new level
    return obj


def q5():
    obj = test()
    for line in obj:
        s = ''
        for pair in line:
            s += pair[0]*pair[1]
        print(s)
    return



#def better():
    
if __name__ == "__main__":
    url = 'http://www.pythonchallenge.com/pc/def/peak.html'
    #test()
    q5()
