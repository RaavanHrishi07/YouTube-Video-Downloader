
import pytest

from youtube_vid_dl import is_valid_youtube_url


@pytest.mark.parametrize(
    "url",
    [
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        "https://youtu.be/dQw4w9WgXcQ",
        "https://youtube.com/shorts/dQw4w9WgXcQ",
        "http://youtube.com/watch?v=dQw4w9WgXcQ",
    ],
)
def test_valid_youtube_urls(url):
    assert is_valid_youtube_url(url) is True


@pytest.mark.parametrize(
    "url",
    [
        "",
        "not-a-url",
        "https://example.com/video",
        "https://youtube.com/watch?v=short",
        "https://youtube.com/watch?v=",
    ],
)
def test_invalid_youtube_urls(url):
    assert is_valid_youtube_url(url) is False


def test_url_with_surrounding_whitespace():
    url = "  https://youtu.be/dQw4w9WgXcQ  "
    assert is_valid_youtube_url(url) is True
