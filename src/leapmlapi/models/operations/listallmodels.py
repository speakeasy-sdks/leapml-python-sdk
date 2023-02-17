import dataclasses
from ..shared import modelentity as shared_modelentity
from ..shared import security as shared_security
from typing import Optional


@dataclasses.dataclass
class ListAllModelsQueryParams:
    return_in_object: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'returnInObject', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class ListAllModelsSecurity:
    bearer: Optional[shared_security.SchemeBearer] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer' }})
    bearer1: Optional[shared_security.SchemeBearer] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer' }})
    

@dataclasses.dataclass
class ListAllModelsRequest:
    query_params: ListAllModelsQueryParams = dataclasses.field()
    security: ListAllModelsSecurity = dataclasses.field()
    

@dataclasses.dataclass
class ListAllModelsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    model_entities: Optional[list[shared_modelentity.ModelEntity]] = dataclasses.field(default=None)
    