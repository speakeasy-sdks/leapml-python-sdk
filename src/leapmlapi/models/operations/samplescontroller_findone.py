from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import security as shared_security
from ..shared import trainingsampleentity as shared_trainingsampleentity
from typing import Optional


@dataclasses.dataclass
class SamplesControllerFindOneSecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer' }})
    

@dataclasses.dataclass
class SamplesControllerFindOnePathParams:
    model_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'modelId', 'style': 'simple', 'explode': False }})
    sample_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'sampleId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class SamplesControllerFindOneRequest:
    path_params: SamplesControllerFindOnePathParams = dataclasses.field()
    security: SamplesControllerFindOneSecurity = dataclasses.field()
    

@dataclasses.dataclass
class SamplesControllerFindOneResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    training_sample_entities: Optional[list[shared_trainingsampleentity.TrainingSampleEntity]] = dataclasses.field(default=None)
    