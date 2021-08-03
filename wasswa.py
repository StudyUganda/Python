#a+b=8
#a+c =13
#b+d =8
#c-d=6
import numpy as np
range = np.arange(0.0,13.0,0.1)
list = list(range)

for i in range: 
    a = i
    for i in range:
        b=i
        if (a+b == 8):
            #a+b=8
            for i in range:
                c = i
                if(a+c == 13):
                    for i in range:
                        d = i
                        if (b + d == 8 ) & (c-d == 6):
                            answer={'a':a,'b':b ,'c':c, "d":d}
                            print(answer)
