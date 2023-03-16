from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from leapmlapi import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateInferenceDto:
    prompt: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('prompt') }})
    enhance_prompt: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enhancePrompt'), 'exclude': lambda f: f is None }})
    height: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('height'), 'exclude': lambda f: f is None }})
    negative_prompt: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('negativePrompt'), 'exclude': lambda f: f is None }})
    number_of_images: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('numberOfImages'), 'exclude': lambda f: f is None }})
    prompt_strength: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('promptStrength'), 'exclude': lambda f: f is None }})
    restore_faces: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('restoreFaces'), 'exclude': lambda f: f is None }})
    seed: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('seed'), 'exclude': lambda f: f is None }})
    steps: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('steps'), 'exclude': lambda f: f is None }})
    version: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('version'), 'exclude': lambda f: f is None }})
    webhook_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('webhookUrl'), 'exclude': lambda f: f is None }})
    width: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('width'), 'exclude': lambda f: f is None }})
    