"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from leapmlapi import utils
from marshmallow import fields


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class InferenceEntity:
    r"""Returns the newly created inference."""
    
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdAt'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})

    height: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('height') }})

    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})

    images: list[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('images') }})

    model_id: list[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modelId') }})

    negative_prompt: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('negativePrompt') }})

    number_of_images: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('numberOfImages') }})

    prompt: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('prompt') }})

    prompt_strength: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('promptStrength') }})

    seed: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('seed') }})

    state: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('state') }})

    steps: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('steps') }})

    upscaling_option: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('upscalingOption') }})

    width: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('width') }})

    