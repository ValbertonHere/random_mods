# Тест генерирования звука на определенных координатах на карте. Работает.

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
import SoundGroups

player = BigWorld.player()
position = player.getOwnVehiclePosition()

print 'mod_loaded'
print '------------'
print player.name
print position
print SoundGroups.g_instance.playSound2D
print SoundGroups.g_instance.playSoundPos('expl_ammo_NPC', (105.0, -5, 100.0))
print '------------'
