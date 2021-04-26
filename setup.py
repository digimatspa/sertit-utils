import setuptools

from sertit import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sertit",
    version=__version__,
    author="Rémi BRAUN",
    author_email="dev-sertit@unistra.fr",
    description="SERTIT python library for generic tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[
        "tqdm",
        "numpy",
        "lxml",
    ],
    extras_require={
        "colorlog": ["colorlog"],
        "full": ["geopandas", "rioxarray", "colorlog"],
        "rasters_rio": ["geopandas", "rasterio"],
        "rasters": ["geopandas", "rioxarray"],
        "vectors": ["geopandas"],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: GIS",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    package_data={"": ["LICENSE", "NOTICE"]},
    include_package_data=True,
    python_requires=">=3.7",
    project_urls={
        "Bug Tracker": "https://github.com/sertit/sertit-utils/issues/",
        "Documentation": "https://sertit.github.io/sertit-utils/sertit/",
        "Source Code": "https://github.com/sertit/sertit-utils",
    },
)
