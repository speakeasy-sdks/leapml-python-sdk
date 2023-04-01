<!-- Start SDK Example Usage -->
```python
import leapmlapi
from leapmlapi.models import operations, shared

s = leapmlapi.LeapMLAPI()


req = operations.ModelsControllerRemoveRequest(
    model_id="corrupti",
)
    
res = s.fine_tuning.models_controller_remove(req, operations.ModelsControllerRemoveSecurity(
    bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.status_code == 200:
    # handle response
```
<!-- End SDK Example Usage -->