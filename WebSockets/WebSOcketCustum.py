import asyncio
import websockets

data = []

async def hello(websocket, path):
    name = await websocket.recv()
    print(f"< {name}")
    greeting = f"Hello {name}!"
    data.append(name)
    await websocket.send(str(data))
    print(f"> {greeting}")

start_server = websockets.serve(hello, '192.168.70.15', 6000)

asyncio.get_event_loop().run_until_complete(start_server) 
asyncio.get_event_loop().run_forever() 