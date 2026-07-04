import httpx

from backend.core.config import settings


class OllamaClient:

    def __init__(self):
        self.base_url = settings.ollama_url
        self.model = settings.model_name

    def generate(self, prompt: str) -> str:

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }

        response = httpx.post(
            f"{self.base_url}/api/generate",
            json=payload,
            timeout=120
        )

        response.raise_for_status()

        return response.json()["response"]