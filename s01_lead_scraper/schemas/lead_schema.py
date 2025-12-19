from pydantic import BaseModel
from typing import List, Optional

class Lead(BaseModel):
    prospect_name: Optional[str]
    title: Optional[str]
    company_name: Optional[str]
    email: Optional[str]
    linkedin_url: Optional[str]
    company_size: Optional[str]
    industry: Optional[str]
    country: Optional[str]

class LeadScraperResponse(BaseModel):
    status: str
    lead_data_array: List[Lead]
