from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PLAYWRIGHT_HEADLESS_MODE: bool = Field(
        default=False, description="Whether to run browser in headless mode."
    )
