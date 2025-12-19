from fastapi import FastAPI
from agent import LeadScraperAgent
from schemas.request_schema import LeadScraperRequest
from schemas.response_schema import LeadScraperResponse

app = FastAPI(title="S01 Lead Scraper Agent")

@app.post("/leads/s01", response_model=LeadScraperResponse)
def run_s01(payload: LeadScraperRequest):
    agent = LeadScraperAgent()

    try:
        # INTERNAL decision
        leads = agent.run(file_path="data/apollo_sample.csv")

        return LeadScraperResponse(
            status="SUCCESS",
            lead_data_array=leads,
            errors=[]
        )
    except Exception as e:
        return LeadScraperResponse(
            status="ERROR",
            lead_data_array=[],
            errors=[{"message": str(e)}]
        )
