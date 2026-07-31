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
import functools
import inspect

from debug_utils import LOG_CURRENT_EXCEPTION

from AvatarInputHandler import DynamicCameraSettings
from AvatarInputHandler.DynamicCameras.SniperCamera import SniperCamera

def override(obj, prop, getter=None, setter=None, deleter=None):
	'''Overrides attribute in object.
	Attribute should be property or callable.
	Getter, setter and deleter should be callable or None.
	:param obj: Object
	:param prop: Name of any attribute in object (can be not mangled)
	:param getter: Getter function
	:param setter: Setter function
	:param deleter: Deleter function'''

	if inspect.isclass(obj) and prop.startswith('__') and prop not in dir(obj) + dir(type(obj)):
		prop = obj.__name__ + prop
		if not prop.startswith('_'):
			prop = '_' + prop

	src = getattr(obj, prop)
	if type(src) is property and (getter or setter or deleter):
		assert getter is None or callable(getter) , 'Getter is not callable!'
		assert setter is None or callable(setter) , 'Setter is not callable!'
		assert deleter is None or callable(deleter), 'Deleter is not callable!'

		getter = functools.partial(getter, src.fget) if getter else src.fget
		setter = functools.partial(setter, src.fset) if setter else src.fset
		deleter = functools.partial(deleter, src.fdel) if deleter else src.fdel

		setattr(obj, prop, property(getter, setter, deleter))
		return getter
	elif getter:
		assert callable(src), 'Source property is not callable!'
		assert callable(getter), 'Handler is not callable!'

		getter_new = lambda *args, **kwargs: getter(src, *args, **kwargs)
		if not isinstance(src, type(BigWorld.Entity.__getattribute__)) and not inspect.ismethod(src) and inspect.isclass(obj):
			getter_new = staticmethod(getter_new)

		setattr(obj, prop, getter_new)
		return getter
	else:
		return functools.partial(override, obj, prop)

@override(SniperCamera, '__applyNoiseImpulse')
def SniperCamera__updateOscillators(base, self, noiseMagnitude):
    base(self, 0.0)

@override(SniperCamera, 'enable')
def SniperCamera_enable(base, self, targetPos, saveZoom):
    base(self, targetPos, saveZoom)
    try:
        self._SniperCamera__movementOscillator.constraints = (0, 0, 0)
    except:
        LOG_CURRENT_EXCEPTION()

@override(DynamicCameraSettings, 'getGunImpulse')
def DynamicCameraSettings_getGunImpulse(base, self, cal):
    """0.2"""
    return 0.2

@override(DynamicCameraSettings, 'getSensitivityToImpulse')
def DynamicCameraSettings_getSensitivityToImpulse(base, self, data):
    """0.3"""
    return 0.3
