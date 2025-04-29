## 文本语音合成


## python 依赖
```bash
pip install requests
```

### 请求地址
```bash
POST https://api-platform.ope.ai/v1/audio/speech
```

请参考 [快速上手指南](https://platform.ope.ai/market/token, "点击跳转快速上手指南") 获取您的 API 密钥。

> 将 $YOUR_API_KEY 替换为您上一步生成的实际 API 密钥。
> 请将 $AUDIO_SAMPLE_URL 替换为语音样本的 URL，并将 $OUTPUT_PATH 替换为音频输出保存路径。

### curl 非流式示例
```bash
curl --location --request POST 'https://api-platform.ope.ai/v1/audio/speech' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer $YOUR_API_KEY' \
--data-raw '{
  "model": "$MODEL_ID", 
  "text": "Hi! My name is Mike.", 
  "language": "en",
  "sample_rate": 8000,
  "format": "wav",
  "speed": 1.0,
  "instruct_text": "Say it in a cheerful tone,",
  "prompt_speech":"AUDIO_SAMPLE_URL"
}'  --output $OUTPUT_PATH
```

### curl 流式示例
```bash
curl --location --request POST 'https://api-platform.ope.ai/v1/audio/speech' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer $YOUR_API_KEY' \
--data-raw '{
  "model": "$MODEL_ID", 
  "text": "Hi! My name is Mike.", 
  "language": "en",
  "sample_rate": 8000,
  "format": "ogg",
  "stream": true, 
  "speed": 1.0, 
  "instruct_text": "Say it in a cheerful tone,",
  "prompt_speech":"AUDIO_SAMPLE_URL"
}' --output $OUTPUT_PATH
```

### python 非流式示例
```python
import requests

url = "https://api-platform.ope.ai/v1/audio/speech"
headers = {
    "Authorization": "Bearer $YOUR_API_KEY",
    "Content-Type": "application/json"
}

payload = {
    "model": "$MODEL_ID",
    "text": "Hi! My name is Mike.",
    "language": "en",
    "sample_rate": 8000,
    "format": "wav",
    "speed": 1.0,
    "instruct_text": "Say it in a cheerful tone,",
    "prompt_speech": "AUDIO_SAMPLE_URL"
}

response = requests.post(url, headers=headers, json=payload)
if response.status_code == 200:
    with open("output.wav", "wb") as f:
        f.write(response.content)
    print("Saved as output.wav")
else:
    print("Failed:", response.status_code)
    print(response.text)
```

### python 流式示例
```python
import requests

url = "https://api-platform.ope.ai/v1/audio/speech"
headers = {
    "Authorization": "Bearer $YOUR_API_KEY",
    "Content-Type": "application/json"
}

payload = {
    "model": "$MODEL_ID",
    "text": "Hi! My name is Mike.",
    "language": "en",
    "sample_rate": 8000,
    "format": "ogg",
    "stream": True,
    "speed": 1.0,
    "instruct_text": "Say it in a cheerful tone,",
    "prompt_speech": "AUDIO_SAMPLE_URL"
}

response = requests.post(url, headers=headers, json=payload, stream=True)
if response.status_code == 200:
    with open("output_stream.ogg", "wb") as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    print("Streamed and saved as output_stream.ogg")
else:
    print("Failed:", response.status_code)
    print(response.text)
```

###APi请求体参数说明
字段 | 类型 | 必填 | 允许值 | 说明
---|---|---|---|---
model | string | 是 | - | 用于生成回复的模型 ID。该字段支持两种类型的模型：语音生成模型：将文本转换为自然语音。声色克隆模型：模仿特定说话人声音进行生成。两种模型均可调用。
text | string | 是 | - | 要转换为语音的文本。
language | string | 是 | - | 文本的语言代码。
sample_rate | integer | 否 | 8000/12000/16000/24000/48000等 | 音频采样率，单位为 Hz。默认为 8000
format | string | 否 | wav/mp3/ogg | 输出音频格式。通常支持：wav、mp3、ogg。默认值为 wav。
stream | boolean | 否 | true/false | 若设为 true，API 将以流式格式返回音频，客户端可在生成过程中实时接收与播放音频，降低延迟。若设为 false 或省略，API 会在生成完成后返回完整音频文件。默认值为 false。
speed | float | 否 | 0.0-2.0 | 控制生成速度。可接受范围通常为 0.0 到 2.0。默认值为 1.0。
instruct_text | string | 否 | - | 自然语言指令，用于引导模型的语气、情绪、语速、方言或角色风格。为了确保最佳音质，请至少包含下方所列的支持关键词之一：支持关键词：・情感：高兴、悲伤、惊讶、愤怒、恐惧、厌恶、冷静、严肃等 ・语速：快速、非常快速、慢速、非常慢速 ・方言：粤语、四川话、上海话、郑州话、长沙话、天津话等 ・角色扮演：神秘、凶狠、好奇、优雅、孤独、机器人、小猪佩奇等。<br>示例值：<br>-"用开心的语气说话"<br>-"使用非常慢且冷静的语调"<br>-"像小猪佩奇那样说话"<br>-"用四川话并带有好奇的语气说话"。 <br>默认值为 ""（不提供提示）。
prompt_speech | string ｜ 否 | - | 参考音频文件的 URL。模型将模仿提供的语音样本的音色、语调、风格进行语音生成。该音频必须通过公网可访问，格式应为标准音频格式如 .mp3、.wav 等。注意：仅当所选模型支持音色克隆功能时该字段才会生效；若为语音生成模型，填写此字段将不会产生效果。若未提供此字段，系统将使用默认语音。

返回值：二进制音频文件。

- ⚠️ **注意**：使用 curl 时，如果未指定 --output 选项，API 返回的二进制内容将直接打印至终端，可能导致乱码或界面错乱。请务必使用：--output $OUTPUT_PATH 将音频另存为文件。