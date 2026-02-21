import pathlib
from typing import Union

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PLAYWRIGHT_BROWSER_CHANNEL: str = Field(
        default="brave", description="Browser distribution channel."
    )
    PLAYWRIGHT_BROWSER_EXECUTABLE_PATH: Union[pathlib.Path, str] = Field(
        default="/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",
        description="Path to a browser executable to run instead of the bundled one.",
    )
