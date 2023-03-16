import requests as requests_http
from . import utils
from leapmlapi.models import operations, shared
from typing import Optional

class FineTuning:
    _client: requests_http.Session
    _security_client: requests_http.Session
    _server_url: str
    _language: str
    _sdk_version: str
    _gen_version: str

    def __init__(self, client: requests_http.Session, security_client: requests_http.Session, server_url: str, language: str, sdk_version: str, gen_version: str) -> None:
        self._client = client
        self._security_client = security_client
        self._server_url = server_url
        self._language = language
        self._sdk_version = sdk_version
        self._gen_version = gen_version
        
    def models_controller_remove(self, request: operations.ModelsControllerRemoveRequest) -> operations.ModelsControllerRemoveResponse:
        r"""Delete a Model
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.ModelsControllerRemovePathParams, base_url, '/api/v1/images/models/{modelId}', request.path_params)
        
        
        client = utils.configure_security_client(self._client, request.security)
        
        http_res = client.request('DELETE', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ModelsControllerRemoveResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            pass

        return res

    def samples_controller_create(self, request: operations.SamplesControllerCreateRequest) -> operations.SamplesControllerCreateResponse:
        r"""Upload Image Samples
        Upload one or multiple image sample to a model.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.SamplesControllerCreatePathParams, base_url, '/api/v1/images/models/{modelId}/samples', request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'multipart')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = utils.configure_security_client(self._client, request.security)
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.SamplesControllerCreateResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.TrainingSampleEntity])
                res.training_sample_entity = out

        return res

    def samples_controller_create_url(self, request: operations.SamplesControllerCreateURLRequest) -> operations.SamplesControllerCreateURLResponse:
        r"""Upload Image Samples Via Url
        Upload one or multiple image sample to a model.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.SamplesControllerCreateURLPathParams, base_url, '/api/v1/images/models/{modelId}/samples/url', request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        query_params = utils.get_query_params(operations.SamplesControllerCreateURLQueryParams, request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        http_res = client.request('POST', url, params=query_params, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.SamplesControllerCreateURLResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.TrainingSampleEntity])
                res.training_sample_entity = out

        return res

    def samples_controller_find_all(self, request: operations.SamplesControllerFindAllRequest) -> operations.SamplesControllerFindAllResponse:
        r"""List Image Samples
        Given a model ID, returns all image samples for that model.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.SamplesControllerFindAllPathParams, base_url, '/api/v1/images/models/{modelId}/samples', request.path_params)
        
        
        client = utils.configure_security_client(self._client, request.security)
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.SamplesControllerFindAllResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[list[shared.TrainingSampleEntity]])
                res.training_sample_entities = out

        return res

    def samples_controller_find_one(self, request: operations.SamplesControllerFindOneRequest) -> operations.SamplesControllerFindOneResponse:
        r"""Get Image Sample
        Given a model ID and a sample ID, returns the image sample.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.SamplesControllerFindOnePathParams, base_url, '/api/v1/images/models/{modelId}/samples/{sampleId}', request.path_params)
        
        
        client = utils.configure_security_client(self._client, request.security)
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.SamplesControllerFindOneResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[list[shared.TrainingSampleEntity]])
                res.training_sample_entities = out

        return res

    def samples_controller_remove(self, request: operations.SamplesControllerRemoveRequest) -> operations.SamplesControllerRemoveResponse:
        r"""Archive Image Sample
        Given a model ID and a sample ID, archives the image sample. Archived samples are not used for training.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.SamplesControllerRemovePathParams, base_url, '/api/v1/images/models/{modelId}/samples/{sampleId}/archive', request.path_params)
        
        
        client = utils.configure_security_client(self._client, request.security)
        
        http_res = client.request('POST', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.SamplesControllerRemoveResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.TrainingSampleEntity])
                res.training_sample_entity = out

        return res

    def versions_controller_find_all(self, request: operations.VersionsControllerFindAllRequest) -> operations.VersionsControllerFindAllResponse:
        r"""List All Model Versions
        This endpoint will return a list of all versions of a model including the status of each model.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.VersionsControllerFindAllPathParams, base_url, '/api/v1/images/models/{modelId}/versions', request.path_params)
        
        
        client = utils.configure_security_client(self._client, request.security)
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.VersionsControllerFindAllResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[list[shared.ModelVersionEntity]])
                res.model_version_entities = out

        return res

    def versions_controller_find_one(self, request: operations.VersionsControllerFindOneRequest) -> operations.VersionsControllerFindOneResponse:
        r"""Get Model Version
        This endpoint will return a version of a model including the status of the model.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.VersionsControllerFindOnePathParams, base_url, '/api/v1/images/models/{modelId}/versions/{versionId}', request.path_params)
        
        
        client = utils.configure_security_client(self._client, request.security)
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.VersionsControllerFindOneResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ModelVersionEntity])
                res.model_version_entity = out

        return res

    def create_model(self, request: operations.CreateModelRequest) -> operations.CreateModelResponse:
        r"""Create Model
        This endpoint will create a new model
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/api/v1/images/models'
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = utils.configure_security_client(self._client, request.security)
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateModelResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ModelEntity])
                res.model_entity = out

        return res

    def list_all_models(self, request: operations.ListAllModelsRequest) -> operations.ListAllModelsResponse:
        r"""List All Models
        This endpoint will return a list of all models for the workspace.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/api/v1/images/models'
        
        query_params = utils.get_query_params(operations.ListAllModelsQueryParams, request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListAllModelsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[list[shared.ModelEntity]])
                res.model_entities = out

        return res

    def queue_training_job(self, request: operations.QueueTrainingJobRequest) -> operations.QueueTrainingJobResponse:
        r"""Queue Training Job
        This endpoint will queue a new model version to be trained. 
            
            After uploading image samples via the samples endpoint. You can use this endpoint to queue a new model version to be trained.
            
            Upon completion, you'll be able to query your custom model via the inference endpoint.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.QueueTrainingJobPathParams, base_url, '/api/v1/images/models/{modelId}/queue', request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = utils.configure_security_client(self._client, request.security)
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.QueueTrainingJobResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ModelVersionEntity])
                res.model_version_entity = out

        return res

    def retrieve_single_model(self, request: operations.RetrieveSingleModelRequest) -> operations.RetrieveSingleModelResponse:
        r"""Retrieve a Single Model
        This endpoint will return a single model.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.RetrieveSingleModelPathParams, base_url, '/api/v1/images/models/{modelId}', request.path_params)
        
        
        client = utils.configure_security_client(self._client, request.security)
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.RetrieveSingleModelResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ModelEntity])
                res.model_entity = out

        return res

    