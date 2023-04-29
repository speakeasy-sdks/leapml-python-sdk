"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import createinferencedto as shared_createinferencedto
from ..shared import inferenceentity as shared_inferenceentity
from typing import Optional


@dataclasses.dataclass
class InferencesControllerCreateSecurity:
    
    bearer: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class InferencesControllerCreateRequest:
    
    create_inference_dto: shared_createinferencedto.CreateInferenceDto = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    model_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'modelId', 'style': 'simple', 'explode': False }})
    r"""The ID of the model to use to generate images."""
    

@dataclasses.dataclass
class InferencesControllerCreateResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    inference_entity: Optional[shared_inferenceentity.InferenceEntity] = dataclasses.field(default=None)
    r"""Returns the newly created inference."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    