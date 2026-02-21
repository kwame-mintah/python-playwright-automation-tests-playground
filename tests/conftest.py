import os
from datetime import datetime

from pytest import Config


def pytest_configure(config: Config) -> None:
    """
    Create a `/reports/` directory and timestamp reports generated.
    """
    # Create reports directory
    os.makedirs("reports", exist_ok=True)

    # Generate timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Build file paths
    html_report = f"reports/report_{timestamp}.html"
    cucumber_report = f"reports/cucumber_{timestamp}.json"

    # Inject options dynamically
    config.option.htmlpath = html_report
    config.option.cucumberjson = cucumber_report
    config.option.self_contained_html = True
