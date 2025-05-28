import pytest

@pytest.mark.usefixtures("setup_browser", "log_on_failure")
class BaseTest:
    pass