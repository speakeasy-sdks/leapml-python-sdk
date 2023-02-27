from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from leapmlapi import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ModelEntity:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    subject_identifier: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('subjectIdentifier') }})
    subject_keyword: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('subjectKeyword') }})
    title: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('title') }})
    