from openai import OpenAI
from typing_extensions import Protocol


class Transformer(Protocol):
    def __call__(self, msg: str) -> str: ...


class AiTransformer:
    def __init__(
        self,
        client: OpenAI,
        system_prompt: str,
    ) -> None:
        self._client = client
        self._prompt = system_prompt

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
    def __init__(self, client: OpenAI, from_lang: str, to_lang: str) -> None:
        super().__init__(
            client,
            f"You are a translator. You should translate the input text to from {from_lang} to {to_lang}. You should only output the translated text and nothing else.",
        )


class Emailer(AiTransformer):
    def __init__(self, client: OpenAI) -> None:
        super().__init__(
            client,
            "You are a personal assistant. You should take input text and write a professional sounding email with it. Only output the contents of the email and nothing else.",
        )
