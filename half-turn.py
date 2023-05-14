import numpy as np
import py222
import math
import numpy as np
import sys

def euler_to_rotation_matrix(yaw, pitch, roll):
    # Convert angles to radians
    yaw = np.deg2rad(yaw)
    pitch = np.deg2rad(pitch)
    roll = np.deg2rad(roll)

    # Yaw
    R_z = np.array([[np.cos(yaw), -np.sin(yaw), 0],
                    [np.sin(yaw), np.cos(yaw), 0],
                    [0, 0, 1]])

    # Pitch
    R_y = np.array([[np.cos(pitch), 0, np.sin(pitch)],
                    [0, 1, 0],
                    [-np.sin(pitch), 0, np.cos(pitch)]])

    # Roll
    R_x = np.array([[1, 0, 0],
                    [0, np.cos(roll), -np.sin(roll)],
                    [0, np.sin(roll), np.cos(roll)]])

    # Combined rotation matrix
    R = np.dot(R_z, np.dot(R_y, R_x))

    return R


def stateToTuple(s):
    return tuple(np.sort(np.where(s == 0)[0]))

states = [ py222.doAlgStr(py222.initState(),"R R") ]
tuples = [ tuple(x) for x in states ]

 #       ┌──┬──┐
 #       │ 0│ 1│
 #       ├──┼──┤
 #       │ 2│ 3│
 # ┌──┬──┼──┼──┼──┬──┬──┬──┐
 # │16│17│ 8│ 9│ 4│ 5│20│21│
 # ├──┼──┼──┼──┼──┼──┼──┼──┤
 # │18│19│10│11│ 6│ 7│22│23│
 # └──┴──┼──┼──┼──┴──┴──┴──┘
 #       │12│13│
 #       ├──┼──┤
 #       │14│15│
 #       └──┴──┘

 #    ┌──┐
 #    │ 0│
 # ┌──┼──┼──┬──┐
 # │ 4│ 2│ 1│ 5│
 # └──┼──┼──┴──┘
 #    │ 3│
 #    └──┘

 
