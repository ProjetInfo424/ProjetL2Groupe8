#!/usr/bin/env python3


def trace_segment(t,x0,y0,x1,y1,couleurf):
    #t=[[couleuri for x in range(largeuri)] for x in range (hauteuri)]
    tmp=0
    tmp2=0
    if x1 < x0 :
        tmp=x0
        x0=x1
        x1=tmp
        tmp2=y0
        y0=y1
        y1=tmp2
        
    deltax = x1-x0
    deltay = y1-y0
    error = 0
    deltaerror = abs(deltay/deltax)
    y=y0
    sign=1
    if y1-y0< 0:
        sign= -1
    for x in range(x0,x1,1):
        t[x][y]=couleurf
        error=error+deltaerror
        while error >= 0.5:
            t[x][y]= couleurf
            y=y+sign
            error=error-1
            
    

    
    

def triangle(x0,y0,x1,y1,x2,y2,largeuri,hauteuri,couleurf,couleuri):
    

    t=[[couleuri for x in range(largeuri)] for x in range (hauteuri)]

    print( "P0 = ({},{})".format( x0, y0 ) )
    print( "P1 = ({},{})".format( x1, y1 ) )
    print( "P2 = ({},{})".format( x2, y2 ) )
    
    trace_segment(t,x0,y0,x1,y1,couleurf);
    trace_segment(t,x1,y1,x2,y2,couleurf);
    trace_segment(t,x2,y2,x0,y0,couleurf);
    





    for i in range(hauteuri):
        print("");
    
        for j in range(largeuri):
            print(str(t[i][j]),end= " ");
            

if __name__ == '__main__' :
    triangle( 1, 1, 20, 25, 15, 4, 50, 50, 0, 1 )
    
