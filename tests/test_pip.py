import unittest
import sys
from prometheus_client import REGISTRY
import pip_prometheus


class TestPipPrometheus(unittest.TestCase):
    def test_exportsPython(self):
        self.assertEquals(
            1, REGISTRY.get_sample_value(
                'pip_system_components_map',
                labels={
                    'component': 'python',
                    'version': sys.version,
                }
            )
        )


if __name__ == '__main__':
    unittest.main()
