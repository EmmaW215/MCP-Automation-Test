import gradio as gr
from backend.ai_wrappers import run_llama2, run_claude


def chat(model_name: str, user_input: str):
    """Route the user prompt to the chosen backend model."""
    if not user_input.strip():
        return ""
    return run_llama2(user_input) if model_name == "Ollama-Llama2" else run_claude(user_input)


def build_interface():
    with gr.Blocks(title="Proxy AI-Agent Demo") as demo:
        gr.Markdown("# 🛰️ Proxy AI-Agent · LangChain + Ollama + Claude")
        model_sel = gr.Radio([
            "Ollama-Llama2",
            "Claude-Sonnet",
        ], value="Ollama-Llama2", label="Choose backend model")

        chat_box = gr.Chatbot(height=400)
        user_txt = gr.Textbox(scale=4, placeholder="Ask me anything…")
        send_btn = gr.Button("Send", scale=1)

        # ---------- helper callbacks ----------
        def user_send(msg, history):
            history = history + [[msg, None]]
            return "", history

        def bot_reply(history, model_name):
            user_msg = history[-1][0]
            answer = chat(model_name, user_msg)
            history[-1][1] = answer
            return history

        user_txt.submit(user_send, [user_txt, chat_box], [user_txt, chat_box])
        send_btn.click(user_send, [user_txt, chat_box], [user_txt, chat_box])
        chat_box.change(bot_reply, [chat_box, model_sel], chat_box)

    return demo


if __name__ == "__main__":
    app = build_interface()
    app.launch(server_name="0.0.0.0", server_port=7860)
