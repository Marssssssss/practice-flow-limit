# 流量计数器
import time
import math
import draw

class TrafficCounter(object):
    # 用的惰性的策略，请求来了才尝试刷新计数器

    def __init__(self, wnd_size, limit):
        self.counter = 0
        self.limit = limit  # 窗口限流数
        self.wnd_size = wnd_size  # 窗口大小
        self.start_time = time.time()
        self.next_stamp = self.start_time + self.wnd_size
        # 记录数据
        self.success = []  # list(<通过调用的时间戳>)

    def check_limit(self, now):
        # 窗口结束，重置计数
        if now >= self.next_stamp:
            self.next_stamp = self.start_time + math.ceil(now - self.start_time) * self.wnd_size
            self.counter = 0
        # 达到上限，限流
        if self.counter == self.limit:
            # ERR_LIMITED
            return
        # do something
        self.counter += 1
        self.success.append(now)

    def tick(self, now):
        pass


if __name__ == '__main__':
    obj = TrafficCounter(1, 200)
    draw.simulate_cases(obj)
