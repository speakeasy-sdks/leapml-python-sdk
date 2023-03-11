from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import modelversionentity as shared_modelversionentity
from ..shared import security as shared_security
from typing import Optional


@dataclasses.dataclass
class VersionsControllerFindOneSecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer' }})
    

@dataclasses.dataclass
class VersionsControllerFindOnePathParams:
    model_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'modelId', 'style': 'simple', 'explode': False }})
    version_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'versionId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class VersionsControllerFindOneRequest:
    path_params: VersionsControllerFindOnePathParams = dataclasses.field()
    security: VersionsControllerFindOneSecurity = dataclasses.field()
    

@dataclasses.dataclass
class VersionsControllerFindOneResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    model_version_entity: Optional[shared_modelversionentity.ModelVersionEntity] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    