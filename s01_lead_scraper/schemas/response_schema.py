from pydantic import BaseModel
from typing import Optional, List

class Lead(BaseModel):
    prospect_name: Optional[str] = None
    title: Optional[str] = None
    company_name: Optional[str] = None
    email: Optional[str] = None
    linkedin_url: Optional[str] = None
    company_size: Optional[str] = None
    industry: Optional[str] = None
    country: Optional[str] = None


class LeadScraperResponse(BaseModel):
    status: str
    lead_data_array: List[Lead] = []
    errors: Optional[list] = None
