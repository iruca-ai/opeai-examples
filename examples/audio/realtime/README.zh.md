# OPE.AI 实时语音示例

## 项目概述
使用 Realtime API 构建低延迟的多模态体验。
OPE.AI Realtime API 支持低延迟的多模态交互，包括语音对语音的对话体验和实时转录功能。

## python 依赖
```bash
pip install dotenv
pip install websocket-client
```

## 使用 WebSocket 连接
WebSocket 是一种广泛支持的实时数据传输 API，非常适合在服务端集成中连接 OPE.AI Realtime API。

## 概览
在服务端与 Realtime API 的集成中，你的后端系统将通过 WebSocket 与 Realtime API 直接连接。你可以使用 标准 API 密钥 来进行身份验证，因为这个密钥仅用于你安全的后端环境中。
标准 [API密钥](https://platform.ope.ai/market/token, "点击跳转密钥界面") 只应在安全的服务器端环境中使用。

## 连接详情
### 语音对语音
通过 WebSocket 连接时需要以下信息：
URL | wss://api-platform.ope.ai/v1/realtime
---|---
查询参数 | `model`, 要连接的 Realtime 模型 ID，例如 `opeai/AudioLLM/Voice2`
请求头 | `Authorization: Bearer $YOUR_API_KEY`<br>OpenAI-Beta: realtime=v1<br>Sec-WebSocket-Protocol:realtime, openai-insecure-api-key."$API_KEY", openai-beta.realtime-v1<br>此标头在 beta 阶段是必需的。

Node.js 示例代码：
```javascript
import WebSocket from "ws";

const url = "wss://api-platform.ope.ai/v1/realtime?model=opeai/AudioLLM/Voice2";
const ws = new WebSocket(url, {
  headers: {
    "Authorization": "Bearer " + process.env.API_KEY,
    "OpenAI-Beta": "realtime=v1",
    "Sec-WebSocket-Protocol:realtime, openai-insecure-api-key." + process.env.API_KEY + ", openai-beta.realtime-v1",
  },
});

ws.on("open", () => console.log("已连接"));
ws.on("message", (msg) => console.log(JSON.parse(msg.toString())));
```

python 示例代码：
```python
import os
import json
import websocket

API_KEY = os.environ.get("API_KEY")

url = "wss://api-platform.ope.ai/v1/realtime?model=opeai/AudioLLM/Voice2"
headers = [
    "Authorization: Bearer " + API_KEY,
    "OpenAI-Beta: realtime=v1"
]

def on_open(ws):
    print("已连接至服务器。")

def on_message(ws, message):
    data = json.loads(message)
    print("收到事件:", json.dumps(data, indent=2))

ws = websocket.WebSocketApp(
    url, 
    header=headers,
    on_open=on_open,
    on_message=on_message,
)

ws.run_forever()
```

web 示例代码：
```javascript
const ws = new WebSocket(
  "wss://api-platform.ope.ai/v1/realtime?model=opeai/AudioLLM/Voice2",
  [
    "realtime",
    // 认证
    "openai-insecure-api-key." + API_KEY,
    // Beta 协议，必须
    "openai-beta.realtime-v1"
  ]
);

ws.on("open", function open() {
  console.log("已连接至服务器。");
});

ws.on("message", function incoming(message) {
  console.log(message.data);
});
```