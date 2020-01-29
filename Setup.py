import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyConnectify",
    version="0.0.1",
    author="Israel Cunha",
    author_email="ms.israel.cunha@gmail.com",
    description=" ... ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/israelcunha/PyConnectify",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3.6.5",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)