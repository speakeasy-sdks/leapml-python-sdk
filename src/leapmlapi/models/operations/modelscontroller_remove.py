from __future__ import annotations
import dataclasses
import requests
from ..shared import security as shared_security
from typing import Optional


@dataclasses.dataclass
class ModelsControllerRemoveSecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer' }})
    

@dataclasses.dataclass
class ModelsControllerRemovePathParams:
    model_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'modelId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ModelsControllerRemoveRequest:
    path_params: ModelsControllerRemovePathParams = dataclasses.field()
    security: ModelsControllerRemoveSecurity = dataclasses.field()
    

@dataclasses.dataclass
class ModelsControllerRemoveResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests.Response] = dataclasses.field(default=None)
    