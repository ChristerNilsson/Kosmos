########################################################
def draw():                                            #
########################################################
    
    # with ass.check("whiteBackground"): 
    #     if ass.errors(): return
        
    # with ass.check("grayBackground"): 
    #     if ass.errors(): return
        
    # with ass.check("redBackground"): 
    #     if ass.errors(): return
        
    # with ass.check("greenBackground"): 
    #     if ass.errors(): return
        
    # with ass.check("yellowBackground"): 
    #     if ass.errors(): return
        
    # with ass.check("point"): 
    #     if ass.errors(): return

    # with ass.check("redPoint"): 
    #     if ass.errors(): return

    # with ass.check("greenPoint"): 
    #     if ass.errors(): return
        
    # with ass.check("horizontalLine"): 
    #     if ass.errors(): return

    # with ass.check("verticalLine"): 
    #     if ass.errors(): return
        
    # with ass.check("yellowLine"): 
    #     if ass.errors(): return

    # with ass.check("whiteCircle"): 
    #     if ass.errors(): return

    # with ass.check("whiteEmptyCircle"): 
    #     if ass.errors(): return
        
    # with ass.check("greenEllipse"): 
    #     if ass.errors(): return

    # with ass.check("greenRect"): 
    #     if ass.errors(): return

    with ass.check("redRect"):
        if ass.errors(): return
        fc(1,0,0)
        rect(80,70,40,100)

    with ass.check("whiteTriangle"):
        if ass.errors(): return
        fc(1)
        triangle(100,140,20,40,160,100)
    with ass.check("yellowQuad"):
        if ass.errors(): return
        fc(1,1,0)
        quad(40,20, 180,20, 150,100, 100,140)
        
    # with ass.check("rotatedRectA"):
    #     if ass.errors(): return
        
    # with ass.check("rotatedRectB"):
    #     if ass.errors(): return
    
    # with ass.check("rotatedRectC"):
    #     if ass.errors(): return
            
    # with ass.check("rotatedEllipse"):
    #     if ass.errors(): return

    with ass.check("twoDiscsA"):
        if ass.errors(): return
        fc(1,0,0)
        ellipse(80,100,80,80)
        fc(0,1,0)
        ellipse(100,120,100,100)

    with ass.check("twoDiscsB"):
        if ass.errors(): return
        fc(0,1,0)
        ellipse(140,120,120,120)
        fc(1,0,0)
        ellipse(60,80,100,100)
        
    with ass.check("twoDiscsC"):
        if ass.errors(): return
        fc(1,0,0)
        ellipse(80,100,80,80)
        fc(0,1,0,0.5)
        ellipse(120,100,100,100)
    with ass.check("twoDiscsD"):
        if ass.errors(): return
        fc(1,0,0, 0.5) 
        ellipse(80,90,120,120)
        fc(0,1,0)
        ellipse
    with ass.check("twoDiscsE"):
        if ass.errors(): return

    with ass.check("twoDiscsF"):
        if ass.errors(): return
        
    with ass.check("twoDiscsG"):
        if ass.errors(): return

    with ass.check("twoDiscsH"):
        if ass.errors(): return

    with ass.check("cross"):
        if ass.errors(): return
                    
    with ass.check("textPythonA"):
        if ass.errors(): return
        
    with ass.check("textPythonB"):
        if ass.errors(): return
        
    with ass.check("textPythonC"):
        if ass.errors(): return
        
    with ass.check("textPythonD"):
        if ass.errors(): return

    with ass.check("pacMan"):
        if ass.errors(): return
        
    with ass.check("squareHole"):
        if ass.errors(): return
        
    # Termin 2        
        
    with ass.check("chessRow"):
        if ass.errors(): return
            
    with ass.check("chessBoard"):
        if ass.errors(): return
        
    with ass.check("dices"):
        if ass.errors(): return
            
    with ass.check("manyDices"):
        if ass.errors(): return
                
    with ass.check("skislope"):
        if ass.errors(): return
            
    with ass.check("sunshine"):
        if ass.errors(): return
    
    with ass.check("klocka"):
        if ass.errors(): return
        #klocka(10,9,30)
        
    with ass.check("klockaB"):
        if ass.errors(): return
        #klocka(11,30,15)
        
    with ass.check("recursiveCircles"):
        if ass.errors(): return

########################################################
from Assert import Assert,fc,sc,sw,rd,circle,bg        #
def setup():                                           #
    size(207,4*180-40)                                 #
    global ass                                         #
    ass = Assert()                                     #
def keyPressed(): ass.keyPressed()                     #
def mousePressed(): ass.mousePressed()                 #
########################################################    