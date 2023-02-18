import dataclasses
from ..shared import editentity as shared_editentity
from ..shared import security as shared_security
from dataclasses_json import dataclass_json
from leapmlapi import utils
from typing import Optional


@dataclass_json
@dataclasses.dataclass
class EditControllerCreateWithURLRequestBody:
    image_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('imageUrl') }})
    prompt: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('prompt') }})
    image_guidance_scale: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('imageGuidanceScale') }})
    seed: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('seed') }})
    steps: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('steps') }})
    text_guidance_scale: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('textGuidanceScale') }})
    webhook_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('webhookUrl') }})
    

@dataclasses.dataclass
class EditControllerCreateWithURLSecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer' }})
    

@dataclasses.dataclass
class EditControllerCreateWithURLRequest:
    request: EditControllerCreateWithURLRequestBody = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    security: EditControllerCreateWithURLSecurity = dataclasses.field()
    

@dataclasses.dataclass
class EditControllerCreateWithURLResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    edit_entity: Optional[shared_editentity.EditEntity] = dataclasses.field(default=None)
    