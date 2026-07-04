from backend.context.context_manager import ContextManager
from backend.llm.prompt_builder import PromptBuilder
from backend.llm.ollama_client import OllamaClient
from backend.models.event import Event


class EventHandler:

    def __init__(
        self,
        context_manager: ContextManager,
        llm: OllamaClient,
    ):
        self.context_manager = context_manager
        self.prompt_builder = PromptBuilder()
        self.llm = llm

    def handle(self, event: Event):

        context = self.context_manager.build_context(event)

        prompt = self.prompt_builder.build(event, context)

        response = self.llm.generate(prompt)

        print(response)