from pytest_bdd import given, then, scenario


@scenario(
    "features/video_stream_injection.feature",
    "Webcam video stream is injected with mock",
)
def test_webcam_video_stream_is_injected_with_mock():
    """Webcam video stream is injected with mock."""


@given("I am a user on <url>")
def _():
    """I am a user on <url>."""
    raise NotImplementedError


@given("I grant permission for the site to access my webcam")
def _():
    """I grant permission for the site to access my webcam."""
    raise NotImplementedError


@then("I should be able to view the stream on the page")
def _():
    """I should be able to view the stream on the page."""
    raise NotImplementedError
