import random
from tqdm import tqdm
import time
#문 3개 변수 생성
door1 = False
door2 = False
door3 = False
doored1 = False
doored2 = False
doored3 = False
Success = 0
Failed = 0
repeatnum = int(input("반복횟수:"))
for i in range(1,repeatnum+1):
    running = True
    door1 = False
    door2 = False
    door3 = False
    doored1 = False
    doored2 = False
    doored3 = False
    dnum = random.randrange(1,4)
    if dnum == 1:
        door1 = True
    if dnum == 2:
        door2 = True
    if dnum == 3:
        door3 = True
    dnum2 = random.randrange(1,4)
    if dnum2 == 1:
        doored1 = True
    if dnum2 == 2:
        doored2 = True
    if dnum2 == 3:
        doored3 = True
#결과
    if doored1 == True:
        if door1 == True:
            Failed = Failed + 1
        if door2 or door3:
            Success = Success + 1
    if doored2 == True:
        if door2 == True:
            Failed = Failed + 1
        if door1 or door3 == True:
            Success = Success + 1
    if doored3 == True:
        if door3 == True:
            Failed = Failed + 1
        if door1 or door2 == True:
            Success = Success + 1
print("성공:",Success,"실패:",Failed)
#분수, 백분율 계산 코드 쓰기