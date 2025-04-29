# OPE.AI 对话补全示例

## 项目概述
演示如何通过OPE.AI API创建对话补全，包含基础对话、工具调用、流式响应等功能

## 快速开始
### 环境准备
1. 复制环境模板
```bash
cp .env.example .env
```
2. 编辑配置文件
```bash
# .env
YOUR_API_KEY=your_api_key  # 替换为您的API密钥
```
3. 安装依赖
```bash
pip install openai
```

## default curl 示例
```bash
curl https://api-platform.ope.ai/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $YOUR_API_KEY" \
  -d '{
    "model": "$MODEL_ID",
    "messages": [
      {
        "role": "system",
        "content": "You are a helpful assistant."
      },
      {
        "role": "user",
        "content": "Hello!" 
      }
    ]
  }'
```
## 更多 DEMO 参照examples/text-chat/create-chat-completion/curl.txt

## default python 示例
```bash
from openai import OpenAI

client = OpenAI(
    api_key="$YOUR_API_KEY",
    base_url="https://api-platform.ope.ai/v1/" 
)
completion = client.chat.completions.create(
  model="$MODEL_ID",
  messages=[
   {"role": "system","content": "You are a helpful assistant."},
   {"role": "user","content": "Hello!"}
  ]
)
print(completion.choices[0].message)

```
## 更多 DEMO 参照examples/text-chat/create-chat-completion/demo.py

## 请求地址
- POST https://api-platform.ope.ai/v1/chat/completions

## API 请求参数说明
参数名 | 类型 | 是否必填 | 说明
---|---|---|---
model | string | 是 | 用于生成回复的模型 ID。OPE.AI 提供了各种具有不同能力、性能特性和价格的模型。请参阅模型指南浏览和比较可用模型。
messages | array | 是 | 由目前为止对话消息组成的列表。详见下表。
frequency_penalty | integer | 否 | 在 -2.0 到 2.0 之间。正值根据文本中已有的出现频率对新 token 进行惩罚，从而降低模型逐字重复同一行的可能性。
max_tokens | integer | 否 | 对话补全中可生成的最大 token 数量。可以通过此值控制 API 生成文本的费用。
parallel_tool_calls | boolean | 否 | 启用工具使用期间的并行函数调用。
presence_penalty | integer | 否 | 介于 -2.0 到 2.0 之间的数字。正值会根据新词是否已在文本中出现而对其进行惩罚，增加模型谈论新话题的可能性。
seed | integer | 否 | 该功能目前处于 Beta 测试阶段。如果指定，系统将尽力进行确定性采样，即相同的 seed 和参数应返回相同的结果。但确定性不保证，需参阅响应中的 system_fingerprint 参数以监控后端变更。
stop | array | 否 | 最多提供 4 个停止序列，API 在生成到这些序列时停止。返回文本中不会包含停止序列。
stream | boolean | 否 | 指定是否使用流式输出，・false：模型生成完所有内容后一次性返回结果。 ・true：边生成边输出，即每生成一部分内容就立即输出一个片段（chunk）。您需要实时地逐个读取这些片段以获得完整的结果。
stream_options | object | 否 | 流式响应选项。仅当 stream: true 时设置。详见下表。
temperature | integer | 否 | 采样温度，范围 0 到 2。较高的值（如 0.8）会使输出更随机，较低的值（如 0.2）则使输出更聚焦、确定性更高。一般建议调整此参数或 top_p，但不要同时调整两者。
tool_choice | string/object | 否 | 控制模型调用哪个工具（如果有的话）。详见下表。
tools | array | 否 | 模型可以调用的工具列表。目前仅支持函数作为工具。 使用此选项可以提供模型可能生成 JSON 输入的函数列表。最多支持 128 个函数。详见下表。
top_p | integer | 否 | 控制模型生成文本的多样性，值越大生成的文本越不相同
top_k | integer | 否 | 控制模型生成文本的多样性，值越大生成的文本越不相同
    
### `messages` 字段对象参数说明
字段 | 类型 | 必填 | 允许值 | 说明
---|---|---|---|---
role | string | 是 | system/user/assistant | 消息角色类型
content | string | 是 | - | 消息文本内容（最长4096字符）
name | string | 否 | - | 参与者名称（区分多用户场景）
    
