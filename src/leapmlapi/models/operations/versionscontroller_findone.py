"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import modelversionentity as shared_modelversionentity
from typing import Optional


@dataclasses.dataclass
class VersionsControllerFindOneSecurity:
    
    bearer: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class VersionsControllerFindOneRequest:
    
    model_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'modelId', 'style': 'simple', 'explode': False }})
    r"""The ID of the model to retrieve."""
    version_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'versionId', 'style': 'simple', 'explode': False }})
    r"""The ID of the version to retrieve."""
    

@dataclasses.dataclass
class VersionsControllerFindOneResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    model_version_entity: Optional[shared_modelversionentity.ModelVersionEntity] = dataclasses.field(default=None)
    r"""A version of a model."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    