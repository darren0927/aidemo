# conf.py
from pydantic import ValidationError
from pydantic_settings import BaseSettings
import json
from pathlib import Path


class AppConfig(BaseSettings):
    model_name: str

    @classmethod
    def from_json(cls):
        try:
            with open(Path('./app_config.json'), encoding='utf-8') as f:
                config_data = json.load(f)
            return cls(**config_data)
        except ValidationError as e:
            raise e
        except Exception as e:
            raise e


class ZhiPuConfig(BaseSettings):
    api_key: str
    daily_quote_prompt: dict
    daily_date_prompt: dict

    @classmethod
    def from_json(cls):
        try:
            with open(Path('./zhipu_config.json'), encoding='utf-8') as f:
                config_data = json.load(f)
            return cls(**config_data)
        except ValidationError as e:
            raise e
        except Exception as e:
            raise e


class QWenConfig(BaseSettings):
    api_key: str
    daily_quote_prompt: dict
    daily_date_prompt: dict

    @classmethod
    def from_json(cls):
        try:
            with open(Path('./qwen_config.json'), encoding='utf-8') as f:
                config_data = json.load(f)
            return cls(**config_data)
        except ValidationError as e:
            raise e
        except Exception as e:
            raise e