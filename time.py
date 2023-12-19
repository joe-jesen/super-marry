import time

def countdown(seconds):
    while seconds > 0:
        # 显示倒计时
        print(seconds)
        
        # 每隔一秒减少一秒
        time.sleep(1)
        seconds -= 1
    
    # 倒计时结束时显示提示信息
    print("倒计时结束！")

# 设置倒计时时长
seconds = 10

# 启动倒计时
countdown(seconds)
