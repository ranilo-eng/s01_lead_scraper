from agent import LeadScraperAgent

class S01AgnoAgent:
    def __init__(self):
        self.core_agent = LeadScraperAgent()

    def run(self, payload):
        leads = self.core_agent.run(payload.file_path)
        return leads
