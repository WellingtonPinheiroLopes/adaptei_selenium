from libraries.date.time import fiveSeconds
from libraries.language.l_selenium import closeSystem, expectedTime
from libraries.login.login import loginSystem

# from libraries.modules.vision.suitsConnect import *
from libraries.modules.vision.suitsPlans import *

loginSystem()
expectedTime(fiveSeconds)
# test_searchActiveStatus()
test_CreatingMonthlyPlansAskingTheClientVisibleYes()
expectedTime(fiveSeconds)
closeSystem()
