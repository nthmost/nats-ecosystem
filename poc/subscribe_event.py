#!/usr/bin/env python3

import asyncio
from nats.aio.client import Client as NATS

async def run():
    nc = NATS()
    await nc.connect("nats://nike.local:4222")

    async def message_handler(msg):
        subject = msg.subject
        data = msg.data.decode()
        print(f"Received a message on '{subject}': {data}")
        # Perform an action in response
        # For example, log the event or trigger another script

    await nc.subscribe("device.telephone", cb=message_handler)

    # Keep the script running indefinitely
    while True:
        await asyncio.sleep(1)

if __name__ == '__main__':
    asyncio.run(run())

