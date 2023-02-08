<!-- Start SDK Example Usage -->
```python
import leapmlapi
from leapmlapi.models import operations, shared

s = leapmlapi.LeapMLAPI()
   
req = operations.ModelsControllerCreateRequest(
    security=operations.ModelsControllerCreateSecurity(
        bearer=shared.SchemeBearer(
            authorization="Bearer YOUR_BEARER_TOKEN_HERE",
        ),
    ),
    request=shared.CreateModelDto(
        subject_identifier="unde",
        subject_keyword="deserunt",
        title="porro",
    ),
)
    
res = s.fine_tuning.models_controller_create(req)

if res.model_entity is not None:
    # handle response
```
<!-- End SDK Example Usage -->