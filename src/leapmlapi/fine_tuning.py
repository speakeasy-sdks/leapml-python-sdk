import requests
from . import utils
from leapmlapi.models import operations, shared
from typing import Optional

class FineTuning:
    _client: requests.Session
    _security_client: requests.Session
    _server_url: str
    _language: str
    _sdk_version: str
    _gen_version: str

    def __init__(self, client: requests.Session, security_client: requests.Session, server_url: str, language: str, sdk_version: str, gen_version: str) -> None:
        self._client = client
        self._security_client = security_client
        self._server_url = server_url
        self._language = language
        self._sdk_version = sdk_version
        self._gen_version = gen_version

    
    def models_controller_create(self, request: operations.ModelsControllerCreateRequest) -> operations.ModelsControllerCreateResponse:
        r"""Create Model
        This endpoint will create a new model
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/api/v1/images/models"
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and json is None:
           raise Exception('request body is required')
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.ModelsControllerCreateResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ModelEntity])
                res.model_entity = out

        return res

    
    def models_controller_find_all(self, request: operations.ModelsControllerFindAllRequest) -> operations.ModelsControllerFindAllResponse:
        r"""List All Models
        This endpoint will return a list of all models for the workspace.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/api/v1/images/models"
        
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.ModelsControllerFindAllResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[list[shared.ModelEntity]])
                res.model_entities = out

        return res

    
    def models_controller_find_one(self, request: operations.ModelsControllerFindOneRequest) -> operations.ModelsControllerFindOneResponse:
        r"""Retrieve a Single Model
        This endpoint will return a single model.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/v1/images/models/{modelId}", request.path_params)
        
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.ModelsControllerFindOneResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ModelEntity])
                res.model_entity = out

        return res

    
    def models_controller_queue(self, request: operations.ModelsControllerQueueRequest) -> operations.ModelsControllerQueueResponse:
        r"""Queue Training Job
        This endpoint will queue a new model version to be trained. 
            
            After uploading image samples via the samples endpoint. You can use this endpoint to queue a new model version to be trained.
            
            Upon completion, you'll be able to query your custom model via the inference endpoint.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/v1/images/models/{modelId}/queue", request.path_params)
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.ModelsControllerQueueResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ModelVersionEntity])
                res.model_version_entity = out

        return res

    
    def samples_controller_create(self, request: operations.SamplesControllerCreateRequest) -> operations.SamplesControllerCreateResponse:
        r"""Upload Image Samples
        Upload one or multiple image sample to a model.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/v1/images/models/{modelId}/samples", request.path_params)
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and json is None:
           raise Exception('request body is required')
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.SamplesControllerCreateResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.TrainingSampleEntity])
                res.training_sample_entity = out

        return res

    
    def samples_controller_find_all(self, request: operations.SamplesControllerFindAllRequest) -> operations.SamplesControllerFindAllResponse:
        r"""List Image Samples
        Given a model ID, returns all image samples for that model.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/v1/images/models/{modelId}/samples", request.path_params)
        
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.SamplesControllerFindAllResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[list[shared.TrainingSampleEntity]])
                res.training_sample_entities = out

        return res

    
    def samples_controller_find_one(self, request: operations.SamplesControllerFindOneRequest) -> operations.SamplesControllerFindOneResponse:
        r"""Get Image Sample
        Given a model ID and a sample ID, returns the image sample.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/v1/images/models/{modelId}/samples/{sampleId}", request.path_params)
        
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.SamplesControllerFindOneResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[list[shared.TrainingSampleEntity]])
                res.training_sample_entities = out

        return res

    
    def samples_controller_remove(self, request: operations.SamplesControllerRemoveRequest) -> operations.SamplesControllerRemoveResponse:
        r"""Archive Image Sample
        Given a model ID and a sample ID, archives the image sample. Archived samples are not used for training.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/v1/images/models/{modelId}/samples/{sampleId}/archive", request.path_params)
        
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("POST", url)
        content_type = r.headers.get("Content-Type")

        res = operations.SamplesControllerRemoveResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.TrainingSampleEntity])
                res.training_sample_entity = out

        return res

    
    def versions_controller_find_all(self, request: operations.VersionsControllerFindAllRequest) -> operations.VersionsControllerFindAllResponse:
        r"""List All Model Versions
        This endpoint will return a list of all versions of a model including the status of each model.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/v1/images/models/{modelId}/versions", request.path_params)
        
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.VersionsControllerFindAllResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[list[shared.ModelVersionEntity]])
                res.model_version_entities = out

        return res

    
    def versions_controller_find_one(self, request: operations.VersionsControllerFindOneRequest) -> operations.VersionsControllerFindOneResponse:
        r"""Get Model Version
        This endpoint will return a version of a model including the status of the model.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/v1/images/models/{modelId}/versions/{versionId}", request.path_params)
        
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.VersionsControllerFindOneResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ModelVersionEntity])
                res.model_version_entity = out

        return res

    