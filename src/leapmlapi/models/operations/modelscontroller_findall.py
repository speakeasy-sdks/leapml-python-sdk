import dataclasses
from ..shared import modelentity as shared_modelentity
from ..shared import security as shared_security
from typing import Optional


@dataclasses.dataclass
class ModelsControllerFindAllSecurity:
    bearer: Optional[shared_security.SchemeBearer] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer' }})
    bearer1: Optional[shared_security.SchemeBearer] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer' }})
    

@dataclasses.dataclass
class ModelsControllerFindAllRequest:
    security: ModelsControllerFindAllSecurity = dataclasses.field()
    

@dataclasses.dataclass
class ModelsControllerFindAllResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    model_entities: Optional[list[shared_modelentity.ModelEntity]] = dataclasses.field(default=None)
    