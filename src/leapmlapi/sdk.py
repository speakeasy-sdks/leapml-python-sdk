"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from .fine_tuning import FineTuning
from .generating_images import GeneratingImages
from .image_editing import ImageEditing
from .projects import Projects

SERVERS = [
    "https://api.tryleap.ai",
    r"""Production"""
]
"""Contains the list of servers available to the SDK"""

class LeapMLAPI:
    r"""The Official Leap API"""
    fine_tuning: FineTuning
    generating_images: GeneratingImages
    image_editing: ImageEditing
    projects: Projects

    _client: requests_http.Session
    _security_client: requests_http.Session
    _server_url: str = SERVERS[0]
    _language: str = "python"
    _sdk_version: str = "1.17.1"
    _gen_version: str = "2.19.1"

    def __init__(self,
                 server_url: str = None,
                 url_params: dict[str, str] = None,
                 client: requests_http.Session = None
                 ) -> None:
        """Instantiates the SDK configuring it with the provided parameters.
        
        :param server_url: The server URL to use for all operations
        :type server_url: str
        :param url_params: Parameters to optionally template the server URL with
        :type url_params: dict[str, str]
        :param client: The requests.Session HTTP client to use for all operations
        :type client: requests_http.Session        
        """
        self._client = requests_http.Session()
        
        
        if server_url is not None:
            if url_params is not None:
                self._server_url = utils.template_url(server_url, url_params)
            else:
                self._server_url = server_url

        if client is not None:
            self._client = client
        
        self._security_client = self._client
        

        self._init_sdks()
    
    def _init_sdks(self):
        self.fine_tuning = FineTuning(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.generating_images = GeneratingImages(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.image_editing = ImageEditing(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.projects = Projects(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
    