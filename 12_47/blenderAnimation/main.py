import bpy
import numpy as np


def getSmallPos(iteration: int)->tuple:
    return (smallCylCenter[0][iteration],0,smallCylCenter[1][iteration])

def getBigPos(iteration: int)->tuple:
    return (bigCylCenter[0][iteration],0,bigCylCenter[1][iteration])
    
def createScene(cylParametrs: np.ndarray)->list:
    cylDepth,verticesQ = 1.5,200
    bigCylThikness = 0.2
    suspencionCylRadius, suspencionCylDepth = 0.06, cylDepth*2
    suspencionCylPos = (0,0,-suspencionCylRadius)
    
    bpy.ops.mesh.primitive_cylinder_add(radius = cylParametrs[0]+bigCylThikness, 
                                        depth = cylDepth, 
                                        end_fill_type = 'NOTHING',
                                        location = getBigPos(0),
                                        vertices = verticesQ)
    bigCyl = bpy.context.active_object
    bigCyl.rotation_euler.x = np.pi/2
    bpy.ops.object.modifier_add(type='SOLIDIFY')
    bpy.context.object.modifiers["Solidify"].thickness = bigCylThikness
    bpy.ops.mesh.primitive_cylinder_add(radius = cylParametrs[1], 
                                        end_fill_type='NGON', 
                                        location = getSmallPos(0),
                                        depth = cylDepth,
                                        vertices = verticesQ)
    smallCyl = bpy.context.active_object
    smallCyl.rotation_euler.x = np.pi/2
    
    bpy.ops.mesh.primitive_cylinder_add(radius = suspencionCylRadius, 
                                        depth = suspencionCylDepth, 
                                        end_fill_type = 'NGON',
                                        location = suspencionCylPos,
                                        vertices = verticesQ)
    suspencionCyl = bpy.context.active_object
    suspencionCyl.rotation_euler.x = np.pi/2
    
    bpy.ops.mesh.
    
    return [bigCyl,smallCyl]

def createKeyFrames(cylinders: list)->None:
    totalFrames = len(smallCylCenter[0])
    bigCyl,smallCyl = cylinders[0],cylinders[1]
    for i in range(totalFrames):
        bigCyl.location = getBigPos(i)
        smallCyl.location = getSmallPos(i)
        bigCyl.keyframe_insert("location",frame = i)
        smallCyl.keyframe_insert("location",frame = i)

     
    
#smallCylNpyPath = r"C:\Users\Владимир\Desktop\BOTAY!\analytical-mechanics\12_47\blenderAnimation\smallCenter.npy"
#bigCylNpyPath = r"C:\Users\Владимир\Desktop\BOTAY!\analytical-mechanics\12_47\blenderAnimation\hollowCenter.npy"
#cylParametrsPath = r"C:\Users\Владимир\Desktop\BOTAY!\analytical-mechanics\12_47\blenderAnimation\cylParametrs.npy"

smallCylNpyPath = r"C:\Users\kaQtu\OneDrive\Рабочий стол\botay\analytical-mechanics\12_47\blenderAnimation\smallCenter.npy"
bigCylNpyPath = r"C:\Users\kaQtu\OneDrive\Рабочий стол\botay\analytical-mechanics\12_47\blenderAnimation\hollowCenter.npy"
cylParametrsPath = r"C:\Users\kaQtu\OneDrive\Рабочий стол\botay\analytical-mechanics\12_47\blenderAnimation\cylParametrs.npy"

smallCylCenter = np.load(smallCylNpyPath)
bigCylCenter = np.load(bigCylNpyPath)
cylParametrs = np.load(cylParametrsPath)

createKeyFrames(createScene(cylParametrs))
    
    
                                    
                                        
                    
