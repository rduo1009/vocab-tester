import icecream
import pytest


@pytest.fixture(scope="session", autouse=True)
def install_icecream():
    icecream.install()
