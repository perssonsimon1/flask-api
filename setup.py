import os
from setuptools import setup

base_dir = os.path.dirname(__file__)

with open(os.path.join(base_dir, "README.md")) as f:
    long_description = f.read()

with open("requirements.txt") as f:
    install_requires = f.readlines()

os.environ['FLASK_APP'] = "app"

setup(
    name='app',
    long_description=long_description,
    author='Simon Persson',
    author_email='simon@akep.se',
    packages=['app', 'app.api', 'app.common'],
    install_requires=install_requires,
    include_package_data=True,
    classifiers=['Programming Language :: Python :: 3']
)
