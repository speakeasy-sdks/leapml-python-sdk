from __future__ import annotations
import dataclasses
from ..shared import modelversionentity as shared_modelversionentity
from ..shared import security as shared_security
from typing import Optional


@dataclasses.dataclass
class VersionsControllerFindAllPathParams:
    model_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'modelId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class VersionsControllerFindAllSecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer' }})
    

@dataclasses.dataclass
class VersionsControllerFindAllRequest:
    path_params: VersionsControllerFindAllPathParams = dataclasses.field()
    security: VersionsControllerFindAllSecurity = dataclasses.field()
    

@dataclasses.dataclass
class VersionsControllerFindAllResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    model_version_entities: Optional[list[shared_modelversionentity.ModelVersionEntity]] = dataclasses.field(default=None)
    