from playwright.sync_api import Page
from pytest_bdd import given, then, scenario, parsers


@scenario(
    feature_name="features/video_stream_injection.feature",
    scenario_name="Webcam video stream is injected with mock",
)
def test_webcam_video_stream_is_injected_with_mock():
    """Webcam video stream is injected with mock."""


@given(name=parsers.parse("I am a user on {url}"))
def access_given_site_url(web_page: Page, url: str):
    """I am a user on <url>."""
    web_page.goto(url)


@given("I grant permission for the site to access my webcam")
def grant_webcam_permissions(web_page: Page):
    """I grant permission for the site to access my webcam."""
    raise NotImplementedError


@then("I should be able to view the stream on the page")
def view_video_stream(web_page: Page):
    """I should be able to view the stream on the page."""
    raise NotImplementedError
