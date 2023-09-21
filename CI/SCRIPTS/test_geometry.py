# -*- coding: utf-8 -*-
# Copyright 2023, SERTIT-ICube - France, https://sertit.unistra.fr/
# This file is part of sertit-utils project
#     https://github.com/sertit/sertit-utils
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
""" Script testing vector functions """

from CI.SCRIPTS.script_utils import s3_env, vectors_path
from sertit import ci, geometry, vectors

ci.reduce_verbosity()


@s3_env
def test_simplify_footprint():
    """Test simplify footprint"""
    complicated_footprint_path = vectors_path().joinpath(
        "complicated_footprint_spot6.geojson"
    )
    max_nof_vertices = 40
    complicated_footprint = vectors.read(complicated_footprint_path)
    ok_footprint = geometry.simplify_footprint(
        complicated_footprint, resolution=1.5, max_nof_vertices=max_nof_vertices
    )
    assert len(ok_footprint.geometry.exterior.iat[0].coords) < max_nof_vertices

    # Just to test
    nof_vertices_complicated = len(
        complicated_footprint.explode(index_parts=True).geometry.exterior.iat[0].coords
    )
    assert nof_vertices_complicated > max_nof_vertices


@s3_env
def test_geometry_fct():
    """Test other geometry functions"""
    kml_path = vectors_path().joinpath("aoi.kml")
    env = vectors.read(kml_path).envelope[0]
    from_env = geometry.from_bounds_to_polygon(*geometry.from_polygon_to_bounds(env))
    assert env.bounds == from_env.bounds


def test_make_valid():
    """Test make valid"""
    broken_geom_path = vectors_path().joinpath("broken_geom.shp")
    broken_geom = vectors.read(broken_geom_path)
    assert len(broken_geom[~broken_geom.is_valid]) == 1
    valid = geometry.make_valid(broken_geom, verbose=True)
    assert len(valid[~valid.is_valid]) == 0
    assert len(valid) == len(broken_geom)


# Missing:
# - get_wider_exterior
# - fill_polygon_holes
