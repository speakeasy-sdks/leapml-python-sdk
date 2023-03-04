from __future__ import annotations
import dataclasses
import requests
from ..shared import security as shared_security
from ..shared import trainingsampleentity as shared_trainingsampleentity
from typing import Optional


@dataclasses.dataclass
class SamplesControllerFindAllSecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer' }})
    

@dataclasses.dataclass
class SamplesControllerFindAllPathParams:
    model_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'modelId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class SamplesControllerFindAllRequest:
    path_params: SamplesControllerFindAllPathParams = dataclasses.field()
    security: SamplesControllerFindAllSecurity = dataclasses.field()
    

@dataclasses.dataclass
class SamplesControllerFindAllResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests.Response] = dataclasses.field(default=None)
    training_sample_entities: Optional[list[shared_trainingsampleentity.TrainingSampleEntity]] = dataclasses.field(default=None)
    