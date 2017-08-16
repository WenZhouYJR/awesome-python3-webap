import asyncio


@asyncio.coroutine
def hello(str):
    print("Hello world %s!", str)
    # 异步调用asyncio.sleep(1):
    r = yield from asyncio.sleep(1)
    print("等待了1秒%s", r)
    print("Hello again %s!",str)


# 获取EventLoop:
loop = asyncio.get_event_loop()
task = [hello("ac"), hello("dd"), hello("12"), hello("23"), hello("34"), hello("45"), hello("56"), hello("67")]
# 执行coroutine
loop.run_until_complete(asyncio.wait(task))
loop.close()
