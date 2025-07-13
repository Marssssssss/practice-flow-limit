# 流量图
import matplotlib.pyplot as plt
import time
import math


def simulate_cases(obj):
    # simulate_requests(obj, 200, 10)  # 模拟卡在限流量上的请求
    # simulate_requests(obj, 300, 10)  # 模拟稍微超出限流量的请求
    # simulate_requests(obj, 1000, 10)  # 模拟超大量请求

    # 1s 的请求偏移到限流窗口中间
    # for _ in range(3):
    #     simulate_requests(obj, 0, 0.5)
    #     simulate_requests(obj, 1000, 0.5)
    #     simulate_requests(obj, 1000, 0.5)
    #     simulate_requests(obj, 0, 0.5)

    # 瞬发流量后没有流量进来
    # simulate_requests(obj, 2000, 0.5)
    # simulate_requests(obj, 1, 4)

    # 流量抖动的场景
    for _ in range(10):
        simulate_requests(obj, 1000, 0.2)
        simulate_requests(obj, 10, 0.2)

    show_success_reqs_per_granularity(obj.start_time, obj.success, 0.1)
    # show_success_reqs_per_granularity(obj.start_time, obj.success, 1)



def simulate_requests(obj, reqs_per_sec, duration):
    try:
        req_duration = 1 / reqs_per_sec if reqs_per_sec > 0 else duration
        start_time = time.time()
        next_req_time = start_time
        now = start_time
        while now - start_time < duration:
            obj.tick(now)
            if now >= next_req_time:
                req_count = max(math.floor((now - next_req_time) / req_duration), 0)
                for _ in range(req_count):
                    obj.check_limit(now)
                next_req_time = req_count * req_duration + next_req_time
            time.sleep(0.0001)
            now = time.time()
    except KeyboardInterrupt:
        pass


def show_success_reqs_per_granularity(start_time, timestamps, time_granularity):
    """ 每个 time_granularity 周期内成功通过的请求数 """
    print("success: ", len(timestamps))
    cur_x = start_time
    count = 0
    x, y = [0], [0]
    idx = 0
    while idx < len(timestamps):
        timestamp = timestamps[idx]
        if timestamp - cur_x > time_granularity:
            cur_x += time_granularity
            x.append(cur_x - start_time)
            y.append(count)
            count = 0
            continue
        count += 1
        idx += 1
    x.append(cur_x - start_time)
    y.append(count)
    plt.figure(figsize=(12, 8))
    plt.plot(x, y, marker=".")
    plt.show()
