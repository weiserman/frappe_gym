from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in frappe_gym/__init__.py
from frappe_gym import __version__ as version

setup(
	name="frappe_gym",
	version=version,
	description="Gym Management",
	author="Warren Eiserman",
	author_email="frappe@agile.co.za",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
