from playwright.sync_api import Page, expect
from pytest_bdd import given, then, scenario, parsers


@scenario(
    feature_name="features/video_stream_injection.feature",
    scenario_name="Webcam video stream is injected with mock",
)
def test_webcam_video_stream_is_injected_with_mock():
    """Webcam video stream is injected with mock."""


@given(name=parsers.parse("I am a user on site {url}"))
def access_given_site_url(web_page: Page, url: str):
    """I am a user on site {url}."""
    web_page.goto(url)
    assert web_page.title() == "Webcam + MediaPipe Image Classification"


@given("I am able to request an image for prediction")
def request_model_prediction(web_page: Page):
    """I am able to request an image for prediction."""
    response = web_page.locator("#response")
    # 10 seconds (default: 5 sec) timeout due to model load timings
    expect(response).to_contain_text("Model loaded. Ready!", timeout=10000)

    web_page.get_by_role(role="button", name="Capture & Predict").click()


@then("I should be able to see the prediction result")
def view_model_prediction_results(web_page: Page):
    """I should be able to see the prediction result."""
    response = web_page.locator("#response")

    expect(response).not_to_contain_text("Webcam access denied or not available.")
    expect(response).not_to_contain_text("Analyzing image...")

    expect(response).to_contain_text("Chihuahua")
    expect(response).to_contain_text("Staffordshire bullterrier")
    expect(response).to_contain_text("white wolf")
