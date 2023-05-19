# fine_tuning

### Available Operations

* [models_controller_remove](#models_controller_remove) - Delete a Model
* [samples_controller_create](#samples_controller_create) - Upload Image Samples
* [samples_controller_create_url](#samples_controller_create_url) - Upload Image Samples Via Url
* [samples_controller_find_all](#samples_controller_find_all) - List Image Samples
* [samples_controller_find_one](#samples_controller_find_one) - Get Image Sample
* [samples_controller_remove](#samples_controller_remove) - Archive Image Sample
* [versions_controller_find_all](#versions_controller_find_all) - List All Model Versions
* [versions_controller_find_one](#versions_controller_find_one) - Get Model Version
* [create_model](#create_model) - Create Model
* [list_all_models](#list_all_models) - List All Models
* [queue_training_job](#queue_training_job) - Queue Training Job
* [retrieve_single_model](#retrieve_single_model) - Retrieve a Single Model

## models_controller_remove

Delete a Model

### Example Usage

```python
import leapmlapi
from leapmlapi.models import operations

s = leapmlapi.LeapMLAPI()

req = operations.ModelsControllerRemoveRequest(
    model_id='provident',
)

res = s.fine_tuning.models_controller_remove(req, operations.ModelsControllerRemoveSecurity(
    bearer="YOUR_BEARER_TOKEN_HERE",
))

if res.status_code == 200:
    # handle response
```

## samples_controller_create

Upload one or multiple image sample to a model.

### Example Usage

```python
import leapmlapi
from leapmlapi.models import operations

s = leapmlapi.LeapMLAPI()

req = operations.SamplesControllerCreateRequest(
    request_body=operations.SamplesControllerCreateRequestBody(
        files=operations.SamplesControllerCreateRequestBodyFiles(
            content='distinctio'.encode(),
            files='quibusdam',
        ),
    ),
    model_id='unde',
)

res = s.fine_tuning.samples_controller_create(req, operations.SamplesControllerCreateSecurity(
    bearer="YOUR_BEARER_TOKEN_HERE",
))

if res.training_sample_entity is not None:
    # handle response
```

## samples_controller_create_url

Upload one or multiple image sample to a model.

### Example Usage

```python
import leapmlapi
from leapmlapi.models import operations, shared

s = leapmlapi.LeapMLAPI()

req = operations.SamplesControllerCreateURLRequest(
    upload_samples_via_url_dto=shared.UploadSamplesViaURLDto(
        images=[
            'corrupti',
            'illum',
            'vel',
            'error',
        ],
    ),
    model_id='deserunt',
    return_in_object=False,
)

res = s.fine_tuning.samples_controller_create_url(req, operations.SamplesControllerCreateURLSecurity(
    bearer="YOUR_BEARER_TOKEN_HERE",
))

if res.training_sample_entity is not None:
    # handle response
```

## samples_controller_find_all

Given a model ID, returns all image samples for that model.

### Example Usage

```python
import leapmlapi
from leapmlapi.models import operations

s = leapmlapi.LeapMLAPI()

req = operations.SamplesControllerFindAllRequest(
    model_id='suscipit',
)

res = s.fine_tuning.samples_controller_find_all(req, operations.SamplesControllerFindAllSecurity(
    bearer="YOUR_BEARER_TOKEN_HERE",
))

if res.training_sample_entities is not None:
    # handle response
```

## samples_controller_find_one

Given a model ID and a sample ID, returns the image sample.

### Example Usage

```python
import leapmlapi
from leapmlapi.models import operations

s = leapmlapi.LeapMLAPI()

req = operations.SamplesControllerFindOneRequest(
    model_id='iure',
    sample_id='magnam',
)

res = s.fine_tuning.samples_controller_find_one(req, operations.SamplesControllerFindOneSecurity(
    bearer="YOUR_BEARER_TOKEN_HERE",
))

if res.training_sample_entities is not None:
    # handle response
```

## samples_controller_remove

Given a model ID and a sample ID, archives the image sample. Archived samples are not used for training.

### Example Usage

```python
import leapmlapi
from leapmlapi.models import operations

s = leapmlapi.LeapMLAPI()

req = operations.SamplesControllerRemoveRequest(
    model_id='debitis',
    sample_id='ipsa',
)

res = s.fine_tuning.samples_controller_remove(req, operations.SamplesControllerRemoveSecurity(
    bearer="YOUR_BEARER_TOKEN_HERE",
))

if res.training_sample_entity is not None:
    # handle response
```

## versions_controller_find_all

This endpoint will return a list of all versions of a model including the status of each model.

### Example Usage

```python
import leapmlapi
from leapmlapi.models import operations

s = leapmlapi.LeapMLAPI()

req = operations.VersionsControllerFindAllRequest(
    model_id='delectus',
)

res = s.fine_tuning.versions_controller_find_all(req, operations.VersionsControllerFindAllSecurity(
    bearer="YOUR_BEARER_TOKEN_HERE",
))

if res.model_version_entities is not None:
    # handle response
```

## versions_controller_find_one

This endpoint will return a version of a model including the status of the model.

### Example Usage

```python
import leapmlapi
from leapmlapi.models import operations

s = leapmlapi.LeapMLAPI()

req = operations.VersionsControllerFindOneRequest(
    model_id='tempora',
    version_id='suscipit',
)

res = s.fine_tuning.versions_controller_find_one(req, operations.VersionsControllerFindOneSecurity(
    bearer="YOUR_BEARER_TOKEN_HERE",
))

if res.model_version_entity is not None:
    # handle response
```

## create_model

This endpoint will create a new model

### Example Usage

```python
import leapmlapi
from leapmlapi.models import operations, shared

s = leapmlapi.LeapMLAPI()

req = shared.CreateModelDto(
    subject_identifier='s2dg3g9sd47sdhj',
    subject_keyword='@me',
    subject_type=shared.CreateModelDtoSubjectType.DOG,
    title='Cat Model',
)

res = s.fine_tuning.create_model(req, operations.CreateModelSecurity(
    bearer="YOUR_BEARER_TOKEN_HERE",
))

if res.model_entity is not None:
    # handle response
```

## list_all_models

This endpoint will return a list of all models for the workspace.

### Example Usage

```python
import leapmlapi
from leapmlapi.models import operations

s = leapmlapi.LeapMLAPI()

req = operations.ListAllModelsRequest(
    return_in_object=False,
)

res = s.fine_tuning.list_all_models(req, operations.ListAllModelsSecurity(
    bearer="YOUR_BEARER_TOKEN_HERE",
))

if res.model_entities is not None:
    # handle response
```

## queue_training_job

This endpoint will queue a new model version to be trained. 
    
    After uploading image samples via the samples endpoint. You can use this endpoint to queue a new model version to be trained.
    
    Upon completion, you'll be able to query your custom model via the inference endpoint.

### Example Usage

```python
import leapmlapi
from leapmlapi.models import operations, shared

s = leapmlapi.LeapMLAPI()

req = operations.QueueTrainingJobRequest(
    train_model_dto=shared.TrainModelDto(
        base_weights_id='minus',
        steps=8121.69,
        webhook_url='https://example.com/webhook',
    ),
    model_id='voluptatum',
)

res = s.fine_tuning.queue_training_job(req, operations.QueueTrainingJobSecurity(
    bearer="YOUR_BEARER_TOKEN_HERE",
))

if res.model_version_entity is not None:
    # handle response
```

## retrieve_single_model

This endpoint will return a single model.

### Example Usage

```python
import leapmlapi
from leapmlapi.models import operations

s = leapmlapi.LeapMLAPI()

req = operations.RetrieveSingleModelRequest(
    model_id='iusto',
)

res = s.fine_tuning.retrieve_single_model(req, operations.RetrieveSingleModelSecurity(
    bearer="YOUR_BEARER_TOKEN_HERE",
))

if res.model_entity is not None:
    # handle response
```
