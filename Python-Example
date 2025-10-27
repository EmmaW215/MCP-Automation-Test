from* openai import OpenAI
client = OpenAI(
base_url="http://localhost:11434/v1",  # 改成 Ollama 地址
api_key="ollama",                      # 必填但随意写
)
response = client.chat.completions.create(
model="llama2",                        # 必须是已 pull 的模型名
messages=[
{"role": "system", "content": "You are a helpful assistant."},
{"role": "user", "content": "今天天气怎么样？"}
]
)
