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
from gui.resource_well.resource import processLoadingResources, convertResourcesToServerLayout
from gui.shared.personality import ServicesLocator
from threading import Thread
from time import sleep
from gui import SystemMessages
from datetime import datetime
from helpers import time_utils
from gui import InputHandler
from gui.shared.utils.key_mapping import getBigworldNameFromKey

need_time = 1755795585
i = 0

def n(code, errStr):
    print code, errStr

def worker():
    global i
    
    while ServicesLocator.itemsCache.items.stats.actualFreeXP > 612000:
        SystemMessages.pushMessage("Putting resources... Try: %s" % i, priority=True)
        compRes = processLoadingResources({'freeXP': 612000.0, 'crystal': 7600.0, 'premium_plus': 300.0})
        BigWorld.player().resourceWell.putResources(convertResourcesToServerLayout(compRes), 'top', n)
        sleep(1.1)
        i += 1

def timerStart():
    timeString = datetime.utcfromtimestamp(need_time).strftime('%Y-%m-%d %H:%M:%S')
    SystemMessages.pushMessage('Waiting until %s.' % timeString, priority=True)
    print '------------------------ START WAITING UNTIL %s' % timeString
    while time_utils.getServerUTCTime() < need_time:
        sleep(0.05)
    else:
        print 'Just in Time'
        SystemMessages.pushMessage("It's time to put resources!", priority=True)
        thread = Thread(target=worker)
        thread.start()

def startTimer(event):
    key = getBigworldNameFromKey(event.key)
    if key == 'KEY_F9':
        threadTimer = Thread(target=timerStart)
        threadTimer.start()

InputHandler.g_instance.onKeyDown += startTimer
