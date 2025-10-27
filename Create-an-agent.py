# pip install -qU "langchain[anthropic]" to call the model

from langchain.agents import create_agent

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

agent = create_agent(
    model="anthropic:claude-sonnet-4-5",
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

# Run the agent
agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
)


# 脚本使用 anthropic Claude 模型，但默认的 langchain 并未包含 anthropic 驱动。已为您在虚拟环境中安装 langchain-anthropic 及其依赖 anthropic。现在可重新运行 Create-an-agent.py，应能正常加载 Claude-Sonnet-4-5（前提：你有 Anthropic API Key 并已设为环境变量 ANTHROPIC_API_KEY）。
#使用示例：
#ANTHROPIC_API_KEY
#source .venv/bin/activate        # 若尚未激活虚拟环境
#export ANTHROPIC_API_KEY=sk-...  # 替换成自己的 Key
#python Create-an-agent.py