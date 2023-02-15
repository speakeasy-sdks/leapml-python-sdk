<!-- Start SDK Example Usage -->
```python
import leapmlapi
from leapmlapi.models import operations, shared

s = leapmlapi.LeapMLAPI()
   
req = operations.SamplesControllerCreateRequest(
    security=operations.SamplesControllerCreateSecurity(
        bearer=shared.SchemeBearer(
            authorization="Bearer YOUR_BEARER_TOKEN_HERE",
        ),
    ),
    path_params=operations.SamplesControllerCreatePathParams(
        model_id="unde",
    ),
    request=operations.SamplesControllerCreateRequestBody(
        files=operations.SamplesControllerCreateRequestBodyFiles(
            content="deserunt".encode(),
            files="porro",
        ),
    ),
)
    
res = s.fine_tuning.samples_controller_create(req)

if res.training_sample_entity is not None:
    # handle response
```
<!-- End SDK Example Usage -->