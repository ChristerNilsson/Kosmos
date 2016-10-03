from Assert import fc,sc,sw,rd,circle,bg,push,col

def lektion3(ass):

    #with ass.check("horizontalLine"): 
     #   if ass.errors(): return


    #with ass.check("verticalLine"): 
     #   if ass.errors(): return

                
    with ass.check("yellowLine"): 
        if ass.errors(): return
        sc(1,1,0)
        line(20,30,140,160)
    with ass.check("skislope"):
        if ass.errors(): return
        bg(0)
        sc(1,0,0)
    
        for i in range(21):
            line(10*i,0,200,10*i)

    with ass.check("sunshine"):
        if ass.errors(): return
        bg(0)
        sc(1,1,0)
        line(100,0, 100,200)
        line(0,0, 200,200)
        line(20,0, 180,200)
        for i in range(11):
            line(20*i,0, 200-20*i,200)
        for i in range(11):
            line(0,i*20, 200,200-20*i)   
        line(0,20, 200,180)
        line(0,40, 200,160)