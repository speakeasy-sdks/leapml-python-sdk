# image_editing

### Available Operations

* [edit_controller_create](#edit_controller_create) - Edit an image
* [edit_controller_create_with_url](#edit_controller_create_with_url) - Edit an image from URL
* [edit_controller_find_one](#edit_controller_find_one) - Get an edit

## edit_controller_create

Edit an image using just a prompt

### Example Usage

```python
import leapmlapi
from leapmlapi.models import operations

s = leapmlapi.LeapMLAPI()


req = operations.EditControllerCreateRequestBody(
    files=operations.EditControllerCreateRequestBodyFiles(
        content="sapiente".encode(),
        files="quo",
    ),
    negative_prompt="Disfigured, asymetric",
    number_of_images=4,
    prompt="Make it rain",
    seed=1403.5,
    steps=25,
    webhook_url="at",
)

res = s.image_editing.edit_controller_create(req, operations.EditControllerCreateSecurity(
    bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.edit_entity is not None:
    # handle response
```

## edit_controller_create_with_url

Edit an image using just a prompt

### Example Usage

```python
import leapmlapi
from leapmlapi.models import operations

s = leapmlapi.LeapMLAPI()


req = operations.EditControllerCreateWithURLRequestBody(
    image_guidance_scale=2,
    image_url="at",
    prompt="Give her sunglasses",
    seed=187461528,
    steps=25,
    text_guidance_scale=10,
    webhook_url="https://example.com/webhook",
)

res = s.image_editing.edit_controller_create_with_url(req, operations.EditControllerCreateWithURLSecurity(
    bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.edit_entity is not None:
    # handle response
```

## edit_controller_find_one

Get an edit by ID

### Example Usage

```python
import leapmlapi
from leapmlapi.models import operations

s = leapmlapi.LeapMLAPI()


req = operations.EditControllerFindOneRequest(
    edit_id="maiores",
)

res = s.image_editing.edit_controller_find_one(req, operations.EditControllerFindOneSecurity(
    bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.edit_entity is not None:
    # handle response
```
