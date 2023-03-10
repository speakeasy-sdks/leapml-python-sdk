from __future__ import annotations
import dataclasses
from ..shared import inferenceentity as shared_inferenceentity
from ..shared import security as shared_security
from typing import Optional


@dataclasses.dataclass
class InferencesControllerFindOnePathParams:
    inference_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'inferenceId', 'style': 'simple', 'explode': False }})
    model_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'modelId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class InferencesControllerFindOneSecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer' }})
    

@dataclasses.dataclass
class InferencesControllerFindOneRequest:
    path_params: InferencesControllerFindOnePathParams = dataclasses.field()
    security: InferencesControllerFindOneSecurity = dataclasses.field()
    

@dataclasses.dataclass
class InferencesControllerFindOneResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    inference_entity: Optional[shared_inferenceentity.InferenceEntity] = dataclasses.field(default=None)
    