"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from leapmlapi.models import operations, shared
from typing import Optional

class RemixImages:
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
        
    
    def control_controller_find_one(self, request: operations.ControlControllerFindOneRequest, security: operations.ControlControllerFindOneSecurity) -> operations.ControlControllerFindOneResponse:
        r"""Get a Remix job by ID
        Get a control job by ID for a particular model.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.ControlControllerFindOneRequest, base_url, '/api/v1/images/models/{modelId}/remix/{remixId}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ControlControllerFindOneResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.RemixJob])
                res.remix_job = out

        return res

    
    def create_remix_with_file(self, request: operations.CreateRemixWithFileRequest, security: operations.CreateRemixWithFileSecurity) -> operations.CreateRemixWithFileResponse:
        r"""Remix Image Via File Upload
        Remix allows you to generate images that use existing images as a starting point. This can increase the resemblance of the generated image to the sample.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.CreateRemixWithFileRequest, base_url, '/api/v1/images/models/{modelId}/remix', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'multipart')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateRemixWithFileResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.RemixJob])
                res.remix_job = out

        return res

    
    def create_remix_with_url(self, request: operations.CreateRemixWithURLRequest, security: operations.CreateRemixWithURLSecurity) -> operations.CreateRemixWithURLResponse:
        r"""Remix Image Via URL
        Remix allows you to generate images that use existing images as a starting point. This can increase the resemblance of the generated image to the sample. This endpoint also allows you to use an image URL instead of uploading an image.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.CreateRemixWithURLRequest, base_url, '/api/v1/images/models/{modelId}/remix/url', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "remix_job_with_url_dto", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateRemixWithURLResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.RemixJob])
                res.remix_job = out

        return res

    