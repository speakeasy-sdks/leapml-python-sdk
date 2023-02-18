import requests
from . import utils
from leapmlapi.models import operations, shared
from typing import Optional

class ImageEditing:
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

    
    def edit_controller_create(self, request: operations.EditControllerCreateRequest) -> operations.EditControllerCreateResponse:
        r"""Edit an image
        Edit an image using just a prompt
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/api/v1/images/edit"
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and json is None:
           raise Exception('request body is required')
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.EditControllerCreateResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.EditEntity])
                res.edit_entity = out

        return res

    
    def edit_controller_create_with_url(self, request: operations.EditControllerCreateWithURLRequest) -> operations.EditControllerCreateWithURLResponse:
        r"""Edit an image from URL
        Edit an image using just a prompt
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/api/v1/images/edit/url"
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and json is None:
           raise Exception('request body is required')
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.EditControllerCreateWithURLResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.EditEntity])
                res.edit_entity = out

        return res

    
    def edit_controller_find_one(self, request: operations.EditControllerFindOneRequest) -> operations.EditControllerFindOneResponse:
        r"""Get an edit
        Get an edit by ID
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/v1/images/edit/{editId}", request.path_params)
        
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.EditControllerFindOneResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.EditEntity])
                res.edit_entity = out

        return res

    