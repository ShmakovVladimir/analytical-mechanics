import bpy 
import numpy as np

def getDiskPosition(frame: int):
    l0 = parametrs[2]
    return ((l0+q['x'][frame])*np.sin(q['theta'][frame])*np.cos(q['psi'][frame]),
            (l0+q['x'][frame])*np.sin(q['theta'][frame])*np.sin(q['psi'][frame]),
            (l0+q['x'][frame])*np.cos(q['theta'][frame]))

def getKernelEndPosition(frame:int, kernelLength: float):
    return (kernelLength*np.sin(q['theta'][frame])*np.cos(q['psi'][frame]),
            kernelLength*np.sin(q['theta'][frame])*np.sin(q['psi'][frame]),
            kernelLength*np.cos(q['theta'][frame]))

def getKernelCenterPosition(frame:int, kernelLength: float):
    return ((kernelLength/2)*np.sin(q['theta'][frame])*np.cos(q['psi'][frame]),
            (kernelLength/2)*np.sin(q['theta'][frame])*np.sin(q['psi'][frame]),
            (kernelLength/2)*np.cos(q['theta'][frame]))

def cylinder_between(startPoint: tuple ,endPoint: tuple, r):
    x1,y1,z1 = startPoint
    x2,y2,z2 = endPoint
    dx, dy, dz = x2 - x1, y2 - y1, z2 - z1 
    dist = np.sqrt(dx**2 + dy**2 + dz**2)
    bpy.ops.mesh.primitive_cylinder_add(
      radius = r, 
      depth = dist,
      location = (dx/2 + x1, dy/2 + y1, dz/2 + z1)   
    ) 
    bpy.context.object.rotation_euler[1] = np.arccos(dz/dist) 
    bpy.context.object.rotation_euler[2] = np.arctan2(dy, dx) 
    return bpy.context.active_object


def createScene() -> list:
    kernel = cylinder_between(ORIGIN,getKernelEndPosition(0,kernelLength),kernelRadius)
    bpy.ops.mesh.primitive_cylinder_add(radius = diskRadius, 
                                        depth = diskDepth,   
                                        location = getDiskPosition(0), 
                                        vertices = verticesQ)
    disk = bpy.context.active_object

    return [kernel,disk]

def createKeyFrames(obj: list):
    kernel,disk = obj[0], obj[1]

    

qPath = r'C:\Users\kaQtu\OneDrive\Рабочий стол\botay\analytical-mechanics\12_59\q.npz'
paramPath = r'C:\Users\kaQtu\OneDrive\Рабочий стол\botay\analytical-mechanics\12_59\parametrs.npy'

q = np.load(qPath)
parametrs = np.load(paramPath)

verticesQ, diskRadius, diskDepth = 200, parametrs[0], 0.2
l0, kernelLength,kernelRadius = parametrs[2], 25, 0.4
ORIGIN = (0,0,0)

createKeyFrames(createScene())
