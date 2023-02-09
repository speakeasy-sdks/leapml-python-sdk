import dataclasses
from dataclasses_json import dataclass_json
from leapmlapi import utils


@dataclass_json
@dataclasses.dataclass
class UploadSamplesViaURLDto:
    images: list[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('images') }})
    