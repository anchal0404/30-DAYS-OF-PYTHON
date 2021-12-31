import asyncio
import time

async def waiting(delay, a):
    await asyncio.sleep(delay)
    print(a)

async def main():
    print(f"started at {time.strftime('%X')}")

    await waiting(1, 'Anchal')
    await waiting(2, 'Rathore')

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())