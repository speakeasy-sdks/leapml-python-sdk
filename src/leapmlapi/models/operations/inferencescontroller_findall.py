import dataclasses
from ..shared import security as shared_security


@dataclasses.dataclass
class InferencesControllerFindAllPathParams:
    model_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'modelId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class InferencesControllerFindAllSecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer' }})
    

@dataclasses.dataclass
class InferencesControllerFindAllRequest:
    path_params: InferencesControllerFindAllPathParams = dataclasses.field()
    security: InferencesControllerFindAllSecurity = dataclasses.field()
    

@dataclasses.dataclass
class InferencesControllerFindAllResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    