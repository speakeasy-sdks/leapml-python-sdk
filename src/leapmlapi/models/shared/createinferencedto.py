"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from leapmlapi import utils
from typing import Optional

class CreateInferenceDtoSamplerEnum(str, Enum):
    r"""Choose the sampler used for your inference."""
    DDIM = 'ddim'
    DPM_2A = 'dpm_2a'
    DPM_PLUSPLUS_SDE = 'dpm_plusplus_sde'
    EULER = 'euler'
    EULER_A = 'euler_a'

class CreateInferenceDtoUpscaleByEnum(str, Enum):
    r"""Optionally upscale the generated images. This will make the images look more realistic. The default is x1, which means no upscaling. The maximum is x4."""
    X1 = 'x1'
    X2 = 'x2'
    X4 = 'x4'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateInferenceDto:
    
    prompt: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('prompt') }})

    r"""The prompt to use for the inference."""
    enhance_prompt: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enhancePrompt'), 'exclude': lambda f: f is None }})

    r"""Optionally enhance your prompts automatically to generate better results."""
    height: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('height'), 'exclude': lambda f: f is None }})

    r"""The height of the image to use for the inference. Must be a multiple of 8."""
    negative_prompt: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('negativePrompt'), 'exclude': lambda f: f is None }})

    r"""Negative prompts to use for the inference."""
    number_of_images: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('numberOfImages'), 'exclude': lambda f: f is None }})

    r"""The number of images to generate for the inference. Max batch size is 20."""
    prompt_strength: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('promptStrength'), 'exclude': lambda f: f is None }})

    r"""The higher the prompt strength, the closer the generated image will be to the prompt. Must be between 0 and 30."""
    restore_faces: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('restoreFaces'), 'exclude': lambda f: f is None }})

    r"""Optionally apply face restoration to the generated images. This will make images of faces look more realistic."""
    sampler: Optional[CreateInferenceDtoSamplerEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sampler'), 'exclude': lambda f: f is None }})

    r"""Choose the sampler used for your inference."""
    seed: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('seed'), 'exclude': lambda f: f is None }})

    r"""The seed to use for the inference. Must be a positive integer."""
    steps: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('steps'), 'exclude': lambda f: f is None }})

    r"""The number of steps to use for the inference."""
    upscale_by: Optional[CreateInferenceDtoUpscaleByEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('upscaleBy'), 'exclude': lambda f: f is None }})

    r"""Optionally upscale the generated images. This will make the images look more realistic. The default is x1, which means no upscaling. The maximum is x4."""
    version: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('version'), 'exclude': lambda f: f is None }})

    r"""The version of the model to use for the inference. If not provided will default to latest."""
    webhook_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('webhookUrl'), 'exclude': lambda f: f is None }})

    r"""An optional webhook URL that will be called when the model is trained."""
    width: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('width'), 'exclude': lambda f: f is None }})

    r"""The width of the image to use for the inference. Must be a multiple of 8."""
    