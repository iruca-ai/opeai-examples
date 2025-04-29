import os
import json
import websocket
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("YOUR_API_KEY")

# 语音对语音
url = "wss://api-platform.ope.ai/v1/realtime?model=opeai/AudioLLM/Voice2"
headers = [
    "Authorization: Bearer " + API_KEY,
    "OpenAI-Beta: realtime=v1",
    "Sec-WebSocket-Protocol:realtime, openai-insecure-api-key." + API_KEY + ", openai-beta.realtime-v1",
]

def on_open(ws):
    print("已连接至服务器。")

def on_message(ws, message):
    data = json.loads(message)
    print("收到事件:", json.dumps(data, indent=2))

def on_error(ws, error):  # 新增错误回调
    print(f"连接错误: {error}")

def on_close(ws, close_status_code, close_msg):  
    print(f"连接关闭，状态码：{close_status_code}，信息：{close_msg}")

ws = websocket.WebSocketApp(
    url, 
    header=headers,
    on_open=on_open,
    on_message=on_message,
    on_error=on_error,  # 添加错误处理
    on_close=on_close   # 添加关闭处理
)

ws.run_forever()