import serial

ser = serial.Serial(port="/dev/ttyAMA4", baudrate=115200, timeout=0.1)

buffer = ""
collecting = False

while True:
    if ser.in_waiting > 0:
        char = ser.read().decode('utf-8', errors='ignore')
        if char == 'k': 
            if len(buffer) > 5:
                parts = buffer.split(',')
                try:
                    x = float(parts[1])
                    y = float(parts[2])
                    z = float(parts[3])
                    print(f"x: {x}, y: {y}, z: {z}")
                except ValueError:
                    pass  # Ignore malformed data
            buffer = 'k'
            collecting = True
        elif collecting:
            buffer += char

# import serial
# import asyncio
# import websockets

# ser = serial.Serial(port="/dev/ttyAMA4", baudrate=115200, timeout=0.1)

# buffer = ""
# collecting = False

# async def handler(websocket, path):
#     global buffer, collecting  # allow access to and mutation of the outer variables
    
#     while True:
#         if ser.in_waiting > 0:
#             char = ser.read().decode('utf-8', errors='ignore')
#             if char == 'k': 
#                 if len(buffer) > 5:
#                     print(buffer+"\n")
#                     parts = buffer.split(',')
#                     try:
#                         x = float(parts[1])
#                         y = float(parts[2])
#                         z = float(parts[3])
                        
#                         await websocket.send(buffer)
#                         await asyncio.sleep(0.001)
#                     except ValueError:
#                         pass  # Ignore malformed data
#                 buffer = 'k'
#                 collecting = True
#             elif collecting:
#                 buffer += char

# async def main():
#     async with websockets.serve(handler, "localhost", 12322):
#         print("WebSocket server started on ws://localhost:6789")
#         await asyncio.Future()  # run forever

# if __name__ == "__main__":
#     asyncio.run(main())
