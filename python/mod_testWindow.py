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

from frameworks.wulf import WindowLayer
from gui import InputHandler
from gui.Scaleform.framework import g_entitiesFactories, ViewSettings, ScopeTemplates
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams
from helpers import dependency
from skeletons.gui.app_loader import IAppLoader
from gui.shared.utils.key_mapping import getBigworldNameFromKey

class TestWindow(AbstractWindowView):

    def __init__(self):
        super(TestWindow, self).__init__()

    def _populate(self):
        super(TestWindow, self)._populate()

    def onWindowClose(self):
        self.destroy()

g_entitiesFactories.addSettings(ViewSettings('TestWindow', TestWindow, 'TestWindowUI.swf', WindowLayer.WINDOW, None, ScopeTemplates.VIEW_SCOPE))

def onhandleKeyEvent(event):
    key = getBigworldNameFromKey(event.key)
    if key == 'KEY_F9':
        appLoader = dependency.instance(IAppLoader)
        app = appLoader.getApp()
        app.loadView(SFViewLoadParams('TestWindow'))

InputHandler.g_instance.onKeyDown += onhandleKeyEvent
