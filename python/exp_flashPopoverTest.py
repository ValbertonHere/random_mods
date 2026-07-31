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

from gui.Scaleform.framework import g_entitiesFactories, ViewSettings, GroupedViewSettings, ScopeTemplates
from frameworks.wulf import WindowLayer
from gui.Scaleform.framework.entities.abstract.AbstractPopOverView import AbstractPopOverView
from gui.shared.personality import ServicesLocator
from helpers import dependency
from skeletons.gui.impl import IGuiLoader

class OLPopOverTest(AbstractPopOverView):

    def _populate(self):
        super(OLPopOverTest, self)._populate()

    def _dispose(self):
        super(OLPopOverTest, self)._dispose()

popoverSettings = GroupedViewSettings('OLPopOverTest', OLPopOverTest, 'OLPopOverTest.swf',
    WindowLayer.WINDOW, 'OLPopOverTest', 'OLPopOverTest',
    ScopeTemplates.DEFAULT_SCOPE)

g_entitiesFactories.addSettings(popoverSettings)
