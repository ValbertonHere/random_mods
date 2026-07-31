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

import BigWorld, Keys

from gui import InputHandler
from skeletons.gui.battle_session import IBattleSessionProvider
from helpers import dependency, isPlayerAvatar
from debug_utils import LOG_NOTE

class BattleLeaverWorker():
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self):
        InputHandler.g_instance.onKeyDown += self._doLeaveBattle
        LOG_NOTE("Valberton's battle leaver - Leave from battle via hotkeys - Copyright (C) 2025 OmniLab R&D.")

    def _doLeaveBattle(self, event):
        if event.isKeyDown() and BigWorld.isKeyDown(Keys.KEY_NUMPAD5) and isPlayerAvatar():
            LOG_NOTE('Leaving from battle...')
            self.sessionProvider.exit()

g_battleLeaverWorker = BattleLeaverWorker()
