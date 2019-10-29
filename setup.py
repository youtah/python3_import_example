import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="arrested_development",
    version="3.1.1",
    author="bluth",
    author_email="bluth@dev.null",
    description="example",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Linux Only"
    ],
    python_requires='>=3.6',
)