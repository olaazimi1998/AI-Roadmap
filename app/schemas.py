from pydantic import BaseModel, Field

class CustomerData(BaseModel):
    tenure_months: int = Field(ge=0)
    monthly_charges: float = Field(ge=0)
    support_calls: int = Field(ge=0)