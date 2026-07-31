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

from gui.Scaleform.daapi.view.lobby.header.battle_selector_items import _BattleSelectorItems

def init_battle_types(self, items, extraItems=None):
    base(self, items, extraItems)
    for i in items:
        i.isDisabled = lambda: False
        i.isLocked = lambda: False
        i.isVisible = lambda: True

base = _BattleSelectorItems.__init__
_BattleSelectorItems.__init__ = init_battle_types
