# remix_images

### Available Operations

* [control_controller_create](#control_controller_create) - Remix an image using a sample by uploading a file - uses multipart/form-data
* [control_controller_create_with_url](#control_controller_create_with_url) - Remix an image using a control sample - upload image using a URL
* [control_controller_find_one](#control_controller_find_one) - Get a Remix job by ID

## control_controller_create

Remix allows you to generate images that use existing images as a starting point. This can increase the resemblance of the generated image to the sample.

### Example Usage

```python
import leapmlapi
from leapmlapi.models import operations

s = leapmlapi.LeapMLAPI()


req = operations.ControlControllerCreateRequest(
    request_body=operations.ControlControllerCreateRequestBody(
        files=operations.ControlControllerCreateRequestBodyFiles(
            content="quo".encode(),
            files="odit",
        ),
        mode="canny",
        negative_prompt="Disfigured, asymetric",
        number_of_images=4,
        prompt="A photo of a person with a beard",
        seed=8700.13,
        steps=25,
        webhook_url="at",
    ),
    model_id="maiores",
)

res = s.remix_images.control_controller_create(req, operations.ControlControllerCreateSecurity(
    bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.control_entity is not None:
    # handle response
```

## control_controller_create_with_url

Remix allows you to generate images that use existing images as a starting point. This can increase the resemblance of the generated image to the sample. This endpoint also allows you to use an image URL instead of uploading an image.

### Example Usage

```python
import leapmlapi
from leapmlapi.models import operations, shared

s = leapmlapi.LeapMLAPI()


req = operations.ControlControllerCreateWithURLRequest(
    body_dto_with_url=shared.BodyDtoWithURL(
        image_url="molestiae",
        mode="scribble",
        negative_prompt="quod",
        number_of_images=4614.79,
        prompt="totam",
        seed=7805.29,
        steps=6788.8,
        webhook_url="dicta",
    ),
    model_id="nam",
)

res = s.remix_images.control_controller_create_with_url(req, operations.ControlControllerCreateWithURLSecurity(
    bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.control_entity is not None:
    # handle response
```

## control_controller_find_one

Get a control job by ID for a particular model.

### Example Usage

```python
import leapmlapi
from leapmlapi.models import operations

s = leapmlapi.LeapMLAPI()


req = operations.ControlControllerFindOneRequest(
    model_id="officia",
    remix_id="occaecati",
)

res = s.remix_images.control_controller_find_one(req, operations.ControlControllerFindOneSecurity(
    bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.control_entity is not None:
    # handle response
```
