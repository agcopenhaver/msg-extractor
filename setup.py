import os
import sys
from setuptools import setup
import re


# a handful of variables that are used a couple of times
github_url = 'https://github.com/mattgwwalker/msg-extractor'
main_module = 'extract_msg'
# main_script = main_module + '.py'

# read in the description from README
if os.name=='nt' and sys.version_info[0] >= 3:
    with open("README.rst", encoding='utf-8') as stream:
        long_description = stream.read()
else:
    with open("README.rst") as stream:
        long_description = stream.read()
# get the version from the ExtractMsg script. This can not be directly
# imported because ExtractMsg imports olefile, which may not be installed yet
version_re = re.compile("__version__ = '(?P<version>[0-9\.]*)'")
with open('extract_msg/__init__.py', 'r') as stream:
    contents = stream.read()
match = version_re.search(contents)
version = match.groupdict()['version']

# read in the dependencies from the virtualenv requirements file
dependencies = []
filename = os.path.join("requirements.txt")
with open(filename, 'r') as stream:
    for line in stream:
        package = line.strip().split('#')[0]
        if package:
            dependencies.append(package)

setup(
    name=main_module,
    version=version,
    description="Extracts emails and attachments saved in Microsoft Outlook's .msg files",
    long_description=long_description,
    url=github_url,
    download_url="%s/archives/master" % github_url,
    author='Matthew Walker & The Elemental of Creation',
    author_email='mattgwwalker@gmail.com, arceusthe@gmail.com',
    license='GPL',
    packages=[main_module],
    py_modules=[main_module],
    include_package_data=True,
    install_requires=dependencies,
)
