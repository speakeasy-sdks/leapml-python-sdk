import dataclasses



@dataclasses.dataclass
class SchemeBearer:
    authorization: str = dataclasses.field(metadata={'security': { 'field_name': 'Authorization' }})
    