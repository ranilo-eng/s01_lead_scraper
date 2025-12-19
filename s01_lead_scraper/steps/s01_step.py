from agent import LeadScraperAgent

def s01_lead_scraper_step(context: dict) -> dict:
    """
    Agno step.
    One responsibility: execute S01 lead scraping.
    """
    file_path = context["file_path"]

    agent = LeadScraperAgent()
    result = agent.run(file_path)

    return result
