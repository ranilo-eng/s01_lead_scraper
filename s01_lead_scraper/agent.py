from tools.csv_loader import load_leads_from_csv

class LeadScraperAgent:
    """
    Core deterministic business logic.
    NO FastAPI
    NO Agno
    NO HTTP
    """

    def run(self, file_path: str) -> list[dict]:
        leads = load_leads_from_csv(file_path)
        return leads
