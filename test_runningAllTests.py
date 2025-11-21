from  lib.login.login import login
from  lib.language.l_selenium import expectedTime
from  lib.date.time import fiveSeconds
from  lib.modules.vision.testsConnect import test_runningAllVisionConnectTests


def test_runningAllSystemTests(): 
    login()
    expectedTime(fiveSeconds)
    test_runningAllVisionConnectTests()
    expectedTime(fiveSeconds)


test_runningAllSystemTests()
