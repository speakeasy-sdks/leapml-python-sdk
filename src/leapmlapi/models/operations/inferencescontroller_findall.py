from __future__ import annotations
import dataclasses
import requests
from ..shared import security as shared_security
from typing import Optional


@dataclasses.dataclass
class InferencesControllerFindAllSecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer' }})
    

@dataclasses.dataclass
class InferencesControllerFindAllPathParams:
    model_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'modelId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class InferencesControllerFindAllQueryParams:
    only_finished: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'onlyFinished', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class InferencesControllerFindAllRequest:
    path_params: InferencesControllerFindAllPathParams = dataclasses.field()
    query_params: InferencesControllerFindAllQueryParams = dataclasses.field()
    security: InferencesControllerFindAllSecurity = dataclasses.field()
    

@dataclasses.dataclass
class InferencesControllerFindAllResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests.Response] = dataclasses.field(default=None)
    