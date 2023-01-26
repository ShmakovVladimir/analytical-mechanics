```python
import bpy 
import numpy as np

def createScene(tringleCurveQ = 10,
                maxRadius = 3,
                startAngle = (np.pi/2,0,0),
                depth = 0.1)->list:
    radiusStep = maxRadius/tringleCurveQ
    radius = radiusStep
    meshes = []
    
    for _ in range(tringleCurveQ):
        bpy.ops.mesh.primitive_circle_add(vertices = 3,
                                          radius = radius)
        meshes.append(bpy.context.active_object)
        
        meshes[-1].rotation_euler = startAngle
        
        bpy.ops.object.convert(target = 'CURVE')
        bpy.context.object.data.bevel_depth = depth
        
        radius+=radiusStep
    
    return meshes

def createKeyFrames(totalFrames = 360, 
                    maxRotationAngleZ = 2*np.pi, 
                    maxRotationAngleY = np.pi/6 ):
    startRotationPos = (np.pi/2,0,0)
    tringles = createScene(startAngle = startRotationPos)
    for i,trMesh in enumerate(tringles):
        trMesh.rotation_euler = startRotationPos
        trMesh.keyframe_insert('rotation_euler',frame = 1)
    for i,trMesh in enumerate(tringles):
        trMesh.rotation_euler.z = maxRotationAngleZ*i/len(tringles)
        trMesh.rotation_euler.y = maxRotationAngleY*(len(tringles)-i)/len(tringles)
        trMesh.keyframe_insert('rotation_euler',frame = totalFrames//2)
    for i,trMesh in enumerate(tringles):
        trMesh.rotation_euler = startRotationPos
        trMesh.keyframe_insert('rotation_euler',frame = totalFrames)
    
createKeyFrames()
```