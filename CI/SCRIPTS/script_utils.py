import filecmp
import hashlib
import os
import rasterio
import numpy as np


def get_proj_path():
    """ Get project path """
    return os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


def get_ci_data_path():
    """ Get CI DATA path """
    return os.path.join(get_proj_path(), "CI", "DATA")


def assert_raster_equal(path_1: str, path_2: str) -> None:
    """
    Assert that 2 raster are equal
    Args:
        path_1 (str): Raster 1
        path_2 (str): Raster 2
    """
    with rasterio.open(path_1) as dst_1:
        with rasterio.open(path_2) as dst_2:
            assert dst_1.meta == dst_2.meta
            np.testing.assert_array_equal(dst_1.read(), dst_2.read())

def assert_dir_equal(path_1: str, path_2: str) -> None:
    """
    Assert that two directories are equal

    Args:
        path_1 (str): Directory 1
        path_2 (str): Directory 2
    """
    dcmp = filecmp.dircmp(path_1, path_2)
    assert os.path.isdir(path_1)
    assert os.path.isdir(path_2)
    assert dcmp.left_only == []
    assert dcmp.right_only == []

def assert_archive_equal(path_1: str, path_2: str) -> None:
    """
    Assert that two archives are equal, by creating hashes that should be equal

    Args:
        path_1 (str): Archive 1
        path_2 (str): Archive 2
    """
    filecmp.cmp(path_1, path_2)

    file_1 = hashlib.sha256(open(path_1, 'rb').read()).digest()
    file_2 = hashlib.sha256(open(path_2, 'rb').read()).digest()
    assert file_1 == file_2