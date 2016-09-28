########################################################
def draw():                                            #
########################################################

    with ass.check("whiteBackground"): 
        if ass.errors(): return
        bg(1)
        
    with ass.check("grayBackground"): 
        if ass.errors(): return
        bg(0.5)
        
    with ass.check("redBackground"): 
        if ass.errors(): return
        bg(1,0,0)
        
    #with ass.check("greenBackground"): 
     #   if ass.errors(): return

                
    with ass.check("yellowBackground"): 
        if ass.errors(): return
        bg(1,1,0)
                
    with ass.check("point"): 
        if ass.errors(): return
        point(10,30)
        

    with ass.check("redPoint"): 
        if ass.errors(): return
        sc(1,0,0)
        point(20,40)

   # with ass.check("greenPoint"): 
    #    if ass.errors(): return

                
    with ass.check("horizontalLine"): 
        if ass.errors(): return
        sc(1,0,1)
        line(10,70,190,70)

    with ass.check("verticalLine"): 
        if ass.errors(): return
        sc(1,1,0)
        sw(10)
        line(110,30,110,170)
                
    with ass.check("yellowLine"): 
        if ass.errors(): return
    
        sc(1,1,0)
        line(20,30,140,160)


    with ass.check("whiteCircle"): 
        if ass.errors(): return
        fc(1)
        circle(60,80,30)

    with ass.check("whiteEmptyCircle"): 
        if ass.errors(): return
        sw(2)
        fc()
        circle(70,90,40)
                
    with ass.check("greenEllipse"): 
        if ass.errors(): return
        fc(0,1,0)
        ellipse(120,60,60,40)

    with ass.check("greenRect"): 
        if ass.errors(): return
        fc(0,1,0)
        rect(60,80,40,50)

    #with ass.check("redRect"):
        #if ass.errors(): return


    with ass.check("whiteTriangle"):
        if ass.errors(): return
        fc(1)
        triangle(20,40,160,100,100,140)
                
    with ass.check("yellowQuad"):
        if ass.errors(): return
        fc(1,1,0)
        quad(40,20,180,20,150,100,100,140)
                
    with ass.check("twoDiscsA"):
        if ass.errors(): return
        fc(1,0,0)
        circle(80,100,40)
        fc(0,1,0)
        circle(100,120,50)

    #with ass.check("twoDiscsB"):
        #if ass.errors(): return

                
    with ass.check("twoDiscsC"):
        if ass.errors(): return
        fc(1,0,0)
        circle(80,100,40)
        fc(0,1,0,0.5)
        circle(120,100,50)
                        
    #with ass.check("twoDiscsD"):
        #if ass.errors(): return


    #with ass.check("twoDiscsE"):
     #   if ass.errors(): return


    #with ass.check("twoDiscsF"):
     #   if ass.errors(): return

                
  #  with ass.check("twoDiscsG"):
   #     if ass.errors(): return


    #with ass.check("twoDiscsH"):
     #   if ass.errors(): return


    with ass.check("cross"):
        if ass.errors(): return
        fc(1,0,0)
        sc()
        rect(115,40,10,100)
        rect(85,70,70,10)
                                        
    with ass.check("squareHole"):
        if ass.errors(): return
        fc(0,1,1)
        sc()
        rect(60,60,80,20)
        rect(60,80,20,40)
        rect(60,120,80,20)
        rect(120,80,20,40)
        fc()
        sc(1,0,0)
        sw(3)
        rect(80,80,40,40)
        rect(60,60,80,80)
       
        
                
        
    # with ass.check("colorCube_2_0"):
    #     if ass.errors(): return
    #     colorCube(2,0)
        
    # with ass.check("colorCube_2_1"):
    #     if ass.errors(): return
    #     colorCube(2,1)
        
    # with ass.check("colorCube_3_0"):
    #     if ass.errors(): return
    #     colorCube(3,0)
        
    # with ass.check("colorCube_3_1"):
    #     if ass.errors(): return
    #     colorCube(3,1)
        
    # with ass.check("colorCube_3_2"):
    #     if ass.errors(): return
    #     colorCube(3,2)
        
    # with ass.check("korg_1"): 
    #     if ass.errors(): return
    #     colorMode(RGB,1,1,1,1)
    #     korg(1,5,color(1,0,0),color(1,1,0))
    
    # with ass.check("korg_2"): 
    #     if ass.errors(): return
    #     colorMode(RGB,1,1,1,1)
    #     korg(2,4,color(0.5),color(1))
        
    # with ass.check("korg_3"): 
    #     if ass.errors(): return
    #     colorMode(RGB,1,1,1,1)
    #     korg(3,3,color(1,1,0),color(1,0,0))
        
    # with ass.check("korg_4"): 
    #     if ass.errors(): return
    #     colorMode(RGB,1,1,1,1)
    #     korg(4,2,color(1),color(0.5))
        
    # with ass.check("korg_5"): 
    #     if ass.errors(): return
    #     colorMode(RGB,1,1,1,1)
    #     korg(5,1,color(1,0,0),color(1,1,0))
        
    # with ass.check("textPythonA"):
    #     if ass.errors(): return

                
    # with ass.check("textPythonB"):
    #     if ass.errors(): return

                
    # with ass.check("textPythonC"):
    #     if ass.errors(): return


                
    # with ass.check("textPythonD"):
    #     if ass.errors(): return


    # with ass.check("rotatedEllipse"):
    #     if ass.errors(): return


    # with ass.check("rotatedRectA"):
    #     if ass.errors(): return

                
    # with ass.check("rotatedRectB"):
    #     if ass.errors(): return

    
    # with ass.check("rotatedRectC"):
    #     if ass.errors(): return

                        
    # with ass.check("pacMan"):
    #     if ass.errors(): return

                
    # Termin 2        
        
    with ass.check("chessRow"):
        if ass.errors(): return
        for i in range(4):
            sc()
            fc(1)
            rect(i*40+20,20,20,20)
            sc(1)
            fc(0.5)
            rect(i*40+40,20,20,20)
            
                        
    with ass.check("chessBoard"):
        if ass.errors(): return
        for i in range(8):
            for j in range(8):     
                fc((((j+i+1)%2)+1)/2.0)
                rect(j*20+20,20*i+20,20,20)
    def dice(x,y,n):
        xo,yo = 20*x,20*y
        if n==1:
            point(xo+10,yo+10)
        if n==2:
            point(xo+8,yo+8)
            point(xo+12,yo+12)
        if n==3:
            point(xo+10,yo+10)
            point(xo+8,yo+8)
            point(xo+12,yo+12)
        if n==4:
            point(xo+8,yo+8)
            point(xo+12,yo+12)
            point(xo+12,yo+8)
            point(xo+8,yo+12)
        if n==5:
            point(xo+10,yo+10)
            point(xo+8,yo+8)
            point(xo+12,yo+12)
            point(xo+12,yo+8)
            point(xo+8,yo+12)
        if n==6:
            point(xo+8,yo+8)
            point(xo+12,yo+12)
            point(xo+12,yo+8)
            point(xo+8,yo+12)
            point(xo+12,yo+10)
            point(xo+8,yo+10)            
                
    with ass.check("dices"):
        if ass.errors(): return
        dice(0,0,1)
        dice(1,0,2)
        dice(2,0,3)
        dice(3,0,4)
        dice(4,0,5)
        dice(5,0,6)
       
            
    with ass.check("manyDices"):
        if ass.errors(): return

                                
    with ass.check("skislope"):
        if ass.errors(): return

                        
    with ass.check("sunshine"):
        if ass.errors(): return

        
    with ass.check("klocka"):
        if ass.errors(): return
        klocka(10,9,30)
        
    with ass.check("klockaB"):
        if ass.errors(): return
        klocka(11,30,15)
        

    with ass.check("recursiveCircles"):
        if ass.errors(): return
        sc(1)
        circles(100,100,100)                            

##########################################################
from Assert import Assert,fc,sc,sw,rd,circle,bg,push,col #
def setup():                                             #
    size(207,680)                                        #
    global ass                                           #
    ass = Assert()                                       #
def keyPressed(): ass.keyPressed()                       #
def mousePressed(): ass.mousePressed()                   #
##########################################################    