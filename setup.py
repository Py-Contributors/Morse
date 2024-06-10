import setuptools
from glob import glob

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

__name__ = "morseify"
__version__ = "1.0.0"
__author__ = "Deepak Raj"
__author_email__ = "deepak008@live.com"
__description__ = "A package to convert text to morse code and vice versa"
__documentation__ = "https://pycontributors.readthedocs.io/projects/morse/en/latest/"
__source__ = "https://github.com/codeperfectplus/morseit"
__tracker__ = "https://github.com/codeperfectplus/morseit/issues"

setuptools.setup(
    name=__name__,
    version=__version__,
    author=__author__,
    author_email=__author_email__,
    description=__description__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    data_files=[('assets', glob('morse/assets/*'))], 
    include_package_data=True,
    url="https://github.com/codePerfectPlus/morseit",
    keywords="morse code, text to morse, morse to text",
    packages=setuptools.find_packages(),
    project_urls={"Documentation": __documentation__,
                  "Source": __source__,
                  "Tracker": __tracker__},
    classifiers=["Development Status :: 2 - Pre-Alpha",
                 "Programming Language :: Python :: 3",
                 "License :: OSI Approved :: MIT License",
                 "Operating System :: OS Independent",
                 "Intended Audience :: Developers"],
    python_requires=">=3.4",
    entry_points={
        "console_scripts": ["morseify = morseify.cli:main"],
    },
)
