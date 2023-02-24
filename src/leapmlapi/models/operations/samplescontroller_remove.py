from __future__ import annotations
import dataclasses
from ..shared import security as shared_security
from ..shared import trainingsampleentity as shared_trainingsampleentity
from typing import Optional


@dataclasses.dataclass
class SamplesControllerRemovePathParams:
    model_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'modelId', 'style': 'simple', 'explode': False }})
    sample_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'sampleId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class SamplesControllerRemoveSecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer' }})
    

@dataclasses.dataclass
class SamplesControllerRemoveRequest:
    path_params: SamplesControllerRemovePathParams = dataclasses.field()
    security: SamplesControllerRemoveSecurity = dataclasses.field()
    

@dataclasses.dataclass
class SamplesControllerRemoveResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    training_sample_entity: Optional[shared_trainingsampleentity.TrainingSampleEntity] = dataclasses.field(default=None)
    