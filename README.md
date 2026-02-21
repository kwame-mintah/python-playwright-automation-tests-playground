# Python Playwright Automation Tests Playground

![python](https://img.shields.io/badge/python-3.14.0-informational)

As the name of the repository suggests, it's just a [_playground_](https://dictionary.cambridge.org/dictionary/english/playground).
A place to better understand using [playwright](https://playwright.dev/), that enables reliable end-to-end testing for modern web apps.
This project aims to have a running demonstration of the tool to run a _simple_ test.

## Prerequisites

1. [Docker for desktop](https://docs.docker.com/desktop/)
2. [uv](https://docs.astral.sh/uv/#installation)
3. [ffmpeg](https://ffmpeg.org/)

### Usage via `uv`

1. Install python packages used for the project

```pycon
uv sync
```

2. Install Playwright browsers

```shell
playwright install
```

3. Run the tests defined within this project

```pycon
pytest
```

[!NOTE]
> If you want to use a different mock video for the [video_stream_injection](tests/features/video_stream_injection.feature) tests
> you will need to convert the video to `.y4m`, which is the raw uncompressed format, note that size on disk can be quite big, use a
> lower resolution e.g. `ffmpeg -i pexels_arijit_dey_dog_video_15271584_3840_2160_60fps.mp4 -vf scale=640:480 -r 10 -t 3 -pix_fmt yuv420p pexels_arijit_dey_dog_video_15271584_3840_2160_60fps.y4m`

## Test outputs

When running Playwright, this project has been configured to [capture a video recording](https://playwright.dev/python/docs/videos#record-video) of the test run, as well as generating a
HTML file containing the results for each test.

### Example recorded video test
![](videos/example_playwright_video_stream_injection_run_converted_to_mp4_for_readme.mp4)

## Credits

[Video by Arijit Dey](data/video/pexels_arijit_dey_dog_video_15271584_3840_2160_60fps.y4m): https://www.pexels.com/video/adorable-puppy-resting-in-a-sunlit-forest-36014853/
