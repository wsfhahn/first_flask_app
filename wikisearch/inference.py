from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam
from typing import TypedDict

class Config(TypedDict):
    model: str
    temperature: float
    top_p: float

def get_model_response(system: str, prompt: str, client: OpenAI, config: Config) -> str:
    if not prompt:
        raise ValueError("Prompt cannot be empty")
    
    messages: list[ChatCompletionMessageParam] = [
        {"role": "system", "content": system},
        {"role": "user", "content": prompt}
    ]

    try:
        response = client.chat.completions.create(
            model=config["model"],
            messages=messages,
            temperature=config["temperature"],
            top_p=config["top_p"]
        )

        if not response.choices[0].message.content:
            return "Model did not respond"
        
        return response.choices[0].message.content
    except Exception as e:
        return f"Failed to get model response: {str(e)}"

if __name__ == "__main__":
    import wikipedia
    from wikisearch.prompts import summarizer_system_prompt, summarizer_user_prompt

    client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")
    config = Config(
        model="gemma-3-270m-it",
        temperature=0.7,
        top_p=0.95
    )
    title = "Apollo 11"
    page = wikipedia.page(title)
    content = page.content[:12000]
    summary = get_model_response(
        summarizer_system_prompt,
        summarizer_user_prompt.format(title=title, content=content),
        client,
        config
    )
    print(summary)
