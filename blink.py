import time

print("Hello, 树莓派! 我是 STM32 老兵。")
print("网络已修好，终端就是我的手术刀。")

for i in range(5):
    print(f"倒计时: {5-i}")
    time.sleep(1)

print("执行完毕！系统交回控制权。")


