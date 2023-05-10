import numpy as np
import py222

SUNE = "R U R' U R U' U' R'"

def stateToTuple(s):
    return tuple(np.sort(np.where(s == 0)[0]))

MARGIN=0.1

def tikzRectangle(x,y,filled):
    f = ""
    if filled:
        f = "[fill=black]"
    return "\\draw{} ({},{}) rectangle ({},{});\n".format(f, x, -y, x+1-MARGIN, -(y+1-MARGIN))

def tikzLine(x,y,dx,dy):
    #if y == 2:
    #    y = 2-MARGIN
    #if x == 2:
    #    x = 2-MARGIN
    if y == -1:
        y = -MARGIN
    if x == -1:
        x = -MARGIN
    return "\\draw[line width=0.7pt] ({},{}) -- ({},{});\n".format(x,-y,x+dx,-(y+dy))

def tikzHorizontalLine(x,y):
    return tikzLine(x,y,1-MARGIN,0)

def tikzVerticalLine(x,y):
    return tikzLine(x,y,0,1-MARGIN)

def tikzImage(s):
    result = ""
    result = result + "\\begin{tikzpicture}[x=0.4cm,y=0.4cm]\n"

    result = result + tikzRectangle(0,0,s[0] == 0)
    result = result + tikzRectangle(1,0,s[1] == 0)
    result = result + tikzRectangle(0,1,s[2] == 0)
    result = result + tikzRectangle(1,1,s[3] == 0)

    if s[8] == 0:
        result = result + tikzHorizontalLine(0,2)
    if s[9] == 0:
        result = result + tikzHorizontalLine(1,2)
    if s[16] == 0:
        result = result + tikzVerticalLine(-1,0)
    if s[17] == 0:
        result = result + tikzVerticalLine(-1,1)
    if s[4] == 0:
        result = result + tikzVerticalLine(2,1)
    if s[5] == 0:
        result = result + tikzVerticalLine(2,0)
    if s[20] == 0:
        result = result + tikzHorizontalLine(1,-1)
    if s[21] == 0:
        result = result + tikzHorizontalLine(0,-1)
                               
    result = result + "\\end{tikzpicture}\n"
    return result

def topFace(s):
  squares = "⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛"
  horizs = "▭             "

  result = ""
  result = result + squares[s[0]] + squares[s[1]]
  result = result + "\n"
  result = result + squares[s[2]] + squares[s[3]]
  result = result + "\n"
  result = result + horizs[s[8]] + horizs[s[9]]
  result = result + "\n"
  return result

def blankState():
  return np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

states = [ blankState() ]
tuples = [ stateToTuple( blankState() ) ]

sune_edges = []
y_edges = []

if __name__ == "__main__":
    # input some scrambled state

    keepGoing = True
    while keepGoing:
        keepGoing = False
        for x in states:
            y = py222.doAlgStr(x,"y")
            if not stateToTuple(y) in tuples:
                tuples.append( stateToTuple(y) )
                states.append(y)
                keepGoing = True
                
            y = py222.doAlgStr(x,SUNE)
            if not stateToTuple(y) in tuples:
                tuples.append( stateToTuple(y) )
                states.append(y)
                keepGoing = True

    for x in states:
        y = py222.doAlgStr(x,"y")
        y_edges.append( tuples.index( stateToTuple(y) ) )
    for x in states:
        y = py222.doAlgStr(x,SUNE)
        sune_edges.append( tuples.index( stateToTuple(y) ) )         
                        
    #print(len(states))
    #print(y_edges)
    #print(sune_edges)

    #print("digraph {")
    #for i in range(len(y_edges)):
    #    print("  {} -> {};".format( i, y_edges[i]) )
    #for i in range(len(sune_edges)):
    #    print("  {} -> {};".format( i, sune_edges[i]) )
    #print("}")

    clusters = []
    clusters.append( [0] )
    clusters.append( [6,3] )
    clusters.append( [8,2,4,1] )
    clusters.append( [26,24,19,18] )
    clusters.append( [11,14,12,9] )
    clusters.append( [21,16,5,10] )
    clusters.append( [22,25,17,23] )
    clusters.append( [20,13,15,7] )
    #py222.printCube( states[6] )

    positions = [
    		(200,470),
		(200,420),
		(350,300),
		(400,0),
		(50,300),
		(200,25),
		(0,0),
		(200,220)
        ]
    # positions = [
    # 		(80,520),
    #     	(96,458),
    #     	(220,450),
    #     	(400,234),
    #     	(57,320),
    #     	(263,162),
    #     	(112,58),
    #     	(191,306)
    #     ]
    positions = [(x / 35.0,y / 35.0) for (x,y) in positions]
    
    #print("digraph {")
    #for i in range(len(states)):
    #    starting = [j for j, xs in enumerate(clusters) if i in xs][0]
    #    ending = [j for j, xs in enumerate(clusters) if sune_edges[i] in xs][0]
    #    print("  {} -> {};".format( starting, ending ) )
    #print("}")

    offsetsX = [x - 0.5 for x in [0,1,0,1]]
    offsetsY = [y - 0.5 for y in [0,0,1,1]]
    
    otherOffsets = {}
    otherOffsets[0] = [ (0,0) ]
    otherOffsets[7] = [ (0,0), (0,1), (0,2), (0,3) ]
    otherOffsets[5] = [ (-0.5,0), (0.5,0), (0,1), (0,2) ]
    
    outin = { (0,1): (0,100),
              (1,3): (110,0),
              (22,25): (300,240),
              (12,0): (90,180),
              (6,12): (180,80),
              (24,26): (240,300),
              #(26,16): (180,0),
              (16,22): (240,290),
              #(25,21): (0,180),
              (21,24): (300,250),
              (4,9): (145,35),
              (17,13): (60,215),
              (13,18): (-35,120),
              (5,11): (180-30,280),
              (2,5): (260,30),
       }
    
    print("\\documentclass{article}")
    print("\\usepackage{tikz}")
    print("\\usepackage{nopageno}")
    print("\\usetikzlibrary{arrows}")
    print("\\begin{document}")
    print("\\begin{tikzpicture}")
    for j in range(len(clusters)):
        cluster = clusters[j]
        for c in range(len(cluster)):
            i = cluster[c]
            offsetX = offsetsX[c] 
            offsetY = offsetsY[c] 
            if j in otherOffsets:
                offsetX = otherOffsets[j][c][0] 
                offsetY = otherOffsets[j][c][1] 
                
            print("\\node ({}) at ({},{}) {{ {} }};\n".format(i, positions[j][0] + offsetX, positions[j][1] + offsetY, tikzImage( states[i] )) )
            #print("\\node (L{}) at ({},{}) {{ \\Huge\\textcolor{{red}}{{{}}} }};\n".format(i, positions[j][0] + offsetX, positions[j][1] + offsetY, i ))
    for i in range(len(states)):
        starting = i
        ending = sune_edges[i]
        if (starting,ending) in outin:
            angleO = outin[(starting,ending)][0]
            angleI = outin[(starting,ending)][1]
            print("\draw[->] ({}) to [out={},in={}] ({});".format(starting, angleO, angleI,ending))
        else:
            print("\draw[->] ({}) -> ({});".format(starting, ending))
    print("\\end{tikzpicture}")        
    print("\\end{document}")
        
    #print(topFace(s))
    #py222.printCube(s)
    #print(stateToTuple(s))
    #py222.printCube(py222.initState())
  
