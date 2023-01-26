import bpy
import numpy as np


def getSmallPos(iteration: int)->tuple:
    return (smallCylCenter[0][iteration],0,smallCylCenter[1][iteration])

def getBigPos(iteration: int)->tuple:
    return (bigCylCenter[0][iteration],0,bigCylCenter[1][iteration])
    
def createScene(cylParametrs: np.ndarray)->list:
    cylDepth,verticesQ = 1.5,200
    bpy.ops.mesh.primitive_cylinder_add(radius = cylParametrs[0], 
                                        depth = cylDepth, 
                                        end_fill_type = 'NOTHING',
                                        location = getBigPos(0),
                                        vertices = verticesQ)
    bigCyl = bpy.context.active_object
    bigCyl.rotation_euler.x = np.pi/2
    
    bpy.ops.mesh.primitive_cylinder_add(radius = cylParametrs[1], 
                                        end_fill_type='NGON', 
                                        location = getSmallPos(0),
                                        depth = cylDepth,
                                        vertices = verticesQ)
    smallCyl = bpy.context.active_object
    smallCyl.rotation_euler.x = np.pi/2
    return [bigCyl,smallCyl]

def createKeyFrames(cylinders: list)->None:
    totalFrames = len(smallCylCenter[0])
    bigCyl,smallCyl = cylinders[0],cylinders[1]
    for i in range(totalFrames):
        bigCyl.location = getBigPos(i)
        smallCyl.location = getSmallPos(i)
        bigCyl.keyframe_insert("location",frame = i)
        smallCyl.keyframe_insert("location",frame = i)

     
    

smallCylCenter = np.load(r"C:\Users\Владимир\Desktop\BOTAY!\analytical-mechanics\12_47\blenderAnimation\smallCenter.npy")
bigCylCenter = np.load(r"C:\Users\Владимир\Desktop\BOTAY!\analytical-mechanics\12_47\blenderAnimation\hollowCenter.npy")
cylParametrs = np.load(r"C:\Users\Владимир\Desktop\BOTAY!\analytical-mechanics\12_47\blenderAnimation\cylParametrs.npy")

createKeyFrames(createScene(cylParametrs))
    
    
                                    
                                        
                    
