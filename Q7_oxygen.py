from PIL import Image


def test1(image):
    #image.show()
    print(image.size)
    
    x, y = (0,0)
    color = image.getpixel((x,y))   # color is a tuple for R/G/B/A(transparency)
    print(color)
    print(zip(['R','G','B','A'],color))

def test2(image):  # hightlight the grey part
    w, h = image.size
    for x in range(w):
        for y in range(h):
            r,g,b,a = image.getpixel((x,y))
            if r == g == b:    # if grey, update to red
                image.putpixel((x, y), (0, g, 0, a))
            else:              # else, update to black
                image.putpixel((x, y), (0, 0, 0, a))
    image.show()

def q7(image):
    w, h = image.size
    grey = [image.getpixel((x,47))[0] for x in range(1,610,7)]#(0,w,7)]
    print(''.join(map(chr, grey)))
    # output: smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]
    s = [105, 110, 116, 101, 103, 114, 105, 116, 121]
    print('translate the numbers {} to char again --> {}'.format(s, ''.join(map(chr, s))))
    
if __name__ == "__main__":
    url = 'http://www.pythonchallenge.com/pc/def/oxygen.html'
    image = Image.open("Q7_oxygen.png")
#    test1(image)
#    testi2(image)
    test3(image)
