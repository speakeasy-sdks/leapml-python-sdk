import dataclasses
from ..shared import createmodeldto as shared_createmodeldto
from ..shared import modelentity as shared_modelentity
from ..shared import security as shared_security
from typing import Optional


@dataclasses.dataclass
class ModelsControllerCreateSecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer' }})
    

@dataclasses.dataclass
class ModelsControllerCreateRequest:
    request: shared_createmodeldto.CreateModelDto = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    security: ModelsControllerCreateSecurity = dataclasses.field()
    

@dataclasses.dataclass
class ModelsControllerCreateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    model_entity: Optional[shared_modelentity.ModelEntity] = dataclasses.field(default=None)
    