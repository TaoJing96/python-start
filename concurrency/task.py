import asyncio


async def my():
    print(1)
    await asyncio.sleep(2) # io操作会自动切换到其他coroutine运行
    print(2)
    return 'done'


async def main():
    print("main start")
    task_list = [asyncio.create_task(my()), asyncio.create_task(my())]
    print('main end')
    done, pending = await asyncio.wait(task_list, timeout=None)
    print(done)
    print(pending)

if __name__ == '__main__':
    asyncio.run(main())