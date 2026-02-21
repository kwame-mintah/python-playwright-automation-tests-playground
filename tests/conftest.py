import os
import pathlib
from datetime import datetime

import pytest
from playwright.sync_api import sync_playwright


def pytest_configure(config: pytest.Config) -> None:
    """
    Create a `/reports/` directory and timestamp reports generated.
    """
    # Create reports directory
    os.makedirs("reports", exist_ok=True)

    # Generate timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Build file paths
    html_report = f"../reports/report_{timestamp}.html"
    cucumber_report = f"../reports/cucumber_{timestamp}.json"

    # Inject options dynamically
    config.option.htmlpath = html_report
    config.option.cucumberjson = cucumber_report
    config.option.self_contained_html = True


@pytest.fixture(scope="session")
def launch_web_browser():
    """
    Launch the web browser ready for testing.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(
            executable_path="/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",
            headless=False,
            slow_mo=1000,
            args=[
                "--use-fake-device-for-media-stream",
                "--use-fake-ui-for-media-stream",
                f"--use-file-for-fake-video-capture={pathlib.Path('data/video/pexels_arijit_dey_dog_video_15271584_3840_2160_60fps.mp4')}",
            ],
        )
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def web_page(launch_web_browser):
    context = launch_web_browser.new_context(permissions=["camera", "microphone"])
    page = context.new_page()
    yield page
    context.close()
