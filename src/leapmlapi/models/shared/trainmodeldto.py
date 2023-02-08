import dataclasses
from dataclasses_json import dataclass_json
from leapmlapi import utils
from typing import Optional


@dataclass_json
@dataclasses.dataclass
class TrainModelDto:
    webhook_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('webhookUrl') }})
    