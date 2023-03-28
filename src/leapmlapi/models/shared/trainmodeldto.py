"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from leapmlapi import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TrainModelDto:
    
    base_weights_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('baseWeightsId'), 'exclude': lambda f: f is None }})
    r"""The ID of the weights to use for training - defaults to Stable Diffusion v1.5 weights. Check the pretrained models page for a list of available weights."""  
    webhook_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('webhookUrl'), 'exclude': lambda f: f is None }})
    r"""An optional webhook URL that will be called when the model is trained."""  
    