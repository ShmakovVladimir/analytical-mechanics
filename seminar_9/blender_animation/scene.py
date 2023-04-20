import numpy as np
import bpy

bpy.ops.object.metaball_add(type='BALL', 
                            enter_editmode=False, 
                            align='WORLD', 
                            location=(0, 0, 0), 
                            scale=(1, 1, 1))
