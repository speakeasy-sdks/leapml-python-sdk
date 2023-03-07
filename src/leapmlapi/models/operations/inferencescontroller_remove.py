from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import security as shared_security
from typing import Optional


@dataclasses.dataclass
class InferencesControllerRemoveSecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer' }})
    

@dataclasses.dataclass
class InferencesControllerRemovePathParams:
    inference_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'inferenceId', 'style': 'simple', 'explode': False }})
    model_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'modelId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class InferencesControllerRemoveRequest:
    path_params: InferencesControllerRemovePathParams = dataclasses.field()
    security: InferencesControllerRemoveSecurity = dataclasses.field()
    

@dataclasses.dataclass
class InferencesControllerRemoveResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    