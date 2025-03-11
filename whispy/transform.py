from openai import OpenAI
from typing_extensions import Protocol


class Transformer(Protocol):
    def __call__(self, msg: str) -> str: ...


class AiTransformer:
    def __init__(
        self, client: OpenAI, name: str, priority: int, system_prompt: str,
    ) -> None:
        self._client = client
        self._prompt = system_prompt
        self._name = name
        self._priority = priority

    def __call__(self, msg: str) -> str:
        response = self._client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": self._prompt},
                {"role": "user", "content": msg},
            ],
        )
        return response.choices[0].message.content  # type: ignore


class Translator(AiTransformer):
    def __init__(self, client: OpenAI, language: str) -> None:
        super().__init__(
            client,
            f"Translator ({language})",
            100,
            f"You are a translator. You should translate the input text to from english to {language}. You should only output the translated text and nothing else.",
        )


class Emailer(AiTransformer):
    def __init__(self, client: OpenAI) -> None:
        super().__init__(
            client,
            "Emailer",
            50,
            "You are a personal assistant. You should take input text and write a professional sounding email with it. Only output the contents of the email and nothing else.",
        )
