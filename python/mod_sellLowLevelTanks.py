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
from gui import InputHandler, SystemMessages
from gui.shared import event_dispatcher
from gui.shared.gui_items import GUI_ITEM_TYPE
from gui.shared.gui_items.processors import plugins
from gui.shared.utils.key_mapping import getBigworldNameFromKey
from helpers import isPlayerAccount
from items import vehicles

def onCacheRecieved(reqID, data):
    for k, v in data[GUI_ITEM_TYPE.VEHICLE]['compDescr'].items():
        veh = vehicles.VehicleDescr(compactDescr=v)
        if not plugins.VehicleSellsLeftValidator(g_currentVehicle.item).validate().success:
            SystemMessages.pushMessage('Limit', priority=True)
            return
        if veh.level in (2, 3, 4) and not veh.type.isPremium:
            event_dispatcher.showVehicleSellDialog(k)
            return

def onhandleKeyEvent(event):
    key = getBigworldNameFromKey(event.key)
    if key == 'KEY_S' and isPlayerAccount():
        BigWorld.player().inventory.getCache(onCacheRecieved)

InputHandler.g_instance.onKeyDown += onhandleKeyEvent
