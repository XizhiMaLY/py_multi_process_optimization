import time
from threading import Thread

class NewThread(Thread):
    def __init__(self):
        Thread.__init__(self)  # 必须步骤
    
    def run(self):  # 入口是名字为run的方法
        print("开始做一个任务啦")
        print(__name__)
        time.sleep(3)  # 用time.sleep模拟任务耗时
        print("这个任务结束啦")
        
if __name__ == '__main__':
    print("这里是主线程")
    # 创建线程对象
    t1 = NewThread()
    # 启动
    t1.start()
    time.sleep(0.3)
    print("主线程依然可以干别的事")
