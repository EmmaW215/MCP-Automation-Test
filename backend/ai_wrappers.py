from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from typing import Dict

"""
Utility wrappers that expose simple functions to call different back-end LLMs.

Functions
---------
run_llama2(prompt: str) -> str
    Invoke local Ollama server with the `llama2` model.
run_claude(prompt: str) -> str
    Invoke Anthropic Claude via LangChain Agent (requires ANTHROPIC_API_KEY).
"""

# --------------- Ollama (local) -------------------------------------------
_llama_chat = ChatOllama(model="llama2")

def run_llama2(user_prompt: str) -> str:
    """Call local Ollama Llama-2 model and return the assistant response."""
    return _llama_chat.invoke(user_prompt)

# --------------- Claude (Anthropic) --------------------------------------
# Simple toy tool for the agent
def _get_weather(city: str) -> str:
    """Dummy weather tool used by the Claude agent."""
    return f"It's always sunny in {city}!"

_claude_agent = create_agent(
    model="anthropic:claude-sonnet-4-5",
    tools=[_get_weather],
    system_prompt="You are a helpful assistant",
)

def run_claude(user_prompt: str) -> str:
    """Call Claude via LangChain Agent and return the assistant response."""
    result: Dict = _claude_agent.invoke(
        {"messages": [{"role": "user", "content": user_prompt}]}
    )
    # Depending on LangChain version, `invoke` may return dict / string.
    return str(result)
