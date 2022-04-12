import time
from datetime import datetime, timedelta

t = time.time()

print(int(round(t * 1000000)))  # 微秒级时间戳

def get_current_time():
    """
    format the current time in a specific way. eg. 2021-04-06T16:21:55.123456Z
    :return: str after formatting
    """
    return datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')


if __name__ == '__main__':
    if '2022-03-28T18:27:02.217020Z' > '2022-03-29T18:27:02.217019Z':
        print(True)
    else:
        print(False)
    print(get_current_time())
