import dataclasses
from dataclasses_json import dataclass_json
from leapmlapi import utils


@dataclass_json
@dataclasses.dataclass
class WeightsEntity:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    uri: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('uri') }})
    