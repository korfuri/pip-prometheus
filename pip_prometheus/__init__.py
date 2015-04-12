import pip
import prometheus_client
import sys


def LoadInstallations(counter):
    """Load installed packages and export the version map.

    This function may be called multiple times, but the counters will
    be increased each time. Since Prometheus counters are never
    decreased, the aggregated results will not make sense.
    """
    installations = pip.utils.get_installed_distributions()
    for i in installations:
        counter.labels(i.key, i.version).inc()


_installed_apps = prometheus_client.Counter(
    'pip_installed_apps_map',
    ('Map of installed packages as reported by PIP. Counter values are'
     'always 1, so the counters can be aggregated to express a count of '
     'targets that have a certain version of a certain package installed.'),
    ['package', 'version'])
# Load installations on import
LoadInstallations(_installed_apps)

_system_version = prometheus_client.Counter(
    'pip_system_components_map',
    ('Map of the versions various system components. Counter values are'
     'always 1, so the counters can be aggregated to express a count of '
     'targets that have a certain version of a certain package installed.'),
    ['component', 'version'])
_system_version.labels('python', sys.version).inc()
_system_version.labels('python_hexversion', sys.hexversion).inc()
_system_version.labels('capi', sys.api_version).inc()
_system_version.labels('platform', sys.platform).inc()
