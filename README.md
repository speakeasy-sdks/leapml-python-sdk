# LeapML Python SDK

<div align="center">
   <p>Generate images, edit them, fine tune models, and more with an easy-to-use API.</p>
   <img src="https://img.shields.io/github/actions/workflow/status/speakeasy-sdks/leapml-python-sdk/speakeasy_sdk_generation.yml?style=for-the-badge" />
   <img src="https://img.shields.io/badge/pypi-1.0.0-blue?style=for-the-badge" />
   <img src="https://img.shields.io/badge/python-3.5 | 3.6 | 3.7 | 3.8-blue?style=for-the-badge" />
   <a href="https://docs.leapml.dev/reference/inferencescontroller_create-1"><img src="https://img.shields.io/static/v1?label=Docs&message=API Ref&color=000&style=for-the-badge" /></a>
   <a href="https://discord.com/channels/1065392526745403502/1065392527198404670"><img src="https://img.shields.io/static/v1?label=Discord&message=Join&color=7289da&style=for-the-badge" /></a>
</div>

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

<!-- Start SDK Available Operations -->
## SDK Available Operations


### fine_tuning

* `models_controller_remove` - Delete a Model
* `samples_controller_create` - Upload Image Samples
* `samples_controller_create_url` - Upload Image Samples Via Url
* `samples_controller_find_all` - List Image Samples
* `samples_controller_find_one` - Get Image Sample
* `samples_controller_remove` - Archive Image Sample
* `versions_controller_find_all` - List All Model Versions
* `versions_controller_find_one` - Get Model Version
* `create_model` - Create Model
* `list_all_models` - List All Models
* `queue_training_job` - Queue Training Job
* `retrieve_single_model` - Retrieve a Single Model

### generating_images

* `inferences_controller_create` - Generate Image
* `inferences_controller_find_all` - List Inference Jobs
* `inferences_controller_find_one` - Get Single Inference Job
* `inferences_controller_remove` - Delete Inference

### image_editing

* `edit_controller_create` - Edit an image
* `edit_controller_create_with_url` - Edit an image from URL
* `edit_controller_find_one` - Get an edit
<!-- End SDK Available Operations -->

### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
