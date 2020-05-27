import os
from setuptools import setup

ROOT = os.path.abspath(os.path.dirname(__file__))

setup(
    name="django-smoketest",
    version="1.1.2",
    author="Anders Pearson",
    author_email="ctl-dev@columbia.edu",
    url="https://github.com/ccnmtl/django-smoketest",
    description="Django smoketest framework",
    long_description_content_type='text/markdown',
    long_description=open(os.path.join(ROOT, 'README.md')).read(),
    install_requires=['Django>=1.8'],
    scripts=[],
    license="BSD",
    platforms=["any"],
    zip_safe=False,
    package_data = {'': ['*.*']},
    packages=['smoketest'],
)
