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

from adisp import adisp_process
from helpers import dependency
from skeletons.gui.game_control import IBrowserController

class A:
    _BROWSER_SIZE = (1014, 654)
    _MIN_BROWSER_ID = 827709
    _browserIDGen = xrange(_MIN_BROWSER_ID, _MIN_BROWSER_ID + 10000).__iter__()
    
    browserCtrl = dependency.descriptor(IBrowserController)
    
    def __init__(self):
        self.url = 'https://tanki.su/ru/daily-check-in'
        self.browser = None
        
    def onLoad(self, url):
        print '----' + url
    
    def browserCallback(self, browserID):
        self.browser = self.browserCtrl.getBrowser(browserID)
        print 'Browser hooked'
    
    @adisp_process
    def startBrowser(self):
        browserID = next(self._browserIDGen)
        if self.browserCtrl.getBrowser(browserID) is not None:
            print self.browserCtrl.getBrowser(browserID)
            print browserID
            return
        
        yield self.browserCtrl.load(url=self.url, browserID=browserID, browserSize=self._BROWSER_SIZE, isAsync=False, callback=self.browserCallback, showCreateWaiting=False, title='TEST', isModal=True)
        self.browserCallback(browserID)
        self.browser.onLoadStart += self.onLoad
        
g_a.startBrowser()
