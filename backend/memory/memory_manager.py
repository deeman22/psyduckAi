from memory.session_memory import SessionMemory

class MemoryManager:

    def __init__(self):
        self.memory = SessionMemory()

    def update_branch(self, branch: str):
        self.memory.current_branch = branch

    def add_error(self, error: str):
        self.memory.add_error(error)

    def get_context(self):
        return self.memory