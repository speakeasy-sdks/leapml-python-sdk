import dataclasses
from ..shared import editentity as shared_editentity
from ..shared import security as shared_security
from typing import Optional


@dataclasses.dataclass
class EditControllerFindOnePathParams:
    edit_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'editId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class EditControllerFindOneSecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer' }})
    

@dataclasses.dataclass
class EditControllerFindOneRequest:
    path_params: EditControllerFindOnePathParams = dataclasses.field()
    security: EditControllerFindOneSecurity = dataclasses.field()
    

@dataclasses.dataclass
class EditControllerFindOneResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    edit_entity: Optional[shared_editentity.EditEntity] = dataclasses.field(default=None)
    