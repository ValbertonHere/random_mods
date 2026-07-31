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

from CurrentVehicle import g_currentVehicle
from debug_utils import LOG_NOTE
from gui.Scaleform.daapi.view.lobby.vehicle_sell_dialog import VehicleSellDialog
from gui.shared.gui_items.processors import plugins

def VehicleSellDialog_as_visibleControlBlockS(self, value):
    base(self, not plugins.VehicleSellsLeftValidator(g_currentVehicle.item).validate().success)

VehicleSellDialog._VehicleSellDialog__useCtrlQuestion = False
base = VehicleSellDialog.as_visibleControlBlockS
VehicleSellDialog.as_visibleControlBlockS = VehicleSellDialog_as_visibleControlBlockS

LOG_NOTE("Valberton's quick vehicle sell tweak - init. Copyright (C) 2025 OmniLab R&D.")
