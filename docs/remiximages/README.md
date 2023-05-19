# remix_images

### Available Operations

* [control_controller_find_one](#control_controller_find_one) - Get a Remix job by ID
* [create_remix_with_file](#create_remix_with_file) - Remix Image Via File Upload
* [create_remix_with_url](#create_remix_with_url) - Remix Image Via URL

## control_controller_find_one

Get a control job by ID for a particular model.

### Example Usage

```python
import leapmlapi
from leapmlapi.models import operations

s = leapmlapi.LeapMLAPI()

req = operations.ControlControllerFindOneRequest(
    model_id='quo',
    remix_id='odit',
)

res = s.remix_images.control_controller_find_one(req, operations.ControlControllerFindOneSecurity(
    bearer="YOUR_BEARER_TOKEN_HERE",
))

if res.remix_job is not None:
    # handle response
```

## create_remix_with_file

Remix allows you to generate images that use existing images as a starting point. This can increase the resemblance of the generated image to the sample.

### Example Usage

```python
import leapmlapi
from leapmlapi.models import operations

s = leapmlapi.LeapMLAPI()

req = operations.CreateRemixWithFileRequest(
    request_body=operations.CreateRemixWithFileRequestBody1(
        files=operations.CreateRemixWithFileRequestBodyFiles(
            content='at'.encode(),
            files='at',
        ),
        mode=operations.CreateRemixWithFileRequestBodyMode.CANNY,
        negative_prompt='Disfigured, asymetric',
        number_of_images=4,
        prompt='A photo of a person with a beard',
        seed=9786.19,
        steps=25,
        webhook_url='molestiae',
    ),
    model_id='quod',
)

res = s.remix_images.create_remix_with_file(req, operations.CreateRemixWithFileSecurity(
    bearer="YOUR_BEARER_TOKEN_HERE",
))

if res.remix_job is not None:
    # handle response
```

## create_remix_with_url

Remix allows you to generate images that use existing images as a starting point. This can increase the resemblance of the generated image to the sample. This endpoint also allows you to use an image URL instead of uploading an image.

### Example Usage

```python
import leapmlapi
from leapmlapi.models import operations, shared

s = leapmlapi.LeapMLAPI()

req = operations.CreateRemixWithURLRequest(
    remix_job_with_url_dto=shared.RemixJobWithURLDto(
        image_url='quod',
        mode=shared.RemixJobWithURLDtoMode.MLSD,
        negative_prompt='totam',
        number_of_images=7805.29,
        prompt='dolorum',
        seed=1182.74,
        steps=7206.33,
        webhook_url='officia',
    ),
    model_id='occaecati',
)

res = s.remix_images.create_remix_with_url(req, operations.CreateRemixWithURLSecurity(
    bearer="YOUR_BEARER_TOKEN_HERE",
))

if res.remix_job is not None:
    # handle response
```
