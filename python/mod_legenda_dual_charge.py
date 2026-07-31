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
from PlayerEvents import g_playerEvents
from constants import DUALGUN_CHARGER_STATUS
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE

def __addEvent(name):
    event = {
        'name': name,
        'fxEvent': '',
        'infChance': 100,
        'predelay': 0,
        'priority': 1001,
        'lifetime': 3,
        'infEvent': 'vo_%s' % name,
        'queue': '1',
        'chance': '100',
        'interrupt': '0',
        'cooldownEvent': '0',
        'queueClearAtStart': '1'
    }
    BigWorld.player().soundNotifications._IngameSoundNotifications__events[event['name']] = event

def afterArenaLoad():
    __addEvent('legenda_charge_start')
    __addEvent('legenda_charge_shot')
    
    BigWorld.player().sessionProvider.shared.vehicleState.onVehicleStateUpdated += onVehicleStateUpdated

def onVehicleStateUpdated(stateID, value):
    if stateID == VEHICLE_VIEW_STATE.DUAL_GUN_CHARGER:
        dualState, time = value
        baseTime, timeLeft = time
        if dualState == DUALGUN_CHARGER_STATUS.PREPARING:
            if timeLeft > 0:
                timeToStart = timeLeft - 2.5
                BigWorld.callback(timeToStart, lambda: BigWorld.player().soundNotifications.play('legenda_charge_start'))
        elif dualState == DUALGUN_CHARGER_STATUS.APPLIED:
            BigWorld.player().soundNotifications.play('legenda_charge_shot')

g_playerEvents.onAvatarReady += afterArenaLoad
