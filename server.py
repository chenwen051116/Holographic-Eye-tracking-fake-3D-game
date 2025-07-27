import asyncio
import websockets
import os


async def handle_connection(websocket, path=None):
    print("客户端已连接")
    try:
        # 读取 output.txt 文件内容
        file_path = os.path.join(os.path.dirname(__file__), "output.txt")


        while True:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
            # 发送文件内容
            await websocket.send(content)
            await asyncio.sleep(1)  # 每秒发送一次
    except FileNotFoundError:
        await websocket.send("错误：output.txt 文件未找到")
    except websockets.exceptions.ConnectionClosedOK:
        print("客户端断开连接")


async def main():
    async with websockets.serve(handle_connection, "127.0.0.1", 12321):
        print("WebSocket服务器已启动，监听端口12321...")
        await asyncio.Future()  # 永远不退出


if __name__ == "__main__":
    asyncio.run(main())