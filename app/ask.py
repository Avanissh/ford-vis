from app.vectorstore import load_index, search
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

index, texts = load_index()


def ask_question(query):
    # Step 1: Retrieve context
    results = search(query, index, texts)
    context = "\n".join(results)

    # Step 2: Prompt (STRICT grounding)
    prompt = f"""
You are a STRICT automotive assistant.

You MUST follow these rules:
- ONLY use the information provided in the context
- DO NOT use any external knowledge
- DO NOT mention any vehicles not present in the context
- If the answer is not clearly in the context, respond EXACTLY with:
"I don't have enough information."

Context:
{context}

Question:
{query}
"""

    # Step 3: LLM call
    model_name = os.getenv("MODEL_NAME", "llama-3.1-8b-instant")
    response = client.chat.completions.create(
        model=model_name,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1
    )

    return response.choices[0].message.content