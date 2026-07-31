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

import VOIP
from gui.shared import event_dispatcher

my_dbID = 72764962

def onPlayerSpeaking(dbID, state):
    if dbID != my_dbID:
        print dbID

VOIP.getVOIPManager().onPlayerSpeaking += onPlayerSpeaking

# Чтобы отобразить статистику игрока, но а ник можно получить на офф. портале.
event_dispatcher.showProfileWindow(13850499, '')
