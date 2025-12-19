from pydantic import BaseModel
from typing import List, Optional

class SearchCriteria(BaseModel):
    industry: Optional[str]
    employee_range: Optional[str]
    title_keywords: Optional[List[str]]

class LeadScraperRequest(BaseModel):
    client_id: str
    target_count: int
    search_criteria: SearchCriteria
