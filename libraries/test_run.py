from libraries.date.time import fiveSeconds
from libraries.language.l_selenium import expectedTime
from libraries.login.login import loginSystem
from libraries.modules.vision.suitsConnect import *

loginSystem()
expectedTime(fiveSeconds)
test_searchActiveStatus()
# expectedTime(fiveSeconds)
# closeSystem()
