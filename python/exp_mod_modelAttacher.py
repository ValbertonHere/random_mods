# [Эксперимент] Попытка в прикрепление эффектов к модели танка.

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

# Импортры.
import BigWorld
from gui import InputHandler
from Avatar import PlayerAvatar
from Account import PlayerAccount
from constants import ARENA_PERIOD
from PlayerEvents import g_playerEvents
from CurrentVehicle import g_currentVehicle
from helpers.statistics import StatisticsCollector
from helpers.statistics import HANGAR_LOADING_STATE
from vehicle_systems.tankStructure import TankPartNames
from gui.shared.utils.key_mapping import getBigworldNameFromKey

# Определение переменных.
playerAllyID_list = []
vehName = 'germany:G98_Waffentrager_E100'

# Хук полной загрузки танка в ангаре.
h_noteHangarLoadingState = StatisticsCollector.noteHangarLoadingState

def n_noteHangarLoadingState(self, state, *args, **kwargs):
    h_noteHangarLoadingState(self, state, *args, **kwargs)
    if state == HANGAR_LOADING_STATE.FINISH_LOADING_VEHICLE:
        if g_currentVehicle.item.name == vehName:
            bte110_addeff(0)

StatisticsCollector.noteHangarLoadingState = n_noteHangarLoadingState


# Добавление эффектов на другие танки после начала боя.
def otherPlayersVehEffAdd(period, *args):
    if period == ARENA_PERIOD.BATTLE:
        if BigWorld.player().vehicleTypeDescriptor.name == vehName: 
            effectDetach() # Отключение эффектов у игрока.
        
        playerAllyID_list = []
        playerTeam = BigWorld.player().team # Определяем команду игрока.
        
        for pl in BigWorld.player().arena.vehicles.values():
            if pl['vehicleType'].name == vehName:
                if pl['team'] == playerTeam and int(pl['avatarSessionID']) != BigWorld.player().playerVehicleID:
                    playerAllyID_list.append(pl['avatarSessionID'])
                    
        for playerAllyID in playerAllyID_list:
            bte110_addeff(playerAllyID) # Добавляем эффекты другим танкам.
        
        playerVehicleEffAdd() # Заново добавляем эффекты игроку для управления.


# Реаттач эффектов в случае отключения.
def onhandleKeyEvent(event):
    key = getBigworldNameFromKey(event.key)
    if key == 'KEY_R':
        effectsReload()


# Добавление эффекта для игрока при загрузке арены.
def playerVehicleEffAdd():
    if BigWorld.player().vehicleTypeDescriptor.name == vehName:
        bte110_addeff(BigWorld.player().playerVehicleID)


# Добавление эффекта.
def bte110_addeff(playerID):
    global gun
    global gun_blendbone
    global hull
    global turret
    global gun_model
    global gun_model2
    global gun_model3
    global hull_model
    global turret_model
    global shield_ind_model
    
    if isinstance(BigWorld.player(), PlayerAvatar):
        vehModel = BigWorld.entity(int(playerID)).appearance
    elif isinstance(BigWorld.player(), PlayerAccount):
        vehModel = g_currentVehicle.hangarSpace.getVehicleEntityAppearance()
    
    gun = vehModel.compoundModel.node('Gun')
    gun_blendbone = vehModel.compoundModel.node('Gun_BlendBone')
    hull = vehModel.compoundModel.node(TankPartNames.HULL)
    turret = vehModel.compoundModel.node(TankPartNames.TURRET)
    gun_model = BigWorld.Model('particles/Environment/event_white_tiger/enemies/Waffentrager_E100_idle/Waffentrager_E100_idle_gun.model')
    gun_model2 = BigWorld.Model('particles/Environment/event_white_tiger/enemies/Waffentrager_E100_shoot/wt_Shoot_lighting_idel.model')
    gun_model3 = BigWorld.Model('particles/Environment/event_white_tiger/enemies/Waffentrager_E100_shoot/wt_Shoot.model')
    hull_model = BigWorld.Model('particles/Environment/event_white_tiger/enemies/Waffentrager_E100_idle/Waffentrager_E100_idle_hull.model')
    turret_model = BigWorld.Model('particles/Environment/event_white_tiger/enemies/Waffentrager_E100_idle/Waffentrager_E100_idle_turret.model')
    shield_ind_model = BigWorld.Model('particles/Environment/event_white_tiger/enemies/Waffentrager_E100_idle/Waffentrager_E100_shield_indicator.model')
    gun.attach(gun_model2)
    gun.attach(gun_model3)
    gun_blendbone.attach(gun_model)
    hull.attach(hull_model)
    turret.attach(turret_model)
    turret.attach(shield_ind_model)


# Реаттач.
def effectsReload():
    gun_blendbone.detach(gun_model)
    gun.detach(gun_model2)
    gun.detach(gun_model3)
    hull.detach(hull_model)
    turret.detach(turret_model)
    turret.detach(shield_ind_model)
    gun_blendbone.attach(gun_model)
    gun.attach(gun_model2)
    gun.attach(gun_model3)
    hull.attach(hull_model)
    turret.attach(turret_model)
    turret.attach(shield_ind_model)


# Отключение.
def effectDetach():
    gun_blendbone.detach(gun_model)
    gun.detach(gun_model2)
    gun.detach(gun_model3)
    hull.detach(hull_model)
    turret.detach(turret_model)
    turret.detach(shield_ind_model)


g_playerEvents.onArenaPeriodChange += otherPlayersVehEffAdd # Привязка к смене момента боя.
g_playerEvents.onAvatarReady += playerVehicleEffAdd # Привязка к загрузке арены.
InputHandler.g_instance.onKeyDown += onhandleKeyEvent # Привязка нажатия кнопки.

print '[VLBRTN] [TEST] Blitztrager E 110 Model Effects tool.'
