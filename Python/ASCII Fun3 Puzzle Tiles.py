'''
Because my other two parts of the serie were pretty well received I decided to do another part.

Puzzle Tiles
You will get two Integer n(width) and m (height) and your task is to draw following pattern. Each line is seperated with '\n'.

Both integers are equal or greater than 1. No need to check for invalid parameters.
There are no whitespaces at the end of each line.
For example, for width = 4 and height = 3, you should draw the following pattern:

   _( )__ _( )__ _( )__ _( )__
 _|     _|     _|     _|     _|
(_   _ (_   _ (_   _ (_   _ (_
 |__( )_|__( )_|__( )_|__( )_|
 |_     |_     |_     |_     |_
  _) _   _) _   _) _   _) _   _)
 |__( )_|__( )_|__( )_|__( )_|
 _|     _|     _|     _|     _|
(_   _ (_   _ (_   _ (_   _ (_
 |__( )_|__( )_|__( )_|__( )_|

 
'''

def puzzle_tiles(width, height):
    if height==1 and width==1:
        return width*"   _( )__\n _|     _|\n(_   _ (_\n |__( )_|"
    else:
        result="  "+" _( )__"*width
        for i in range(height):
            if (i+1)%2!=0:
                o1="_|     "*(width)+"_|"
                o2=("(_   _ "*(width))+"(_"
                o3=("|__( )_"*width)+"|"
                result=result+"\n "+o1+"\n"+o2+"\n "+o3
            else:
                e1="|_     "*(width)+"|_"
                e2="  _)"+(" _   _)"*width)
                e3="|__( )_"*width+"|"
                result=result+"\n "+e1+"\n"+e2+"\n "+e3
        return result