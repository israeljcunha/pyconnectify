# import setuptools
#
# with open("README.md", "r") as fh:
#     long_description = fh.read()
#
# setuptools.setup(
#     name="pyconnectify",
#     version="0.1",
#     author="Israel Cunha",
#     author_email="ms.israel.cunha@gmail.com",
#     description=" ... ",
#     long_description=long_description,
#     long_description_content_type="text/markdown",
#     url="https://gitlab.com/israelcunha/PyConnectify",
#     packages=setuptools.find_packages(exclude=['venv']),
#     classifiers=(
#         "Programming Language :: Python :: 3.7.5",
#         "License :: OSI Approved :: MIT License",
#         "Operating System :: OS Independent",
#     ),
#     zip_safe=False,
#     setup_requires=['nose>=1.0'],
# )

from setuptools import setup

setup(
    name='pyconnectify',
    version='0.0.2',
    url='https://gitlab.com/israelcunha/PyConnectify',
    license='MIT License',
    author='Israel Cunha',
    author_email='ms.israel.cunha@gmail.com',
    keywords='ssh utp tcp tar redes network',
    description=u'Telecommunication and file management application',
    packages=['pyconnectify'],
    long_description=open('README.md').read(),
    install_requires=[],
)