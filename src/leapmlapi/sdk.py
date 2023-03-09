__doc__ = """ SDK Documentation: The Official Leap API"""
import requests as requests_http
from . import utils
from .fine_tuning import FineTuning
from .generating_images import GeneratingImages
from .image_editing import ImageEditing

SERVERS = [
	"https://api.tryleap.ai",
]

class LeapMLAPI:
    r"""SDK Documentation: The Official Leap API"""
    fine_tuning: FineTuning
    generating_images: GeneratingImages
    image_editing: ImageEditing
    
    _client: requests_http.Session
    _security_client: requests_http.Session
    
    _server_url: str = SERVERS[0]
    _language: str = "python"
    _sdk_version: str = "1.8.5"
    _gen_version: str = "1.8.7"

    def __init__(self) -> None:
        self._client = requests_http.Session()
        self._security_client = requests_http.Session()
        self._init_sdks()

    def config_server_url(self, server_url: str, params: dict[str, str] = None):
        if params is not None:
            self._server_url = utils.template_url(server_url, params)
        else:
            self._server_url = server_url

        self._init_sdks()
    
    

    def config_client(self, client: requests_http.Session):
        self._client = client
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
        
    