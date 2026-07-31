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
from gui.shared.gui_items.items_actions import factory
from functools import partial

tList = []

def dissmisAction(tankmanList):
    factory.doAction(factory.DISMISS_TANKMAN, tankmanList)

for tankmanObj in g_currentVehicle.itemsCache.items.getTankmen().values():
    if not tankmanObj.isInTank and tankmanObj.earnedSkillsCount == 0:
        tList.append(tankmanObj)
    else: continue

dissmisAction(tList)
