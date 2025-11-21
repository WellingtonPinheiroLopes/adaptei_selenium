from lib.date.time import fiveSeconds
from lib.language.l_selenium import expectedTime
from lib.login.login import login
from lib.modules.vision.suitsConnect import searchStatus

login()
expectedTime(fiveSeconds)
searchStatus()
