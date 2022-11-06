import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Morse",
    version="1.0.0",
    author="CodePerfectPlus",
    author_email="deepak008@live.com",
    description="A package to convert text to morse code and vice versa",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/codePerfectPlus/morse",
    keywords="audiobook",
    packages=setuptools.find_packages(),
    project_urls={"Documentation": "https://pycontributors.readthedocs.io/projects/morse/en/latest/",
                  "Source": "https://github.com/Py-Contributors/morse",
                  "Tracker": "https://github.com/Py-Contributors/morse/issues"},
    classifiers=["Development Status :: 2 - Pre-Alpha",
                 "Programming Language :: Python :: 3",
                 "License :: OSI Approved :: MIT License",
                 "Operating System :: OS Independent",
                 "Intended Audience :: Developers"],
    python_requires=">=3.4",
    entry_points={
        "console_scripts": ["morse = morse.cli:main"],
    },
)
