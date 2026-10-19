import BigWorld, Math, math_utils, logging
from helpers.CallbackDelayer import CallbackDelayer
from PlayerEvents import g_playerEvents

ANIM_RATE = 0.001
ANIM_STEP = 0.025
ANIM_LIMITS = (1.0, 0.5)

logger = logging.getLogger(__name__)

class ToyotaYarisTanks(CallbackDelayer):
    def __init__(self):
        CallbackDelayer.__init__(self)
        self._player = None
        self._arena = None
        self._currentScale = 1.0
        self._isSqueezing = True

        g_playerEvents.onAvatarBecomePlayer += self._onBattleJoined
        g_playerEvents.onAvatarReady += self._start
        g_playerEvents.onAvatarBecomeNonPlayer += self._stop
        logger.info('ToyotaYarisTanks::__init__')

    def _onBattleJoined(self):
        self._player = BigWorld.player()
        self._arena = self._player.arena
        logger.info('ToyotaYarisTanks::onBattleJoined')

    def _start(self):
        self.delayCallback(ANIM_RATE, self._tick)
        logger.info('ToyotaYarisTanks::start')

    def _stop(self):
        self.stopCallback(self._tick)
        logger.info('ToyotaYarisTanks::stop')

    def _tick(self):
        self._currentScale = self._currentScale - ANIM_STEP if self._isSqueezing else self._currentScale + ANIM_STEP

        if self._currentScale > ANIM_LIMITS[0]:
            self._currentScale = ANIM_LIMITS[0]
            self._isSqueezing = True
        elif self._currentScale < ANIM_LIMITS[1]:
            self._currentScale = ANIM_LIMITS[1]
            self._isSqueezing = False

        for vehicleID in self._arena.vehicles.keys():
            vehicle = BigWorld.entity(vehicleID)
            if vehicle is not None and vehicle.model is not None:
                vehicle.model.matrix = self._createScaledTankMatrix(vehicle, self._checkPlayerTarget(vehicleID))
        
        return ANIM_RATE

    def _createScaledTankMatrix(self, vehicle, needToReturn=False):
        return math_utils.createSRTMatrix(Math.Vector3(1.0, self._currentScale if not needToReturn else 1.0, 1.0), Math.Vector3(vehicle.yaw, vehicle.pitch, vehicle.roll), vehicle.position)
    
    def _checkPlayerTarget(self, vehicleID):
        target = BigWorld.target()
        if target is not None:
            return target.id == vehicleID
        
        return False


    def _returnToMonke(self):
        for vehicleID in self._arena.vehicles.keys():
            vehicle = BigWorld.entity(vehicleID)
            if vehicle is not None:
                vehicle.model.matrix = self._createScaledTankMatrix(vehicle, True)

g_toyotaYarisTanks = ToyotaYarisTanks()