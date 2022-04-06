import asyncio
import concurrent.futures


def func1():
    print("func1")
    return "async"


def func2():
    print("func2")


async def main_thread_pool():
    loop = asyncio.get_running_loop()
    fut = loop.run_in_executor(None, func1)
    res = await fut
    print("default executor", res)


async def main_process_pool():
    with concurrent.futures.ProcessPoolExecutor() as pool:
        loop = asyncio.get_running_loop()
        loop.run_in_executor(pool, func2) # 丢入进程池
        res = await loop.run_in_executor(pool, func1)
    print("process executor", res)


if __name__ == '__main__':
    asyncio.run(main_thread_pool())
    asyncio.run(main_process_pool())