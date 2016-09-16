import sys
from Area import Area,BACKGR
    
EXT = ".png"
WIDTH = 200
HEIGHT = 180
GAP = 3

# def bg(*params):
#     if len(params)==0:
#         pass
#     elif len(params)==1:
#         background(255*params[0])
#     elif len(params)==2:
#         background(255*params[0], 255*params[0], 255*params[0], 255*params[1])
#     elif len(params)==3:
#         background(255*params[0], 255*params[1], 255*params[2])
#     elif len(params)==4:
#         background(255*params[0], 255*params[1], 255*params[2], 255*params[3])
        
def fc(*params):
    if len(params)==0:
        noFill()
    elif len(params)==1:
        fill(255*params[0])
    elif len(params)==2:
        fill(255*params[0], 255*params[0], 255*params[0], 255*params[1])
    elif len(params)==3:
        fill(255*params[0], 255*params[1], 255*params[2])
    elif len(params)==4:
        fill(255*params[0], 255*params[1], 255*params[2], 255*params[3])
        
def sc(*params):
    if len(params)==0:
        noStroke()
    elif len(params)==1:
        stroke(255*params[0])
    elif len(params)==2:
        stroke(255*params[0], 255*params[0], 255*params[0], 255*params[1])
    elif len(params)==3:
        stroke(255*params[0],255*params[1],255*params[2])
    elif len(params)==4:
        stroke(255*params[0],255*params[1],255*params[2],255*params[3])

def sw(n):
    strokeWeight(n)                

class Assert:
    
    def __init__(self):
        self.equal = True
        self.images = {}
        self.result = {}
        self.area1 = Area(GAP,GAP,                       WIDTH,HEIGHT)
        self.area2 = Area(GAP,GAP+HEIGHT+GAP,            WIDTH,HEIGHT)
        self.area3 = Area(GAP,GAP+HEIGHT+GAP+HEIGHT+GAP, WIDTH,HEIGHT)
        self.count = 0
        self.showText = True
        self.img3 = None
    
    def check(self,filename): # missing ext
        if self.equal == True:
            background(255)
            self.filename = filename
            if filename in self.images:
                img = self.images[filename]
            else:
                img = loadImage(filename + EXT)
            a = self.area2
            if img == None:
                fill(BACKGR)
                strokeWeight(1)
                stroke(0)
                rect(a.x,a.y,a.w,a.h)
            else: 
                self.images[filename] = img
                image(img, a.x, a.y)
            
        if self.img3:
            self.area3.myset(self.img3)        

        if self.showText:        
            textAlign(CENTER,BOTTOM)
            textSize(16)
            strokeWeight(1)
            fill(255)
            text(self.filename,WIDTH/2,505)

            if GAP < mouseX < WIDTH+GAP and (mouseY-GAP) % (HEIGHT+GAP) < HEIGHT :
                s = "x,y = "+str(mouseX-GAP) + ","+str((mouseY-GAP)% (HEIGHT+GAP)) 
                text(s,GAP+WIDTH/2,525)
        
            if self.count==0: fill(0,128,0)
            else:             fill(255,0,0)
            text(str(self.count) + " pixel errors",GAP+WIDTH/2,545)
                                                                        
        return self
        
    def __enter__(self):
        return self
    
    def __exit__(self, type, value, tb):
        if self.filename not in self.result:
            count = self.compare()
            resetMatrix()
            rectMode(CORNER)
            self.result[self.filename] = count==0
        else:
            resetMatrix()
            rectMode(CORNER)
        
    def split(self,c):
        #c = c >> 8; 
        b = c & 0xFF
        c = c >> 8; g = c & 0xFF 
        c = c >> 8; r = c & 0xFF 
        return [r,g,b]
    
    def compare(self):
        self.count = 0
        
        img1 = self.area1.myget()
        img2 = self.area2.myget()
        self.img3 = self.area3.myget()
        
        for i in range(WIDTH+1):
            for j in range(HEIGHT+1):
                r1,g1,b1 = self.split(img1.get(i,j))
                r2,g2,b2 = self.split(img2.get(i,j))
                r,g,b = r1^r2, g1^g2, b1^b2
                c = color(r,g,b)
                self.img3.set(i,j,c) 
                if r+g+b > 0: # [1,2,3]: # or r+g+b>=3*254: 
                    self.count += 1
                    if self.count < 10: print r,g,b
        self.area3.myset(self.img3)        
        self.equal = self.count==0
        if self.equal == False: self.filename2 = self.filename
        if self.count > 0: print self.count,self.filename2
        return self.count
   
    def ok(self):
        if self.equal: 
            self.area1.coords()
            translate(self.area1.x,self.area1.y)
        return not self.equal
    
    def keyPressed(self):
        if key == "!": 
            self.area1.save(self.filename + EXT)!

    def mousePressed(self):
        self.showText = not self.showText            