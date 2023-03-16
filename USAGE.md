<!-- Start SDK Example Usage -->
```python
import leapmlapi
from leapmlapi.models import operations, shared

s = leapmlapi.LeapMLAPI()

   
req = operations.ModelsControllerRemoveRequest(
    security=operations.ModelsControllerRemoveSecurity(
        bearer=shared.SchemeBearer(
            authorization="Bearer YOUR_BEARER_TOKEN_HERE",
        ),
    ),
    path_params=operations.ModelsControllerRemovePathParams(
        model_id="unde",
    ),
)
    
res = s.fine_tuning.models_controller_remove(req)

if res.status_code == 200:
    # handle response
```
<!-- End SDK Example Usage -->