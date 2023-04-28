# generating_images

### Available Operations

* [inferences_controller_create](#inferences_controller_create) - Generate an image using a text prompt
* [inferences_controller_find_all](#inferences_controller_find_all) - List inference jobs for a model
* [inferences_controller_find_one](#inferences_controller_find_one) - Get a single inference job
* [inferences_controller_remove](#inferences_controller_remove) - Delete Inference

## inferences_controller_create

Generate an image using a text prompt. The model used to generate the image is determined by the `modelId` parameter. A job ID is returned that can be used to retrieve the generated image(s).

### Example Usage

```python
import leapmlapi
from leapmlapi.models import operations, shared

s = leapmlapi.LeapMLAPI()


req = operations.InferencesControllerCreateRequest(
    create_inference_dto=shared.CreateInferenceDto(
        enhance_prompt=False,
        height=512,
        negative_prompt="asymmetric, bad hands, bad hair",
        number_of_images=1,
        prompt="A photo of an astronaut riding a horse",
        prompt_strength=7,
        restore_faces=False,
        sampler="dpm_plusplus_sde",
        seed=4523184,
        steps=50,
        upscale_by="x2",
        version="307f2df9-4305-4d5e-9b95-9be1d9d6fb35",
        webhook_url="recusandae",
        width=512,
    ),
    model_id="temporibus",
)

res = s.generating_images.inferences_controller_create(req, operations.InferencesControllerCreateSecurity(
    bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.inference_entity is not None:
    # handle response
```

## inferences_controller_find_all

Fetch a list of inference jobs for a particular model.

### Example Usage

```python
import leapmlapi
from leapmlapi.models import operations

s = leapmlapi.LeapMLAPI()


req = operations.InferencesControllerFindAllRequest(
    model_id="ab",
    only_finished=False,
    page=3373.96,
    page_size=871.29,
)

res = s.generating_images.inferences_controller_find_all(req, operations.InferencesControllerFindAllSecurity(
    bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.status_code == 200:
    # handle response
```

## inferences_controller_find_one

This endpoint will retrieve a specific inference for a particular model.

### Example Usage

```python
import leapmlapi
from leapmlapi.models import operations

s = leapmlapi.LeapMLAPI()


req = operations.InferencesControllerFindOneRequest(
    inference_id="deserunt",
    model_id="perferendis",
)

res = s.generating_images.inferences_controller_find_one(req, operations.InferencesControllerFindOneSecurity(
    bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.inference_entity is not None:
    # handle response
```

## inferences_controller_remove

Delete Inference

### Example Usage

```python
import leapmlapi
from leapmlapi.models import operations

s = leapmlapi.LeapMLAPI()


req = operations.InferencesControllerRemoveRequest(
    inference_id="ipsam",
    model_id="repellendus",
)

res = s.generating_images.inferences_controller_remove(req, operations.InferencesControllerRemoveSecurity(
    bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.status_code == 200:
    # handle response
```
