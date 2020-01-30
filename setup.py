# from setuptools import setup, find_packages
#
# setup(
#     name='pyconnectify',
#     version='0.0.3',
#     url='https://gitlab.com/israelcunha/PyConnectify',
#     license='MIT License',
#     author='Israel Cunha',
#     author_email='ms.israel.cunha@gmail.com',
#     keywords='ssh utp tcp tar redes network',
#     description=u'Telecommunication and file management application',
#     packages=find_packages(exclude=['venv']),
#     long_description_content_type="text/markdown",
#     long_description=open('README.md').read(),
#     install_requires=[],
# )

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyconnectify",
    version="0.0.3.1",
    author="Israel Cunha",
    author_email="ms.israel.cunha@gmail.com",
    keywords='ssh utp tcp tar redes network',
    description="Telecommunication and file management application",
    license='MIT License',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/israelcunha/PyConnectify",
    packages=setuptools.find_packages(exclude=['venv']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
