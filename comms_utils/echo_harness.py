from threading import Thread
from comms_utils import echo

s = Thread(target=lambda: echo.server('127.0.0.1', 65432))
c1 = Thread(target=lambda: echo.client('127.0.0.1', 65432, 'test1'))
c2 = Thread(target=lambda: echo.client('127.0.0.1', 65432, 'test2'))
c3 = Thread(target=lambda: echo.client('127.0.0.1', 65432, 'test3'))


s.start()
c1.start()
c2.start()
c3.start()
