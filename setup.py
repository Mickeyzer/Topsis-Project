import pathlib
from setuptools import setup
HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="Topsis-ishan-102313022",
    version="1.0.0",
    description="A Python package that implements the TOPSIS multi-criteria decision-making method.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Mickeyzer/Topsis-Project",
    author="Ishan Bhat",
    author_email="ishanbhat05@gmail.com",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3.8",
    ],
    packages=["topsis"],
    include_package_data=True,
    install_requires=[
        "pandas>=1.0.0",
        "numpy>=1.18.0",
    ],
    entry_points={
        "console_scripts": [
            "topsis=topsis.__main__:main",
        ],
    },
)