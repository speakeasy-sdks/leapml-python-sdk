import dataclasses
from ..shared import editentity as shared_editentity
from ..shared import security as shared_security
from dataclasses_json import dataclass_json
from leapmlapi import utils
from typing import Optional


@dataclass_json
@dataclasses.dataclass
class EditControllerCreateRequestBodyBody:
    prompt: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('prompt') }})
    image_guidance_scale: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('imageGuidanceScale') }})
    seed: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('seed') }})
    steps: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('steps') }})
    text_guidance_scale: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('textGuidanceScale') }})
    webhook_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('webhookUrl') }})
    

@dataclasses.dataclass
class EditControllerCreateRequestBodyFiles:
    content: bytes = dataclasses.field(metadata={'multipart_form': { 'content': True }})
    files: str = dataclasses.field(metadata={'multipart_form': { 'field_name': 'files' }})
    

@dataclasses.dataclass
class EditControllerCreateRequestBody:
    body: EditControllerCreateRequestBodyBody = dataclasses.field(metadata={'multipart_form': { 'field_name': 'body', 'json': True }})
    files: EditControllerCreateRequestBodyFiles = dataclasses.field(metadata={'multipart_form': { 'file': True }})
    

@dataclasses.dataclass
class EditControllerCreateSecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer' }})
    

@dataclasses.dataclass
class EditControllerCreateRequest:
    request: EditControllerCreateRequestBody = dataclasses.field(metadata={'request': { 'media_type': 'multipart/form-data' }})
    security: EditControllerCreateSecurity = dataclasses.field()
    

@dataclasses.dataclass
class EditControllerCreateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    edit_entity: Optional[shared_editentity.EditEntity] = dataclasses.field(default=None)
    