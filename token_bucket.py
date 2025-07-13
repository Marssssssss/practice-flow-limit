# 滑动窗口
import time
import math
import draw


class TokenBucket(object):
    def __init__(self, capacity, token_rate):
        self.capacity = capacity  # 令牌容量
        self.token_rate = token_rate  # 令牌添加速度
        self.start_time = time.time()
        self.next_stamp = self.start_time + self.token_rate
        self.token = capacity  # 请求缓存数量
        # 调用成功的记录
        self.success = []  # list(<调用成功的时间戳>)

    def check_limit(self, now):
        # 检查当前容量是否触发限流
        if self.token <= 0:
            # ERR_LIMIT
            return
        # 成功执行
        self.token -= 1
        self.success.append(now)

    def tick(self, now):
        if now < self.next_stamp:
            return
        deal_add_tokens = math.floor((now - self.next_stamp) / self.token_rate)
        add_tokens = min(deal_add_tokens, self.capacity - self.token)
        self.token += add_tokens
        self.next_stamp = self.next_stamp + deal_add_tokens * self.token_rate


if __name__ == '__main__':
    rate = 1 / 200  # 1s 放入 200 个令牌
    obj = TokenBucket(60, rate)
    draw.simulate_cases(obj)
