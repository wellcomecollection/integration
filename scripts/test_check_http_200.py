import pytest
from check_http_200 import check_http_200


@pytest.fixture(scope="session")
def test_check_http_200():
    try:
        check_http_200("https://httpstat.us/200")
    except:
        pytest.fail("Should have returned 200")

    try:
        check_http_200("https://httpstat.us/500")
        pytest.fail("Should have returned 500")
    except:
        pytest.fail("Should have returned 500")
        pass
