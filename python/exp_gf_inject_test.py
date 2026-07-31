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

import logging
from frameworks.wulf import ViewModel
from gui.impl.pub import ViewImpl
from frameworks.wulf import ViewSettings, ViewFlags
from openwg_gameface import ModDynAccessor, gf_mod_inject
from gui.impl.lobby.crew.hangar_crew_widget import HangarCrewWidget

VAL_TEST_VIEW = 'VAL_TEST'

logger = logging.getLogger(__name__)


class ValInjectModel(ViewModel):
  
    def __init__(self, properties=1, commands=0):
        super(ValInjectModel, self).__init__(properties=properties, commands=commands)
    
    def _initialize(self):
        super(ValInjectModel, self)._initialize()
        
        self._addStringProperty('name', '')
        
        gf_mod_inject(self, VAL_TEST_VIEW, styles=[
            'coui://gui/gameface/mods/index.css'
        ], modules=[
            'coui://gui/gameface/mods/valberton/val_test/index.js'
        ])

    def setName(self, value):
        self._setString(0, value)


class ValInjectView(ViewImpl):
  
    viewLayoutID = ModDynAccessor(VAL_TEST_VIEW)
    
    def __init__(self):
        settings = ViewSettings(ValInjectView.viewLayoutID(), flags=ViewFlags.VIEW, model=ValInjectModel())
        super(ValInjectView, self).__init__(settings)
         
    @property
    def viewModel(self):
        return super(ValInjectView, self).getViewModel()
    
def HangarCrewWidget__onLoading(self, *args, **kwargs):

    resultView = AMV_onLoading_base(self, *args, **kwargs)

    self.setChildView(
        ValInjectView.viewLayoutID(),
        ValInjectView()
    )

    return resultView

AMV_onLoading_base = HangarCrewWidget._onLoading
HangarCrewWidget._onLoading = HangarCrewWidget__onLoading
