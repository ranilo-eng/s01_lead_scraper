from schemas.request_schema import LeadScraperRequest
from schemas.response_schema import LeadScraperResponse
from agent import LeadScraperAgent
from pydantic import ValidationError

def handle_request(payload: dict):
    try:
        request = LeadScraperRequest(**payload)
    except ValidationError as e:
        return LeadScraperResponse(
            status="ERROR",
            errors=e.errors()
        ).dict()

    agent = LeadScraperAgent()

    try:
        response = agent.run(request.file_path)
        return response.dict()
    except Exception as e:
        return LeadScraperResponse(
            status="ERROR",
            errors=[{"message": str(e)}]
        ).dict()


if __name__ == "__main__":
    result = handle_request({
        "file_path": "data/apollo_sample.csv"
    })
    print(result)
