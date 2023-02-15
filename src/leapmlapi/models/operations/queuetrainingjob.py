import dataclasses
from ..shared import modelversionentity as shared_modelversionentity
from ..shared import security as shared_security
from ..shared import trainmodeldto as shared_trainmodeldto
from typing import Optional


@dataclasses.dataclass
class QueueTrainingJobPathParams:
    model_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'modelId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class QueueTrainingJobSecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer' }})
    

@dataclasses.dataclass
class QueueTrainingJobRequest:
    path_params: QueueTrainingJobPathParams = dataclasses.field()
    security: QueueTrainingJobSecurity = dataclasses.field()
    request: Optional[shared_trainmodeldto.TrainModelDto] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class QueueTrainingJobResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    model_version_entity: Optional[shared_modelversionentity.ModelVersionEntity] = dataclasses.field(default=None)
    