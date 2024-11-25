#!/usr/bin/env python3

import asyncio
from nats.aio.client import Client as NATS

async def run():
    nc = NATS()
    await nc.connect("nats://localhost:4222")

    # Simulate off-hook event
    subject = "device.telephone"
    message = "Handset lifted on nike"

    await nc.publish(subject, message.encode())
    await nc.drain()

if __name__ == '__main__':
    asyncio.run(run())

