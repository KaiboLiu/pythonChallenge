# pythonChallenge
![](https://img.shields.io/badge/language-python-orange.svg)  
codes for the interesting riddles from [Python Challenge](http://www.pythonchallenge.com)


#### 02/07/2018 Wed
##### string mapping
- implement the string.maketrans
    ```python
    import string
    a = 'abc'
    b = 'xyz'
    transtab = string.maketrans(a,b)
    
    s = 'abcbabcbcba'
    res s.translate(transtab)
    
    # the same as dict(zip(a,b))
    ```
##### char, string operations
- check if a char is alpha/letters
    ```python
    s = 'adas21234fsadfavFDDSFGG'
    s[6].isalpha()  # return boolean
    s[0].isupper()  # return False
    s[0].islower()  # return True
    
    import string
    s[4] in string.letters # return boolean
    ```
##### Q3_equality
- regex
    ```python
    import re
    s = file('Q3_data.txt').read()
    pattern_test = "[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]"
    pattern_test = "[^A-Z][A-Z]{3}[a-z][A-Z]{3}[^A-Z]"
    
    # re.findall(parrern, str) returns a list of results
    res_test = re.findall(pattern_test, s)
    ## ['qIQNlQSLi', 'eOEKiVEYj', 'aZADnMCZq', 'bZUTkLYNg', 'uCNDeHSBj', 'kOIXdKBFh', 'dXJVlGZVm', 'gZAGiLQZx', 'vCJAsACFl', 'qKWGtIDCj']
    res = re.findall(pattern, s)
    ## ['l', 'i', 'n', 'k', 'e', 'd', 'l', 'i', 's', 't']
    
    return "".join(res)
    ## linkedlist
    ```
    
##### Q4_linkedlist_urllib
- use `urllib` to open and read url  
    ```python
    import urllib
    content = urllib.urlopen(url).read()
    # .read() returns the whole string in the url
    ```
##### Q5_peak
peak hell -> pickle(泡菜)
- pickle/cPickle is a fundamental, but powerful algorithm for serializing and de-serializing a Python object structure.
    ```python
    import urllib
    import pickle
    import pprint
    
    data_file = urllib.urlopen(url)
    obj = pickle.load(data_file)
    ## return a obj which is a list (may contain lists)
    pprint.pprint(obj,None,4)       # level-view, 4 is the indent for a new level
    ```
    
##### Q6_channel
- zipfile is a module to deal with zip files, it has a function named `zipfile.ZipFile(zipname)`, which returns the obj of a zipfile.
- we can access the inner files with `obj.read(file_name)`
- we can access the info of inner files with `obj.getinfo(file_name).comment`
    ```python
    import zipfile
    zfile = zipfile.ZipFile("Q6_channel.zip")
    # returns the obj of a zipfile(can access in inner files with obj.read(file_name))
    ```
    
