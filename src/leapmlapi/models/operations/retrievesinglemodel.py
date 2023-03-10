from __future__ import annotations
import dataclasses
from ..shared import modelentity as shared_modelentity
from ..shared import security as shared_security
from typing import Optional


@dataclasses.dataclass
class RetrieveSingleModelPathParams:
    model_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'modelId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class RetrieveSingleModelSecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer' }})
    

@dataclasses.dataclass
class RetrieveSingleModelRequest:
    path_params: RetrieveSingleModelPathParams = dataclasses.field()
    security: RetrieveSingleModelSecurity = dataclasses.field()
    

@dataclasses.dataclass
class RetrieveSingleModelResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    model_entity: Optional[shared_modelentity.ModelEntity] = dataclasses.field(default=None)
    