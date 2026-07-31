# Эксперимент: Добавление твоего префаб-компонента - подсказка и клик.

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

import CGF
import ResMgr
from cgf_components.hover_component import IsHoveredComponent
from cgf_script.component_meta_class import registerComponent, ComponentProperty, CGFMetaTypes
from cgf_script.managers_registrator import onAddedQuery, onRemovedQuery, registerManager, Rule, registerRule
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.shared.events import LobbySimpleEvent
from gui.shared import g_eventBus
from gui.shared.tooltips import contexts, ToolTipBaseData
from gui.shared.tooltips.builders import DataBuilder
from skeletons.gui.app_loader import IAppLoader
from helpers import dependency
from frameworks.wulf import WindowLayer
from gui.shared.personality import ServicesLocator
from skeletons.gui.app_loader import GuiGlobalSpaceID

appLoader = dependency.instance(IAppLoader)

@registerComponent
class OmniTooltipComponent(object):
    domain = CGF.DomainOption.DomainClient
    editorTitle = 'OmniTooltip'
    category = 'Common'
    tooltip = ComponentProperty(type=CGFMetaTypes.STRING, editorName='selectionId')


class OmniTooltipManager(CGF.ComponentManager):

    @onAddedQuery(IsHoveredComponent, OmniTooltipComponent)
    def onTooltipAdded(self, _, omniTooltipComponent):
        lobby = appLoader.getDefLobbyApp()
        if lobby and lobby.containerManager:
            view = lobby.containerManager.getView(WindowLayer.SUB_VIEW)

        callTooltip = getattr(view, 'as_show3DSceneTooltipS', None)
        if callTooltip is not None:
            view.as_show3DSceneTooltipS('OmniEnvironment', [omniTooltipComponent.tooltip])

    @onRemovedQuery(IsHoveredComponent, OmniTooltipComponent)
    def onTooltipRemoved(self, *_):
        g_eventBus.handleEvent(LobbySimpleEvent(LobbySimpleEvent.ENTITY_TOOLTIP_HIDE))


@registerRule
class OmniSelectionRule(Rule):
    category = 'Hangar rules'
    domain = CGF.DomainOption.DomainClient

    @registerManager(OmniTooltipManager)
    def reg1(self):
        try:
            appLoader.getDefLobbyApp()._toolTip._builders.addBuilder(DataBuilder('OmniEnvironment', TOOLTIPS_CONSTANTS.ENVIRONMENT_UI, OmniEnvironmentTooltipData(contexts.HangarContext())))
        except:
            print 'No need to add OmniEnvironment tooltip builder again.'
        return


class OmniEnvironmentTooltipData(ToolTipBaseData):

    _ENV_TOOLTIPS_PATH = '#test_tooltip:%s'
    _ENV_IMAGES_PATH = '../maps/icons/omniEnvironmentTooltips/%s.png'
    _ENV_IMAGES_PATH_FOR_CHECK = 'gui/maps/icons/omniEnvironmentTooltips/%s.png'

    def __init__(self, context):
        super(OmniEnvironmentTooltipData, self).__init__(context, None)
        return

    def getDisplayableData(self, tooltipId):
        title = self._ENV_TOOLTIPS_PATH % ('%s/header' % tooltipId)
        desc = self._ENV_TOOLTIPS_PATH % ('%s/body' % tooltipId)
        icon = None
        if ResMgr.isFile(self._ENV_IMAGES_PATH_FOR_CHECK % tooltipId):
            icon = self._ENV_IMAGES_PATH % tooltipId
        return {'title': title, 
           'text': desc,
           'icon': icon}

