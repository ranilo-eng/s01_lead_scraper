# S01 Lead Scraper Agent

A deterministic, API-driven lead scraping service designed for workflow automation (n8n) with a clean upgrade path to AI-agent orchestration (Agno).

---

## 1. Purpose

The **S01 Lead Scraper Agent** processes lead-generation requests and returns **structured lead data** in a stable JSON format.

This MVP is intentionally **non-AI**, **deterministic**, and **workflow-friendly**, ensuring:

- Predictable output  
- Easy debugging  
- Seamless n8n integration  
- Future AI enablement without breaking changes  

---

## 2. Key Design Decisions

### Why Apollo UI + CSV (MVP)
- Apollo API is **not required** for MVP validation  
- CSV export is **stable, auditable, and cost-free**  
- Prevents vendor lock-in  
- Keeps business logic independent of data sources  

### Why Not Agno (Yet)
Agno is designed for **reasoning, decision-making, and multi-step AI workflows**.

This MVP:
- Does not require reasoning  
- Must remain deterministic  
- Must be easy to test and explain  

Agno is intentionally **deferred to Phase 2**.

---

## 3. Architecture (Phase 1 – MVP)

Client / n8n  
→ FastAPI (API Layer)  
→ LeadScraperAgent (Core Business Logic)  
→ CSV Loader (Apollo UI export)

---

## 4. Project Structure

```
s01_lead_scraper/
├── api.py
├── agent.py
├── main.py
├── s01_agno_agent.py
├── data/
│   └── apollo_sample.csv
├── schemas/
│   ├── request_schema.py
│   ├── response_schema.py
│   └── lead_schema.py
├── tools/
│   └── csv_loader.py
├── test_workflow.py
├── .env
├── requirements.txt
└── README.md
```

---

## 5. API Contract

### Endpoint
```
POST /leads/s01
```

### Request Body
```json
{
  "client_id": "client_001",
  "target_count": 100,
  "search_criteria": {
    "industry": "Fintech",
    "employee_range": "100-500",
    "title_keywords": ["VP of Engineering"]
  }
}
```

### Response Body
```json
{
  "status": "SUCCESS",
  "lead_data_array": [
    {
      "prospect_name": "Priyal Shrimali",
      "company_name": "HiLabs",
      "title": "Software Development Engineer",
      "email": "priyal.shrimali@hilabs.com",
      "linkedin_url": "http://www.linkedin.com/in/priyalshrimali",
      "company_size": "310",
      "industry": "information technology & services",
      "country": "United States"
    }
  ],
  "errors": []
}
```

---

## 6. Installation

```bash
python -m venv agno-venv
source agno-venv/Scripts/activate
pip install -r requirements.txt
```

### requirements.txt
```
fastapi
uvicorn
pydantic
pandas
python-dotenv
ango
```

---

## 7. Run the API

```bash
uvicorn api:app --reload
```

Server URL:
```
http://127.0.0.1:8000
```

---

## 8. API Documentation

- Swagger UI: http://127.0.0.1:8000/docs  
- OpenAPI JSON: http://127.0.0.1:8000/openapi.json  

---

## 9. Local Workflow Test (No API)

```bash
python test_workflow.py
```

---

## 10. n8n Integration

- Method: POST  
- URL: `/leads/s01`  
- Body: JSON  

---

## 11. Phase 2 – Agno Integration (Planned)

Agno will be added as a **reasoning layer only**, without modifying the API or core logic.

Capabilities:
- Lead ranking and scoring
- Intelligent filtering
- Data enrichment orchestration

---

## 12. Summary

- Deterministic MVP  
- Stable API contract  
- Workflow-first  
- AI-ready architecture  
