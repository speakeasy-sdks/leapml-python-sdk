from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from leapmlapi import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UploadSamplesViaURLDto:
    images: list[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('images') }})
    