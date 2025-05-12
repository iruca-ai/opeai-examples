import os
import requests

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("YOUR_API_KEY")
AUDIO_SAMPLE_URL = ""

# ---------------非流式文本语音合成---------------
url = "https://api-platform.ope.ai/v1/audio/speech"
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

payload = {
    "model": "opeai/AudioLLM/Voice-GT",
    "text": "Hi! My name is Mike.",
    "language": "en",
    "sample_rate": 8000,
    "format": "wav",
    "speed": 1.0,
    "instruct_text": "Say it in a cheerful tone,",
    "prompt_speech": AUDIO_SAMPLE_URL
}

response = requests.post(url, headers=headers, json=payload)
if response.status_code == 200:
    with open("output.wav", "wb") as f:
        f.write(response.content)
    print("Saved as output.wav")
else:
    print("Failed:", response.status_code)
    print(response.text)


# ---------------流式文本语音合成---------------
# url = "https://api-platform.ope.ai/v1/audio/speech"
# headers = {
#     "Authorization": f"Bearer {API_KEY}",
#     "Content-Type": "application/json"
# }

# payload = {
#     "model": "opeai/AudioLLM/Voice-GT",
#     "text": "Hi! My name is Mike.",
#     "language": "en",
#     "sample_rate": 8000,
#     "format": "ogg",
#     "stream": True,
#     "speed": 1.0,
#     "instruct_text": "Say it in a cheerful tone,",
#     "prompt_speech": AUDIO_SAMPLE_URL
# }

# response = requests.post(url, headers=headers, json=payload, stream=True)
# if response.status_code == 200:
#     with open("output_stream.ogg", "wb") as f:
#         for chunk in response.iter_content(chunk_size=1024):
#             print("chunk", len(chunk))
#             if chunk:
#                 f.write(chunk)
#     print("Streamed and saved as output_stream.ogg")
# else:
#     print("Failed:", response.status_code)
#     print(response.text)