"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import modelentity as shared_modelentity
from typing import Optional


@dataclasses.dataclass
class CreateModelSecurity:
    
    bearer: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})  
    

@dataclasses.dataclass
class CreateModelResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    model_entity: Optional[shared_modelentity.ModelEntity] = dataclasses.field(default=None)
    r"""The model has been successfully created."""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    