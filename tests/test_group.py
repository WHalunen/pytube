import pytest

from pytube import YouTube

def test_filename():
    url = "https://www.youtube.com/watch?v=rf_KqDoNvhQ&"

    # Size of file in Bytes
    filename = YouTube(url).streams.first().filename

    expectedfilename = "The Tommy Wi-Show Ep. 1: Mortal Kombats"

    assert expectedfilename == filename


def test_filesize():
    url = "https://www.youtube.com/watch?v=rf_KqDoNvhQ&"

    # Size of file in Bytes
    actual_filesize = YouTube(url).streams.first().filesize

    expected_file_size = 52408985

    assert actual_filesize == expected_file_size

def test_videolength():
    url = "https://www.youtube.com/watch?v=rf_KqDoNvhQ&"

    # Size of file in Bytes
    actual_seconds_long = YouTube(url).length

    expected_seconds_long = 374

    assert actual_seconds_long == expected_seconds_long

