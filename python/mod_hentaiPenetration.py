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

import BigWorld, SoundGroups
from PlayerEvents import g_playerEvents

def onHealthChanged(attackedID, *args, **kwargs):
    if attackedID == BigWorld.player().playerVehicleID:
        SoundGroups.g_instance.playSound2D('hentai_sound')

def onAvatarReady():
    BigWorld.player().arena.onVehicleHealthChanged += onHealthChanged

g_playerEvents.onAvatarReady += onAvatarReady

print '[OMNILAB: HENTAI ROFL] INIT! Copyright (C) 2024 OmniLab R&D.'
