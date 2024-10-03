import icecream  # type: ignore[import-untyped]
import pytest


@pytest.fixture(scope="session", autouse=True)
def install_icecream():
    icecream.install()
