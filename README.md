# pip-prometheus
Export the version of Pip packages to Prometheus.io

[![PyPI version](https://badge.fury.io/py/pip-prometheus.svg)](http://badge.fury.io/py/pip-prometheus)
[![Build Status](https://travis-ci.org/korfuri/pip-prometheus.svg?branch=master)](https://travis-ci.org/korfuri/pip-prometheus)

## Usage

Simply `import pip_prometheus` to register the metrics.

See the [prometheus_client documentation](https://github.com/prometheus/client_python) to see how to export the
metrics via an HTTP server. If you're using Django, check out
[django-prometheus](https://github.com/korfuri/django-prometheus) which can export metrics to a Django view, and
exports metrics relevant to Django.

To aggregate the exported variables, see the [Prometheus.io documentation](http://prometheus.io/).