def cubeToTikz(s):
    face_colors = ['white','orange!85!yellow!85!white','blue!70!white','yellow!95!black','red!90!blue','green!90!black']
    
    result = '''
    \\begin{tikzpicture}[scale=0.415,line join=round]
    \\begin{scope}[tdplot_main_coords]
    \\filldraw [canvas is yz plane at x=1] (-1,-1) rectangle (1,1);
    \\filldraw [canvas is xz plane at y=1] (-1,-1) rectangle (1,1);
    \\filldraw [canvas is yx plane at z=1] (-1,-1) rectangle (1,1);
    '''
    
    result = result + "\\draw [canvas is yz plane at x=1,shift={(-1,-1)},fill=" + face_colors[s[10]] + "](0.5,0) -- ({1-\\radius},0) arc (-90:0:\\radius) -- (1,{1-\\radius}) arc (0:90:\\radius) -- (\\radius,1) arc (90:180:\\radius) -- (0,\\radius) arc (180:270:\\radius) -- cycle;"
    result = result + "\\draw [canvas is yz plane at x=1,shift={(0,-1)},fill=" + face_colors[s[11]] + "](0.5,0) -- ({1-\\radius},0) arc (-90:0:\\radius) -- (1,{1-\\radius}) arc (0:90:\\radius) -- (\\radius,1) arc (90:180:\\radius) -- (0,\\radius) arc (180:270:\\radius) -- cycle;"
    result = result + "\\draw [canvas is yz plane at x=1,shift={(-1,0)},fill=" + face_colors[s[8]] + "](0.5,0) -- ({1-\\radius},0) arc (-90:0:\\radius) -- (1,{1-\\radius}) arc (0:90:\\radius) -- (\\radius,1) arc (90:180:\\radius) -- (0,\\radius) arc (180:270:\\radius) -- cycle;"
    result = result + "\\draw [canvas is yz plane at x=1,shift={(0,0)},fill=" + face_colors[s[9]] + "](0.5,0) -- ({1-\\radius},0) arc (-90:0:\\radius) -- (1,{1-\\radius}) arc (0:90:\\radius) -- (\\radius,1) arc (90:180:\\radius) -- (0,\\radius) arc (180:270:\\radius) -- cycle;"

    result = result + "\\draw [canvas is xz plane at y=1,shift={(-1,-1)},fill=" + face_colors[s[7]] + "](0.5,0) -- ({1-\\radius},0) arc (-90:0:\\radius) -- (1,{1-\\radius}) arc (0:90:\\radius) -- (\\radius,1) arc (90:180:\\radius) -- (0,\\radius) arc (180:270:\\radius) -- cycle;"
    result = result + "\\draw [canvas is xz plane at y=1,shift={(0,-1)},fill=" + face_colors[s[6]] + "](0.5,0) -- ({1-\\radius},0) arc (-90:0:\\radius) -- (1,{1-\\radius}) arc (0:90:\\radius) -- (\\radius,1) arc (90:180:\\radius) -- (0,\\radius) arc (180:270:\\radius) -- cycle;"
    result = result + "\\draw [canvas is xz plane at y=1,shift={(-1,0)},fill=" + face_colors[s[5]] + "](0.5,0) -- ({1-\\radius},0) arc (-90:0:\\radius) -- (1,{1-\\radius}) arc (0:90:\\radius) -- (\\radius,1) arc (90:180:\\radius) -- (0,\\radius) arc (180:270:\\radius) -- cycle;"
    result = result + "\\draw [canvas is xz plane at y=1,shift={(0,0)},fill=" + face_colors[s[4]] + "](0.5,0) -- ({1-\\radius},0) arc (-90:0:\\radius) -- (1,{1-\\radius}) arc (0:90:\\radius) -- (\\radius,1) arc (90:180:\\radius) -- (0,\\radius) arc (180:270:\\radius) -- cycle;"

    result = result + "\\draw [canvas is yx plane at z=1,shift={(-1,-1)},fill=" + face_colors[s[0]] + "](0.5,0) -- ({1-\\radius},0) arc (-90:0:\\radius) -- (1,{1-\\radius}) arc (0:90:\\radius) -- (\\radius,1) arc (90:180:\\radius) -- (0,\\radius) arc (180:270:\\radius) -- cycle;"
    result = result + "\\draw [canvas is yx plane at z=1,shift={(0,-1)},fill=" + face_colors[s[1]] + "](0.5,0) -- ({1-\\radius},0) arc (-90:0:\\radius) -- (1,{1-\\radius}) arc (0:90:\\radius) -- (\\radius,1) arc (90:180:\\radius) -- (0,\\radius) arc (180:270:\\radius) -- cycle;"
    result = result + "\\draw [canvas is yx plane at z=1,shift={(-1,0)},fill=" + face_colors[s[2]] + "](0.5,0) -- ({1-\\radius},0) arc (-90:0:\\radius) -- (1,{1-\\radius}) arc (0:90:\\radius) -- (\\radius,1) arc (90:180:\\radius) -- (0,\\radius) arc (180:270:\\radius) -- cycle;"
    result = result + "\\draw [canvas is yx plane at z=1,shift={(0,0)},fill=" + face_colors[s[3]] + "](0.5,0) -- ({1-\\radius},0) arc (-90:0:\\radius) -- (1,{1-\\radius}) arc (0:90:\\radius) -- (\\radius,1) arc (90:180:\\radius) -- (0,\\radius) arc (180:270:\\radius) -- cycle;"
    
    result = result + "\\end{scope}\\end{tikzpicture}"
    return result

def permutationToCycle(p):
    cycles = []

    todo = list(range(len(p)))
    while len(todo) > 0:
        i = todo.pop()
        cycle = [i]
        cycles.append(cycle)
        while not p[i] in cycle: 
            i = p[i]
            cycle.append(i)
            todo.remove(i)
        
    return [tuple(x) for x in cycles]

# vertices = (0, ±1, ±2)
# edge vectors = (0, \pm 1, \pm 1)

def transformation(v):
    v = np.array(v)
    # Euler angles (in radians)
    yaw = -10
    pitch = -9
    roll = 0

    # Convert Euler angles to rotation matrix
    rotation_matrix = euler_to_rotation_matrix(roll, pitch, yaw)
    v = np.matmul(rotation_matrix, v)
    
    return v[0] - 0.8, v[1] + 1.0, v[2] + 11

def projection(v):
    v = transformation(v) 
    x = 29 * v[0] / v[2]
    y = 29 * v[1] / v[2]
    return x,y

def pointToPermutation(v):
    v = np.array(v)
    w = (v[np.nonzero(v)] > 0).dot( [2,1] )
    #v = list(np.abs(v))
    #v.insert( w, 3 )
    return v

