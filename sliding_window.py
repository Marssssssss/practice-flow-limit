# 滑动窗口
import time
import math
import draw


class SlidingWindow(object):
    def __init__(self, wnd_size, wnd_count, limit):
        self.windows = [0]
        self.wnd_count = wnd_count
        self.wnd_size = wnd_size  # 窗口的时间跨度
        self.limit = limit  # 窗口总限流数
        self.start_time = time.time()
        self.next_stamp = self.start_time + self.wnd_size
        # 调用成功的记录
        self.success = []  # list(<调用成功的时间戳>)

    def check_limit(self):
        # 检查窗口循环
        now = time.time()
        duration = now - self.next_stamp
        if duration >= 0:
            # 长时间没有请求的情况下，补前面的窗口
            for _ in range(min(math.ceil(duration / self.wnd_size), self.wnd_count)):
                if len(self.windows) == self.wnd_count:
                    self.windows.pop(0)
                self.windows.append(0)
            self.next_stamp = math.ceil(duration / self.wnd_size) * self.wnd_size + self.start_time
        # 检查总限流数
        if sum(self.windows) == self.limit:
            # ERR_LIMIT
            return
        # do something
        self.windows[-1] += 1
        self.success.append(now)


if __name__ == '__main__':
    obj = SlidingWindow(1, 10, 2000)
    draw.simulate_requests(obj)
    draw.generate_time_series_plot(obj.success, 0.1)
