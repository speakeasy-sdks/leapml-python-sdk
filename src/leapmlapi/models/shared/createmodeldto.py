from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from leapmlapi import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateModelDto:
    subject_keyword: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('subjectKeyword') }})
    title: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('title') }})
    subject_identifier: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('subjectIdentifier'), 'exclude': lambda f: f is None }})
    