def printEdge( i, j, color ):
    if i > j:
        i, j = j, i

    angle = 20
    outin = { (6,14): (180+angle,-angle),
              (3,9): (180+angle+60,-angle+60),
              (15,22): (-angle+60+60,180+angle+60+60),
              (18,19): (angle, 180-angle),
              (2,7): (180-angle+60,angle+60),
              (8,17): (180-angle+60+60,angle+60+60)
             }
    
    colors = { 'R': 'edgeR', 'U': 'edgeU', 'F': 'edgeF' }
    c = colors[color]
    
    if (i,j) in outin:
        angleO = outin[(i,j)][0]
        angleI = outin[(i,j)][1]
        print("\draw[{}] ({}) to [out={},in={}] ({});".format(c,i, angleO, angleI,j))
    else:
        print("\draw[{}] ({}) -> ({});".format(c,i,j))

def makeHexagon( positions, h, v, c, ix ):
    positions[ix[0]] = (c[0] + h,c[1] + v)
    positions[ix[1]] = (c[0] - h,c[1] + v)
    positions[ix[2]] = (c[0] -2*h,c[1])
    positions[ix[3]] = (c[0]-h,c[1]-v)
    positions[ix[4]] = (c[0]+h,c[1]-v)
    positions[ix[5]] = (c[0]+2*h,c[1])
    
if __name__ == "__main__":
    # input some scrambled state

    keepGoing = True
    while keepGoing:
        keepGoing = False
        for x in states:
            y = py222.doAlgStr(x,"R R")
            if not np.any( [tuple(y) == z for z in tuples] ):
                states.append(y)
                tuples.append( tuple(y) )
                keepGoing = True
            y = py222.doAlgStr(x,"F F")
            if not np.any( [tuple(y) == z for z in tuples] ):
                states.append(y)
                tuples.append( tuple(y) )
                keepGoing = True
            y = py222.doAlgStr(x,"U U")
            if not np.any( [tuple(y) == z for z in tuples] ):
                states.append(y)
                tuples.append( tuple(y) )
                keepGoing = True
                
    #print(len(states))

    gR = [tuples.index(tuple(py222.doAlgStr(x,"R R"))) for x in states]
    gU = [tuples.index(tuple(py222.doAlgStr(x,"U U"))) for x in states]
    gF = [tuples.index(tuple(py222.doAlgStr(x,"F F"))) for x in states]

    #print(permutationToCycle(gR))
    #print(permutationToCycle(gU))
    #print(permutationToCycle(gF))

    # print("graph {")
    # for i in range(len(states)):
    #     if i < gR[i]:
    #         print("  {} -- {} [color=\"red\"];".format( i, gR[i]) )
    # for i in range(len(states)):
    #     if i < gU[i]:
    #         print("  {} -- {} [color=\"blue\"];".format( i, gU[i]) )
    # for i in range(len(states)):
    #     if i < gF[i]:
    #         print("  {} -- {} [color=\"green\"];".format( i, gF[i]) )
    # print("}")
    
    with open('half-turn-header.tex', 'r') as file:
        for line in file:
            print(line.rstrip('\n'))


    positions = []
    for i in range(len(states)):
        positions.append( (0,0) )
    size = 2.9
    h = (2.0 * size) / 4.0
    v = (math.sqrt(3) * size) * 0.5
    makeHexagon( positions, h, v, (0, 0), [1,5,13,21,11,4] )
    makeHexagon( positions, h, v, (3*h, v), [2,0,1,4,10,6] )
    makeHexagon( positions, h, v, (3*h, -v), [10,4,11,20,17,19] )
    makeHexagon( positions, h, v, (0, -2*v), [11,21,16,7,15,20] )
    makeHexagon( positions, h, v, (-3*h, -v), [13,23,18,9,16,21] )
    makeHexagon( positions, h, v, (-3*h, v), [12,22,14,23,13,5] )
    makeHexagon( positions, h, v, (0, 2*v), [3,8,12,5,1,0] )
    
    for i in range(len(states)):
        v = states[i]
        x, y = positions[i]
        print("\\node ({}) at ({},{}) {{ {} }};\n".format(i, x, y, cubeToTikz(states[i]) ) )
        #print("\\node ({}) at ({},{}) {{ {} }};\n".format(i, x, y, i ) )

    for i in range(len(states)):
         if i < gR[i]:
             printEdge( i, gR[i], 'R' )
    for i in range(len(states)):
         if i < gU[i]:
             printEdge( i, gU[i], 'U' )
    for i in range(len(states)):
         if i < gF[i]:
             printEdge( i, gF[i], 'F' )
    
    with open('half-turn-footer.tex', 'r') as file:
        for line in file:
            print(line.rstrip('\n'))
    
