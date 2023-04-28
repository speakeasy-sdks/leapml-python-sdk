"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import modelentity as shared_modelentity
from typing import Optional


@dataclasses.dataclass
class RetrieveSingleModelSecurity:
    
    bearer: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})

    

@dataclasses.dataclass
class RetrieveSingleModelRequest:
    
    model_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'modelId', 'style': 'simple', 'explode': False }})

    r"""The ID of the model to retrieve."""
    

@dataclasses.dataclass
class RetrieveSingleModelResponse:
    
    content_type: str = dataclasses.field()

    status_code: int = dataclasses.field()

    model_entity: Optional[shared_modelentity.ModelEntity] = dataclasses.field(default=None)

    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)

    