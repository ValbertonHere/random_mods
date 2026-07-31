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

from vehicle_systems import model_assembler

engineEventsOverrides = {'eng_V2K': 'eng_v55', 'eng_V2_34': 'eng_v55', 'eng_Continental_R975_C1': 'eng_Continental_R975'}

def returnToMonke(isPlayer, appearance):
    typeDescriptor = appearance.typeDescriptor
    sounds = list(typeDescriptor.engine.sounds._WWTripleSoundConfig__eventNames)
    for idx, event in enumerate(sounds):
        for oldEvent in engineEventsOverrides.keys():
            if event.find(oldEvent) != -1:
                sounds[idx] = event.replace(oldEvent, engineEventsOverrides[oldEvent])
                break
    
    typeDescriptor.engine.sounds._WWTripleSoundConfig__eventNames = tuple(sounds)
    base(isPlayer, appearance)

base = model_assembler.assembleVehicleAudition
model_assembler.assembleVehicleAudition = returnToMonke
