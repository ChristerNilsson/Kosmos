def draw():
    
    with ass.check("whitePoint"): 
        if ass.ok(): return

    with ass.check("redPoint"): 
        if ass.ok(): return

    with ass.check("greenPoint"): 
        if ass.ok(): return
        
    with ass.check("bluePoint"): 
        if ass.ok(): return
        
    with ass.check("horizontalLine"): 
        if ass.ok(): return

    with ass.check("verticalLine"): 
        if ass.ok(): return
        
    with ass.check("yellowLine"): 
        if ass.ok(): return

    with ass.check("whiteEmptyCircle"): 
        if ass.ok(): return

    with ass.check("greenEllipse"): 
        if ass.ok(): return

    with ass.check("greenRect"): 
        if ass.ok(): return

    with ass.check("redRect"):
        if ass.ok(): return

    with ass.check("whiteTriangle"):
        if ass.ok(): return
        
    with ass.check("yellowQuad"):
        if ass.ok(): return
        
    with ass.check("rotatedRect"):
        if ass.ok(): return
    
    with ass.check("rotatedEllipse"):
        if ass.ok(): return

    with ass.check("twoDiscsA"):
        if ass.ok(): return

    with ass.check("twoDiscsB"):
        if ass.ok(): return
        
    with ass.check("twoDiscsC"):
        if ass.ok(): return
        
    with ass.check("twoDiscsD"):
        if ass.ok(): return

    with ass.check("twoDiscsE"):
        if ass.ok(): return

    with ass.check("twoDiscsF"):
        if ass.ok(): return
        
    with ass.check("twoDiscsG"):
        if ass.ok(): return

    with ass.check("twoDiscsH"):
        if ass.ok(): return

    with ass.check("cross"):
        if ass.ok(): return
                    
    with ass.check("textPython"):
        if ass.ok(): return

    with ass.check("pacMan"):
        if ass.ok(): return
        
    with ass.check("squareHole"):
        if ass.ok(): return
        
    with ass.check("chessBoard"):
        if ass.ok(): return
        
    with ass.check("dices"):
        if ass.ok(): return

    with ass.check("manyDices"):
        if ass.ok(): return


########################################################
from Assert import Assert,fc,sc,sw                     #
def setup(): size(207,553); global ass; ass = Assert() #
def keyPressed(): ass.keyPressed()                     #
def mousePressed(): ass.mousePressed()                 #
########################################################    