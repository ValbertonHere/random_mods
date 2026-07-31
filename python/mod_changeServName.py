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

from predefined_hosts import g_preDefinedHosts

for idx, host in enumerate(g_preDefinedHosts._hosts):
    if 'WOT' not in host.name or 'W.o.T.' not in host.name:
        if 'RU' in host.name:
            g_preDefinedHosts._hosts[idx] = host._replace(name='WOT ' + host.name, shortName='WOT ' + host.name)
        elif 'PT' in host.name:
            g_preDefinedHosts._hosts[idx] = host._replace(name='W.o.T. Common Test', shortName='W.o.T. Common Test')
        elif 'ST' in host.name:
            g_preDefinedHosts._hosts[idx] = host._replace(name='W.o.T. Super Test' + host.name.split('ST')[-1], shortName='W.o.T. Super Test' + host.name.split('ST')[-1])
