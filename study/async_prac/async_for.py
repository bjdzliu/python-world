import asyncio

async def asynchronous_generator():
    for i in range(111):
        yield i
        await asyncio.sleep(0.1)  # Simulate an asynchronous operation

async def main():
    async for i in asynchronous_generator():
        print(i)

# Run the event loop
asyncio.run(main())
