import requests as requests_http
from . import utils
from leapmlapi.models import operations, shared
from typing import Optional

class GeneratingImages:
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
        
    def inferences_controller_create(self, request: operations.InferencesControllerCreateRequest) -> operations.InferencesControllerCreateResponse:
        r"""Generate Image
        This endpoint will generate a new inference for a particular model.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.InferencesControllerCreatePathParams, base_url, '/api/v1/images/models/{modelId}/inferences', request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = utils.configure_security_client(self._client, request.security)
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.InferencesControllerCreateResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.InferenceEntity])
                res.inference_entity = out

        return res

    def inferences_controller_find_all(self, request: operations.InferencesControllerFindAllRequest) -> operations.InferencesControllerFindAllResponse:
        r"""List Inference Jobs
        Retrieve all inferences for a specific model
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.InferencesControllerFindAllPathParams, base_url, '/api/v1/images/models/{modelId}/inferences', request.path_params)
        
        query_params = utils.get_query_params(operations.InferencesControllerFindAllQueryParams, request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.InferencesControllerFindAllResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            pass

        return res

    def inferences_controller_find_one(self, request: operations.InferencesControllerFindOneRequest) -> operations.InferencesControllerFindOneResponse:
        r"""Get Single Inference Job
        This endpoint will retrieve a specific inference for a particular model.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.InferencesControllerFindOnePathParams, base_url, '/api/v1/images/models/{modelId}/inferences/{inferenceId}', request.path_params)
        
        
        client = utils.configure_security_client(self._client, request.security)
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.InferencesControllerFindOneResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.InferenceEntity])
                res.inference_entity = out

        return res

    def inferences_controller_remove(self, request: operations.InferencesControllerRemoveRequest) -> operations.InferencesControllerRemoveResponse:
        r"""Delete Inference
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.InferencesControllerRemovePathParams, base_url, '/api/v1/images/models/{modelId}/inferences/{inferenceId}', request.path_params)
        
        
        client = utils.configure_security_client(self._client, request.security)
        
        http_res = client.request('DELETE', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.InferencesControllerRemoveResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            pass

        return res

    