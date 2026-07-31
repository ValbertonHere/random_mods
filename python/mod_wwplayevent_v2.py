# Использовал для воспроизведения звуковых ивентов через WoT-Transmission.

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

from gui import SystemMessages
import WWISE

event = 'ev_white_tiger_gameplay_music_start'

def wwPlaySound(event):
    WWISE.WW_eventGlobal(event)
    SystemMessages.pushMessage('Trying to play event:<br><b>' + event + '</b>', SystemMessages.SM_TYPE.Information, True)

def wwSetState(state, value):
    WWISE.WW_setState(state, value)
    SystemMessages.pushMessage('State:<br><b>' + state + '</b><br>has been switched to:<br><b>' + value + '</b>', SystemMessages.SM_TYPE.Information, True)

def wwStopMusic(event):
    WWISE.WW_eventGlobal('music_dron_endbattle_stop')
    SystemMessages.pushMessage('Trying to stop music:<br><b>' + event + '</b>', SystemMessages.SM_TYPE.Information, True)

wwPlaySound(event)
#wwSetState('STATE_viewPlayMode', 'STATE_viewPlayMode_arcade')
#wwSetState('STATE_BR_gameplay_music_phase', 'STATE_BR_gameplay_music_phase_start')
#wwSetState('STATE_BR_gameplay_music_status', 'STATE_BR_gameplay_music_status_exploring')
#wwSetState('STATE_arenastate', 'STATE_arenastate_battle')
#wwSetState('STATE_battle_phaze', 'STATE_combat')
#wwStopMusic(event)
