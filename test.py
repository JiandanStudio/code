print('-----small game ----------')
temp = input("猜猜你心里想的什么数字：")
guess = int(temp)
if guess == 8:
    print("卧槽，你是我心里的蛔虫吗？")
    print("猜中了也没奖励！")
else:
    print("猜错了，心里想的是8！")
print("Game Over!")
print("mie")

count=0
i=1
while(i<10):
    temp = input("猜猜你心里想的什么数字：")
    guess = int(temp)
    i = i+1
    if guess == 8:
        print("卧槽，你是我心里的蛔虫吗？")
        break

for i in range(0,10):
    temp = input("猜猜你心里想的什么数字：")
    guess = int(temp)
    i = i+1
    if guess == 8:
        print("卧槽，你是我心里的蛔虫吗？")
        break