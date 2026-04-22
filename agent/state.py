from pydantic import BaseModel
from typing import Optional, List

class AgentState(BaseModel):
    messages: List[str] = []
    intent: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
    platform: Optional[str] = None
    stage: str = "start"