# Спавн танка в ангаре.

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
from CurrentVehicle import g_currentVehicle
from skeletons.gui.shared import IItemsCache
from helpers import dependency
from gui.shared.utils.requesters import REQ_CRITERIA

itemsCache = dependency.instance(IItemsCache)
#entities = []
print itemsCache.items.getVehicles(REQ_CRITERIA.VEHICLE.LEVELS([6])).values()[100].descriptor
#entity = BigWorld.createEntity('HangarPoster', g_currentVehicle.hangarSpace.spaceID, 0, BigWorld.player().position + (-4, 1, 0), (0.0, 0.0, 0.0), {})
#entities.append(entity)
print BigWorld.entities[entities[1]].modelName
