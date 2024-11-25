#!/usr/bin/env python3

import asyncio
from nats.aio.client import Client as NATS

async def run():
    nc = NATS()
    await nc.connect("nats://localhost:4222")

    await nc.publish("device.offhook", b"Handset is off-hook")
    await nc.drain()

if __name__ == '__main__':
    asyncio.run(run())

