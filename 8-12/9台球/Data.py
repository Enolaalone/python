import math
dig=[[45,45],[500,45],[1000-45,45],[45,600-45],[500,600-45],[1000-45,600-45]]

dot=[[45+111,22.5],[45+222,22.5],[45+333,22.5],[500+111,22.5],[500+222,22.5],[500+333,22.5],
     [45+111,600-22.5],[45+222,600-22.5],[45+333,600-22.5],[500+111,600-22.5],[500+222,600-22.5],[500+333,600-22.5],
     [22.5,45+125],[22.5,45+250],[22.5,45+375],[1000-22.5,45+125],[1000-22.5,45+250],[1000-22.5,45+375]]

balls=[[150,300,'red'],[250,300,'yellow'],[250,400,'green'],[250,200,'orange'],[500,300,'skyblue'],[900,300,'black'],[600,300,'orange'],
       [650, 0+300, 'red'], [650 + 30 * math.sqrt(3) / 2, (30 / 2)+300, 'red'],
       [650 + 30 * math.sqrt(3) / 2, (-30 / 2)+300, 'red'], [650 + 2 * 30 * math.sqrt(3) / 2, (60 / 2)+300, 'red'],
       [650 + 2 * 30 * math.sqrt(3) / 2, (-60 / 2)+300, 'red'], [650 + 2 * 30 * math.sqrt(3) / 2, (0)+300, 'red'],
       [650 + 3 * 30 * math.sqrt(3) / 2, (90 / 2)+300, 'red'], [650 + 3 * 30 * math.sqrt(3) / 2, (30 / 2)+300, 'red'],
       [650 + 3 * 30 * math.sqrt(3) / 2, (-90 / 2)+300, 'red'], [650 + 3 * 30 * math.sqrt(3) / 2, (-30 / 2)+300, 'red'],
       [650 + 4 * 30 * math.sqrt(3) / 2, (120 / 2)+300, 'red'], [650 + 4 * 30 * math.sqrt(3) / 2, (60 / 2)+300, 'red'],
       [650 + 4 * 30 * math.sqrt(3) / 2, (-120 / 2)+300, 'red'], [650 + 4 * 30 * math.sqrt(3) / 2, (-60 / 2)+300, 'red'],
       [650 + 4 * 30 * math.sqrt(3) / 2, (0)+300, 'red']
       ]