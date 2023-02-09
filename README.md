# LeapML Python SDK

Generate images, edit them, fine tune models, and more with an easy-to-use API.

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install leapml
```
<!-- End SDK Installation -->

## Authentication

Signup for [access](https://www.leapml.dev/signup) to LeapML to use the API. 

## SDK Example Usage
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

<!-- Start SDK Available Operations -->
## SDK Available Operations


### fine_tuning

* `models_controller_create` - Create Model
* `models_controller_find_all` - List All Models
* `models_controller_find_one` - Retrieve a Single Model
* `models_controller_queue` - Queue Training Job
* `samples_controller_create` - Upload Image Samples
* `samples_controller_create_url` - Upload Image Samples Via Url
* `samples_controller_find_all` - List Image Samples
* `samples_controller_find_one` - Get Image Sample
* `samples_controller_remove` - Archive Image Sample
* `versions_controller_find_all` - List All Model Versions
* `versions_controller_find_one` - Get Model Version

### generating_images

* `inferences_controller_create` - Generate Image
* `inferences_controller_find_all` - List Inference Jobs
* `inferences_controller_find_one` - Get Single Inference Job
* `inferences_controller_remove` - Delete Inference

### image_editing

* `edit_controller_create` - Edit a photo
* `edit_controller_find_one` - Get an edit
<!-- End SDK Available Operations -->

### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
