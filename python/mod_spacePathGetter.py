# Получение названия и пути к карте через хук.

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

import game

hookedOnGeometryMapped = game.onGeometryMapped

def hookOnGeometryMapped(spaceID, path):
    hookedOnGeometryMapped(spaceID, path)
    print 'mapName: %s, mapPath: %s' % (path.split('/')[-1], path)

game.onGeometryMapped = hookOnGeometryMapped
