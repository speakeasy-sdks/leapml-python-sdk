import dataclasses
import dateutil.parser
from ..shared import modelentity as shared_modelentity
from ..shared import weightsentity as shared_weightsentity
from dataclasses_json import dataclass_json
from datetime import datetime
from enum import Enum
from leapmlapi import utils
from marshmallow import fields

class ModelVersionEntityStatusEnum(str, Enum):
    QUEUED = "queued"
    PROCESSING = "processing"
    FINISHED = "finished"
    FAILED = "failed"


@dataclass_json
@dataclasses.dataclass
class ModelVersionEntity:
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('createdAt'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    model: shared_modelentity.ModelEntity = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('model') }})
    status: ModelVersionEntityStatusEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('status') }})
    weights: shared_weightsentity.WeightsEntity = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('weights') }})
    