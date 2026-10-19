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

from gui import SystemMessages
from survey.gui.game_control.SurveyChannelHandler import SurveyChannelHandler

def onSurveySuppressed(self, ctx):
    _, message = ctx
    arenaUniqueID = message.data.get('arenaUniqueID', 0)

    SystemMessages.pushMessage('Предложение пройти опрос после боя, присланное сервером, было автоматически отклонено.', SystemMessages.SM_TYPE.InformationHeader, True, {'header': 'Подавление опроса боя'})
    BigWorld.player().AccountSurveyComponent.sendSurveyResult(BigWorld.player().databaseID, arenaUniqueID, -3)

SurveyChannelHandler._showAward = onSurveySuppressed
