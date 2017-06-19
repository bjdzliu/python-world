# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import aiohttp
async def some_function():
 async with aiohttp.ClientSession() as session:
    async with session.get('https://api.github.com/events') as resp:
        print(resp.status)
        print(await resp.text())