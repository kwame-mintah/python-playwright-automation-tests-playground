from playwright.sync_api import Page, expect
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
    assert web_page.title() == "Webcam + MediaPipe Image Classification"


@given("I grant permission for the site to access my webcam")
def grant_webcam_permissions(web_page: Page):
    """I grant permission for the site to access my webcam."""
    response = web_page.locator("#response")

    web_page.get_by_role(role="button", name="Capture & Predict").click()


@then("I should be able to view the stream on the page")
def view_video_stream(web_page: Page):
    """I should be able to view the stream on the page."""
    response = web_page.locator("#response")

    expect(response).not_to_contain_text("Webcam access denied or not available.")
    expect(response).not_to_contain_text("Analyzing image...")

    expect(response).to_contain_text("Chihuahua")
    expect(response).to_contain_text("Staffordshire bullterrier")
    expect(response).to_contain_text("white wolf")
