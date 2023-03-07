from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import createinferencedto as shared_createinferencedto
from ..shared import inferenceentity as shared_inferenceentity
from ..shared import security as shared_security
from typing import Optional


@dataclasses.dataclass
class InferencesControllerCreateSecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer' }})
    

@dataclasses.dataclass
class InferencesControllerCreatePathParams:
    model_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'modelId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class InferencesControllerCreateRequest:
    path_params: InferencesControllerCreatePathParams = dataclasses.field()
    request: shared_createinferencedto.CreateInferenceDto = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    security: InferencesControllerCreateSecurity = dataclasses.field()
    

@dataclasses.dataclass
class InferencesControllerCreateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    inference_entity: Optional[shared_inferenceentity.InferenceEntity] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    