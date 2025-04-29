from openai import OpenAI
from dotenv import load_dotenv
import os

# load the .env file
load_dotenv()

YOUR_API_KEY = os.getenv("YOUR_API_KEY")
MODEL_ID = os.getenv("MODEL_ID")

# Default
client = OpenAI(
    api_key=YOUR_API_KEY,
    base_url="https://api-platform.ope.ai/v1/" 
)
completion = client.chat.completions.create(
  model=MODEL_ID,
  messages=[
   {"role": "system","content": "You are a helpful assistant."},
   {"role": "user","content": "Hello!"}
  ]
)
print(completion.choices[0].message)
# ChatCompletionMessage(content='Hello! How can I assist you today? 😊', refusal=None, role='assistant', annotations=None, audio=None, function_call=None, tool_calls=[], reasoning_content=None)

# Optional
# client = OpenAI(
#     api_key=YOUR_API_KEY,
#     base_url="https://api-platform.ope.ai/v1/" 
# )
# completion = client.chat.completions.create(
#   model=MODEL_ID,
#   messages=[
#     {"role": "system", "content": "You are a helpful assistant."},
#     {"role": "user", "content": "Hello!"}
#   ],
#   temperature=1.0,
#   top_p=1.0,
#   max_tokens=200,
#   frequency_penalty=0,
#   presence_penalty=0
# )
# print(completion.choices[0])
# Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='Hello! How can I assist you today? 😊', refusal=None, role='assistant', annotations=None, audio=None, function_call=None, tool_calls=[], reasoning_content=None), stop_reason=None)

# Streaming
# client = OpenAI(
#     api_key=YOUR_API_KEY,
#     base_url="https://api-platform.ope.ai/v1/" 
# )
# stream = client.chat.completions.create(
#   model=MODEL_ID,
#   messages=[
#     {
#     "role": "user", "content": "Hello!"}
#   ],
#   stream=True
# )
# for chunk in stream:
#     print(chunk.choices[0].delta.content or "", end="")
# Hello! How can I assist you today? 😊

# Functions
# client = OpenAI(
#     api_key=YOUR_API_KEY,
#     base_url="https://api-platform.ope.ai/v1/" 
# )
# completion = client.chat.completions.create(
#   model=MODEL_ID,
#   messages=[{"role": "user", "content": "What is the weather like in Boston today?"}],
#   tools=[{
#     "type": "function",
#     "function": {
#       "name": "get_current_weather",
#       "description": "Get weather",
#       "parameters": {
#         "type": "object",
#         "properties": {
#           "location": {"type": "string"},
#           "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]}
#         },
#         "required": ["location"]
#       }
#     }
#   }],
#   tool_choice={"type": "function", "function": {"name": "get_current_weather"}}
# )
# print(completion.choices[0])
# Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='', refusal=None, role='assistant', annotations=None, audio=None, function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='chatcmpl-tool-13eec61c1af84384b9fa9806b3447189', function=Function(arguments='{"location":"Boston, MA, USA","unit":"fahrenheit"}', name='get_current_weather'), type='function')], reasoning_content=None), stop_reason=None)