### `stream_options` 字段对象参数说明
字段 | 类型 | 必填 | 允许值 | 说明
---|---|---|---|---
include_usage |  boolean | 否 | true/false | 如果设置，在 data: [DONE] 消息之前将流式传输一个额外块，usage 字段将显示整个请求的 token 使用统计，choices 字段始终为空数组。 其他块也包含 usage 字段，但值为 null。注意：如果流中断，可能无法收到最终的使用情况块。
    
### `tool_choice` 字段对象参数说明
值 | 类型 | 说明
---|---|---
none | string | 模型不会调用任何工具，而是生成消息
auto | string | 模型可选择生成消息或调用一个或多个工具
required | string | 模型必须调用一个或多个工具
`{"type": "function", "function": {"name": "my_function"}}` | object | 模型调用指定的工具对象
    
### `tools` 字段对象参数说明
字段 | 类型 | 必填 | 允许值 | 说明
---|---|---|---|---
type | string | 是 | function | 工具类型
function | object | 是 | - | 工具对象。详见下表。
        
#### `tools`.`function` 字段对象参数说明
字段 | 类型 | 必填 | 允许值 | 说明
---|---|---|---|---
name | string | 是 | - | 工具名称
strict | boolean | 否 | true/false | 是否在生成函数调用时启用严格模式。如果设置为 true，模型将严格遵循 parameters 字段中定义的模式。
description | string | 是 | - | 函数的描述，模型将根据描述选择何时以及如何调用函数。
parameters | object | 是 | - | 以 JSON Schema 格式描述。

## 响应示例
```json
{
 "id": "chatcmpl-B9MHDbslfkBeAs8l4bebGdFOJ6PeG",
 "object": "chat.completion",
 "created": 1741570283,
 "model": "$MODEL_ID",
 "choices": [
   {
     "index": 0,
     "message": {
       "role": "assistant",
       "content": "The image shows a wooden boardwalk path running through a lush green field or meadow. The sky is bright blue with some scattered clouds, giving the scene a serene and peaceful atmosphere. Trees and shrubs are visible in the background.",
       "refusal": null
     },
     "finish_reason": "stop"
   }
 ],
 "usage": {
   "prompt_tokens": 1117,
   "completion_tokens": 46,
   "total_tokens": 1163,
   },
 "system_fingerprint": "fp_fc9f1d7035"
 }
 ```

## API 返回对话补全对象说明
字段 | 类型 | 说明
---|---|---
choices | array | 对话补全结果列表。详见下表。
created | integer | 对话补全创建的 Unix 时间戳（秒）。
id  | string | 对话补全的唯一标识符。
model | string | 用于对话补全的模型。
object | string | 对象类型，始终为 chat.completion。
system_fingerprint | string | 表示模型运行时后端配置的指纹。可与 seed 请求参数配合使用，以了解后端配置变更对确定性的影响。
usage | object | 补全请求的使用统计数据。详见下表。

### `usage` 字段对象参数说明
字段 | 类型 | 说明
---|---|---
completion_tokens | integer | 生成的补全中的令牌数量。
prompt_tokens | integer | 提示中的令牌数量。
total_tokens | integer | 请求中使用的总令牌数（提示 + 补全）。

### `choices` 字段对象参数说明
字段 | 类型 | 说明
---|---|---
finish_reason | string | 对话补全结束原因.如果模型到达自然停止点或提供的停止序列，则为 stop；如果达到请求指定的最大令牌数，则为 length；如果因内容过滤器被删除内容，则为 content_filter；如果调用了工具，则为 tool_calls。
index | integer | 对话补全结果的索引。
message | object | 对话补全结果消息对象。详见下表。

#### `choices`.`message` 字段对象参数说明
字段 | 类型 | 说明
---|---|---
role | string | 消息作者的角色。
content | string | 消息内容。
reasoning_content | string | 仅适用于推理模型。内容为 assistant 消息中在最终答案之前的推理内容。
refusal | string | 模型生成的拒绝消息。
tool_calls | array | 模型生成的工具调用（例如函数调用）。详见下表。

