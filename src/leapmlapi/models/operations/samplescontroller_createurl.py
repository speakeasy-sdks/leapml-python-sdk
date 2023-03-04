from __future__ import annotations
import dataclasses
import requests
from ..shared import security as shared_security
from ..shared import trainingsampleentity as shared_trainingsampleentity
from ..shared import uploadsamplesviaurldto as shared_uploadsamplesviaurldto
from typing import Optional


@dataclasses.dataclass
class SamplesControllerCreateURLSecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer' }})
    

@dataclasses.dataclass
class SamplesControllerCreateURLPathParams:
    model_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'modelId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class SamplesControllerCreateURLQueryParams:
    return_in_object: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'returnInObject', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class SamplesControllerCreateURLRequest:
    path_params: SamplesControllerCreateURLPathParams = dataclasses.field()
    query_params: SamplesControllerCreateURLQueryParams = dataclasses.field()
    request: shared_uploadsamplesviaurldto.UploadSamplesViaURLDto = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    security: SamplesControllerCreateURLSecurity = dataclasses.field()
    

@dataclasses.dataclass
class SamplesControllerCreateURLResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests.Response] = dataclasses.field(default=None)
    training_sample_entity: Optional[shared_trainingsampleentity.TrainingSampleEntity] = dataclasses.field(default=None)
    