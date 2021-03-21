import BigWorld, game, Keys, BattleReplay
from helpers import dependency
from skeletons.gameplay import IGameplayLogic


def overrideIn(cls):
    def _overrideIn(func):
        old = getattr(cls, func.__name__)

        def wrapper(*args, **kwargs):
            return func(old, *args, **kwargs)

        setattr(cls, func.__name__, wrapper)
        return wrapper
    return _overrideIn


gameplayLogicObj = dependency.instance(IGameplayLogic)


@overrideIn(game)
def handleKeyEvent(func, event):
    if not BattleReplay.isPlaying() and event.isKeyDown() and event.isCtrlDown():
        if event.key == Keys.KEY_K:
            gameplayLogicObj.goToLoginByDisconnectRQ()
            
    return func(event)