##### `choices`.`message`.`tool_calls` 字段对象参数说明
字段 | 类型 | 说明
---|---|---
id | string | 工具调用的唯一标识符。
type | string | 工具调用的类型。目前仅支持 function。
function | object | 工具调用的函数对象。详见下表。

###### `choices`.`message`.`tool_calls`.`function` 字段对象参数说明
字段 | 类型 | 说明
---|---|---
name | string | 函数名称。  
arguments | string | 模型以 JSON 格式生成的调用函数参数。请注意，模型可能不一定生成有效 JSON，也可能幻观出未存在的参数，调用函数前应验证。

## 流式请求 python 示例
```bash
client = OpenAI(
    api_key="$YOUR_API_KEY",
    base_url="https://api-platform.ope.ai/v1/" 
)
stream = client.chat.completions.create(
  model="$MODEL_ID",
  messages=[
    {
    "role": "user", "content": "Hello!"}
  ],
  stream=True
)
for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="")

```

## 当stream=True时，流式响应示例
```json
{
{"id":"chatcmpl-123","object":"chat.completion.chunk","created":1694268190,"model":"$MODEL_ID", "system_fingerprint": "fp_44709d6fcb", "choices":[{"index":0,"delta":{"role":"assistant","content":""},"finish_reason":null}]}
{"id":"chatcmpl-123","object":"chat.completion.chunk","created":1694268190,"model":"$MODEL_ID", "system_fingerprint": "fp_44709d6fcb", "choices":[{"index":0,"delta":{"content":"Hello"},"finish_reason":null}]}
...
{"id":"chatcmpl-123","object":"chat.completion.chunk","created":1694268190,"model":"$MODEL_ID", "system_fingerprint": "fp_44709d6fcb", "choices":[{"index":0,"delta":{},"finish_reason":"stop"}]}
}
```
## 流式响应返回说明
字段 | 类型 | 说明
---|---|---
choices | array | 对话补全结果列表。详见下表。
created | integer | 对话补全创建的 Unix 时间戳（秒）。
id  | string | 对话补全的唯一标识符。
model | string | 用于对话补全的模型。
object | string | 对象类型，始终为 chat.completion.chunk。
system_fingerprint | string | 表示模型运行时后端配置的指纹。可与 seed 请求参数配合使用，以了解后端配置变更对确定性的影响。
usage | object | 补全请求的使用统计数据。详见下表。

### `usage` 字段对象参数说明
字段 | 类型 | 说明
---|---|---
completion_tokens | integer | 生成补全使用的令牌数。
prompt_tokens | integer | 提示词使用的令牌数。
total_tokens | integer | 请求中使用的令牌总数（提示 + 补全）。

### `choices` 字段对象参数说明
字段 | 类型 | 说明
---|---|---
delta | object | 由流式模型响应生成的对话补全增量。详见下表。
finish_reason | string | 对话补全结束原因.如果模型到达自然停止点或提供的停止序列，则为 stop；如果达到请求指定的最大令牌数，则为 length；如果因内容过滤器被删除内容，则为 content_filter；如果调用了工具，则为 tool_calls。
index | integer | 对话补全结果的索引。

#### `choices`.`delta` 字段对象参数说明
字段 | 类型 | 说明
---|---|---
content | string | 生成的补全中的令牌数量。
role | string | 提示中的令牌数量。
tool_calls | array | 模型生成的工具调用（例如函数调用）。详见下表。

##### `choices`.`delta`.`tool_calls` 字段对象参数说明
字段 | 类型 | 说明
---|---|---
id | string | 工具调用的唯一标识符。
type | string | 工具调用的类型。目前仅支持 function。
index | string | 工具调用列表中的索引。
function | object | 工具调用的函数对象。详见下表。

###### `choices`.`delta`.`tool_calls`.`function` 字段对象参数说明
字段 | 类型 | 说明
---|---|---
name | string | 要调用的函数名称。
arguments | string | 模型以 JSON 格式生成的函数调用参数。请注意，模型生成的 JSON 可能无效，且可能生成未在函数模式中定义的参数。请在调用函数前自行验证参数。