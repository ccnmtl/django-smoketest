import os
from setuptools import setup

ROOT = os.path.abspath(os.path.dirname(__file__))

setup(
    name="django-smoketest",
    version="1.1.0",
    author="Anders Pearson",
    author_email="anders@columbia.edu",
    url="https://github.com/ccnmtl/django-smoketest",
    description="Django smoketest framework",
    long_description=open(os.path.join(ROOT, 'README.md')).read(),
    install_requires=['Django>=1.6', 'nose'],
    scripts=[],
    license="BSD",
    platforms=["any"],
    zip_safe=False,
    package_data = {'': ['*.*']},
    packages=['smoketest'],
    test_suite='nose.collector',
)
