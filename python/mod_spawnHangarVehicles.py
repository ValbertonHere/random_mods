"""
Copyright (C) 2026 Roman "Valberton" Levchenko

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.
"""

import BigWorld
from helpers import dependency
from skeletons.gui.shared.utils import IHangarSpace
from items import vehicles

hangarSpace = dependency.instance(IHangarSpace)

def spawn():
    if hangarSpace.spacePath == 'spaces/hangar_v2':
        entities = []
        entities.append(BigWorld.createEntity('ClientSelectableCameraVehicle', hangarSpace.spaceID, 0, (6, 0, -38), (0.0, 0.0, 0.0), {}))
        entities.append(BigWorld.createEntity('ClientSelectableCameraVehicle', hangarSpace.spaceID, 0, (2, 0, -38), (0.0, 0.0, 0.0), {}))
        entities.append(BigWorld.createEntity('ClientSelectableCameraVehicle', hangarSpace.spaceID, 0, (-2, 0, -38), (0.0, 0.0, 0.0), {}))
        entities.append(BigWorld.createEntity('ClientSelectableCameraVehicle', hangarSpace.spaceID, 0, (-6, 0, -38), (0.0, 0.0, 0.0), {}))
        
        BigWorld.entities[entities[0]].recreateVehicle(typeDescriptor=vehicles.VehicleDescr(typeName='germany:G121_Grille_15_L63'))
        BigWorld.entities[entities[1]].recreateVehicle(typeDescriptor=vehicles.VehicleDescr(typeName='uk:GB83_FV4005'))
        BigWorld.entities[entities[2]].recreateVehicle(typeDescriptor=vehicles.VehicleDescr(typeName='germany:G178_Sturmtiger_V1'))
        BigWorld.entities[entities[3]].recreateVehicle(typeDescriptor=vehicles.VehicleDescr(typeName='france:F129_Schneider_120_AC_Gendarme'))
        
        lights = []
        for _ in xrange(0, 4):
            light = BigWorld.PySpotLight()
            light.castShadows = True
            light.coneAngle = 1
            light.outerRadius = 10
            lights.append(light)
        
        lights[0].direction = (0, -1, -.2)
        lights[0].position = (2, 6, -36)
        
        lights[1].direction = (0, -1, 0)
        lights[1].position = (6, 5, -38)
        
        lights[2].direction = (0, -1, 0)
        lights[2].position = (-2, 5, -37)
        
        lights[3].direction = (0, -1, 0)
        lights[3].position = (-6, 6, -38)

hangarSpace.onSpaceCreate += spawn
