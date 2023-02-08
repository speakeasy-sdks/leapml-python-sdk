import dataclasses
from ..shared import modelentity as shared_modelentity
from ..shared import security as shared_security
from typing import Optional


@dataclasses.dataclass
class ModelsControllerFindOnePathParams:
    model_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'modelId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ModelsControllerFindOneSecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer' }})
    

@dataclasses.dataclass
class ModelsControllerFindOneRequest:
    path_params: ModelsControllerFindOnePathParams = dataclasses.field()
    security: ModelsControllerFindOneSecurity = dataclasses.field()
    

@dataclasses.dataclass
class ModelsControllerFindOneResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    model_entity: Optional[shared_modelentity.ModelEntity] = dataclasses.field(default=None)
    