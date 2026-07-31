# Для спавна моделей для видео.

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

import BigWorld, Keys, ResMgr
from gui import InputHandler

MODELS = []
for i in ResMgr.readDirectory('content/pb'):
    if i.endswith('.model'):
        MODELS.append('content/pb/' + i)
models_count = 0

def addModel():
    global models_count

    model = BigWorld.Model(MODELS[models_count])
    model.position = BigWorld.camera().position
    BigWorld.addModel(model)
    models_count += 1 if models_count < len(MODELS) - 1 else - len(MODELS)

def delModels():
    for i in BigWorld.models():
        BigWorld.delModel(i)

def onKeyDown(event):
    if event.isKeyDown() and BigWorld.isKeyDown(Keys.KEY_LCONTROL) and BigWorld.isKeyDown(Keys.KEY_NUMPAD9):
        delModels()
        addModel()
    elif event.isKeyDown() and BigWorld.isKeyDown(Keys.KEY_LCONTROL) and BigWorld.isKeyDown(Keys.KEY_UPARROW):
        BigWorld.models()[0].rotate(0.1, (1, 0, 0))
    elif event.isKeyDown() and BigWorld.isKeyDown(Keys.KEY_LCONTROL) and BigWorld.isKeyDown(Keys.KEY_DOWNARROW):
        BigWorld.models()[0].rotate(0.1, (-1, 0, 0))
    elif event.isKeyDown() and BigWorld.isKeyDown(Keys.KEY_LCONTROL) and BigWorld.isKeyDown(Keys.KEY_LEFTARROW):
        BigWorld.models()[0].rotate(0.1, (0, 1, 0))
    elif event.isKeyDown() and BigWorld.isKeyDown(Keys.KEY_LCONTROL) and BigWorld.isKeyDown(Keys.KEY_RIGHTARROW):
        BigWorld.models()[0].rotate(0.1, (0, -1, 0))

InputHandler.g_instance.onKeyDown += onKeyDown
