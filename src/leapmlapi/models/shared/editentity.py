from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from leapmlapi import utils
from marshmallow import fields


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EditEntity:
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('createdAt'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    edited_image_uri: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('editedImageUri') }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    image_guidance_scale: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('imageGuidanceScale') }})
    project_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('projectId') }})
    prompt: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('prompt') }})
    source_image_uri: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('sourceImageUri') }})
    status: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('status') }})
    steps: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('steps') }})
    text_guidance_scale: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('textGuidanceScale') }})
    