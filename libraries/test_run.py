from  libraries.login.login import test_loginSystem
from  libraries.language.l_selenium import expectedTime
from  libraries.date.time import fiveSeconds
from  libraries.modules.vision.connectTests import test_runningAllVisionConnectTests



def test_runningAllSystemTests(): 
    test_loginSystem()
    expectedTime(fiveSeconds)
    test_runningAllVisionConnectTests()
    expectedTime(fiveSeconds)



