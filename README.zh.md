# OPE.AI 官方示例库

涵盖 OPE.AI 平台各类API的调用示例，帮助开发者快速接入人工智能服务。

### 核心功能示例
| 类别          | 示例路径                                  | 功能描述                     |
|---------------|------------------------------------------|----------------------------|
| 文本对话      | examples/text-chat                       | 聊天补全、流式响应、函数调用 |
| 实时音频      | examples/audio/realtime                  | 语音转录、实时语音对话       |
| 图像生成      | examples/images                          | DALL·E 图像生成与编辑       |

## 快速开始

### 前置要求
```bash
# 安装基础依赖
pip install openai python-dotenv websocket-client
```

### 配置密钥
1. 复制环境模板
```bash
cp .env.example .env
```
2. 编辑配置文件
```bash
# .env
YOUR_API_KEY=your_api_key  # 替换为您的API密钥
```

> 默认MODEL_ID=opeai/deepseek-v3，如需其他模型请自行修改。

### 运行示例
```bash
-文本对话示例
# 进入示例目录
cd examples/text-chat
# 运行示例
python text_chat_demo.py

-实时音频示例
# 进入示例目录
cd examples/audio/realtime
# 运行示例
python realtime_demo.py

-tts 文本音频合成示例
# 进入示例目录
cd examples/audio/tts
# 运行示例
python tts_demo.py
```     