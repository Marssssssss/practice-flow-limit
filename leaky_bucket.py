# 滑动窗口
import time
import math
import draw


class LeakyBucket(object):
    def __init__(self, capacity, leaky_rate):
        self.capacity = capacity  # 漏桶容量
        self.leaky_rate = leaky_rate  # 漏出速度
        self.start_time = time.time()
        self.next_stamp = self.start_time + self.leaky_rate
        self.cache = 0  # 请求缓存数量
        # 调用成功的记录
        self.success = []  # list(<调用成功的时间戳>)

    def check_limit(self, now):
        # 检查当前容量是否触发限流
        if self.cache >= self.capacity:
            # ERR_LIMIT
            return
        # 加入缓存
        self.cache += 1

    def tick(self, now):
        if now < self.next_stamp:
            return
        deal_req_count = math.floor((now - self.next_stamp) / self.leaky_rate)
        req_count = min(deal_req_count, self.cache)
        self.success.extend([now] * req_count)
        self.cache -= req_count
        self.next_stamp = self.next_stamp + deal_req_count * self.leaky_rate


if __name__ == '__main__':
    rate = 1 / 200  # 1s 处理 200 个请求
    obj = LeakyBucket(600, rate)
    draw.simulate_cases(obj)
