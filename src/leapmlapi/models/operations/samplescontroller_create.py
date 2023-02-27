from __future__ import annotations
import dataclasses
from ..shared import security as shared_security
from ..shared import trainingsampleentity as shared_trainingsampleentity
from typing import Optional


@dataclasses.dataclass
class SamplesControllerCreatePathParams:
    model_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'modelId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class SamplesControllerCreateRequestBodyFiles:
    content: bytes = dataclasses.field(metadata={'multipart_form': { 'content': True }})
    files: str = dataclasses.field(metadata={'multipart_form': { 'field_name': 'files' }})
    

@dataclasses.dataclass
class SamplesControllerCreateRequestBody:
    files: Optional[SamplesControllerCreateRequestBodyFiles] = dataclasses.field(default=None, metadata={'multipart_form': { 'file': True }})
    

@dataclasses.dataclass
class SamplesControllerCreateSecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer' }})
    

@dataclasses.dataclass
class SamplesControllerCreateRequest:
    path_params: SamplesControllerCreatePathParams = dataclasses.field()
    request: SamplesControllerCreateRequestBody = dataclasses.field(metadata={'request': { 'media_type': 'multipart/form-data' }})
    security: SamplesControllerCreateSecurity = dataclasses.field()
    

@dataclasses.dataclass
class SamplesControllerCreateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    training_sample_entity: Optional[shared_trainingsampleentity.TrainingSampleEntity] = dataclasses.field(default=None)
    