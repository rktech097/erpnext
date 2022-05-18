from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in erp/__init__.py
from erp import __version__ as version

setup(
	name="erp",
	version=version,
	description="erp",
	author="erp",
	author_email="erp",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
