# Меню настроек.

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

from OpenModsCore import SimpleConfigInterface

class OMCMenu(SimpleConfigInterface):

    def __init__(self):
        self.authors = ['omnilab', 'nick', 'prev']
        self.builds = ['current', 'prev', 'first']
        super(OMCMenu, self).__init__()
    
    def init(self):
        self.ID = 'WTSM_Menu'
        self.version = '0.0a'
        self.author = 'by Valberton'
        self.modsGroup = 'WTSM'
        self.modSettingsID = 'WTSM_Menu'
        self.data = {'enabled': True, 'author': 0, 'build': 0, 'control': False}
        self.i18n = {'name': 'Тестовые настройки мода', 
                     'UI_setting_author_text': 'Издатели мода',
                     'UI_setting_author_omnilab': 'OmniLab Research & Development',
                     'UI_setting_author_nick': 'Valberton',
                     'UI_setting_author_prev': 'OmniLight Software',
                     'UI_setting_build_text': 'Билды мода',
                     'UI_setting_build_current': '0124/3',
                     'UI_setting_build_prev': '1223/6',
                     'UI_setting_build_first': '0000/0',
                     'UI_setting_control_text': 'Чекбокс'}
        super(OMCMenu, self).init()
    
    def createTemplate(self):
        return None

    def onButtonPress(self, vName, value):
        print vName, value
    
    def onMSADestroy(self):
        self.readData()

g_config = OMCMenu()
