import dataclasses
from ..shared import modelversionentity as shared_modelversionentity
from ..shared import security as shared_security
from ..shared import trainmodeldto as shared_trainmodeldto
from typing import Optional


@dataclasses.dataclass
class ModelsControllerQueuePathParams:
    model_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'modelId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ModelsControllerQueueSecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer' }})
    

@dataclasses.dataclass
class ModelsControllerQueueRequest:
    path_params: ModelsControllerQueuePathParams = dataclasses.field()
    security: ModelsControllerQueueSecurity = dataclasses.field()
    request: Optional[shared_trainmodeldto.TrainModelDto] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class ModelsControllerQueueResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    model_version_entity: Optional[shared_modelversionentity.ModelVersionEntity] = dataclasses.field(default=None)
    