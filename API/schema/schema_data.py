from pydantic import BaseModel
from typing import List,Dict,Optional

class PopulateTable(BaseModel):
    table_name:str
    data: List[Dict[str,Optional[int|str|float]]]

    class Config:
        from_attributes = True

class ResponseModel(BaseModel):
    table_name:Optional[str]
    count:Optional[int]