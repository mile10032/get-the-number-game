import sys
import random
def typecheck():
    while True:
        try:
            param = int(input())
            return param
        except ValueError:
            print("数字を入れてください。")
def generateRandom(minNum,maxNum):
    return random.randint(minNum,maxNum)

print("2つの数字を当ててください。ただし、１回目より２回目の数字は大きくないといけません。")
print("最初の数字を入力してください。")
randomNumber = generateRandom(1,10)
randomNumber2 = generateRandom(randomNumber+1,44)
while True:
    param1 = typecheck()
    while True:
        print("２回目の数字を入れてください、ただし、１回目より大きな数字で。")
        param2 = typecheck()
        if param2 > param1:
            break
        else:
            print("２回目の数字は１回目より大きくないといけません。")
    if param1 == randomNumber & param2 == randomNumber2:
        break
    else:
        print("やりなおし。")
    


