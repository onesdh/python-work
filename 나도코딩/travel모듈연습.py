'''import travel.thailand
# import travel.thailand.ThailandPackage() 로는 사용불가
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

from travel.thailand import ThailandPackage
trip_to = ThailandPackage()
trip_to.detail()

from travel import*   #__init__모듈에 __all__을 넣었을떄만 가능
trip_to = vietnam.VietnamPackage()
trip_to.daetail()'''

from travel import*
import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))