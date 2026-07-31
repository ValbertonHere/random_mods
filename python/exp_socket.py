# Общение клиента и сервера на Web-Socket.

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

import socket
from time import sleep
from gui.Scaleform.daapi.view.battle.shared.damage_log_panel import DamageLogPanel
from OpenModsCore import overrideMethod
import BigWorld
from PlayerEvents import g_playerEvents

@overrideMethod(DamageLogPanel, '_updateTotalDamageValue')
def test(base, self, value):
    base(self, value)
    send_message('Total damage in battle: ' + value)

def onBattleResultsReceived(_, data):
    send_message('-----------BATTLE ENDED------------')
    send_message('Total damage after battle: %s' % data['personal'].items()[0][1]['damageDealt'])

def client_init():
    client = socket.socket()
    hostname = '26.174.146.138'
    port = 12345
    client.connect((hostname, port))
    return client

def send_message(msg='No message found.'):
    client = client_init()
    sleep(0.01)
    client.send(msg.encode())
    data = client.recv(1024)
    print "Server sent: %s" % data.decode()
    client.close()

send_message('init')

g_playerEvents.onBattleResultsReceived += onBattleResultsReceived
