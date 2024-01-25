#фильтр
'''
def negImg():
    global img
    save_img("tempimg")
    open_img("tempimg.png")
    negImg2()


def negImg2():
    global img
    for i in range (img.width()):
        for j in range (img.height()):
            v1 = img.get(i,j)[0]
            v2 = img.get(i,j)[1]
            v3 = img.get(i,j)[2]
            img.put('"' + rgbtohex(255-v1,255-v2,255-v3) + '"', to=(i, j))


def rgbtohex(r,g,b):
    return "#{:02x}{:02x}{:02x}".format(r,g,b)'''


