import os
from setuptools import setup

LONG_DESCRIPTION = """Pip-Prometheus

This code exports the version of installed Pip packages.

See https://github.com/korfuri/pip-prometheus for usage
instructions.
"""

setup(
    name="pip-prometheus",
    version="1.2.1",
    author="Uriel Corfa",
    author_email="uriel@corfa.fr",
    description=(
        "Exports Pip packages versions for Prometheus.io."),
    license="Apache",
    keywords="python pip monitoring prometheus",
    url="http://github.com/korfuri/pip-prometheus",
    packages=["pip_prometheus"],
    test_suite="tests",
    long_description=LONG_DESCRIPTION,
    install_requires=[
        "prometheus_client>=0.7.0",
        "pip>=9.0.0",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "Topic :: System :: Monitoring",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
