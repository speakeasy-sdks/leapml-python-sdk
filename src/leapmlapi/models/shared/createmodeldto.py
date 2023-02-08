import dataclasses
from dataclasses_json import dataclass_json
from leapmlapi import utils
from typing import Optional


@dataclass_json
@dataclasses.dataclass
class CreateModelDto:
    subject_keyword: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('subjectKeyword') }})
    title: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('title') }})
    subject_identifier: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('subjectIdentifier') }})
    