__author__ = 'mbach'

import unittest

from devpi_builder.cli import main
from devpi_builder import devpi

from tests.tools import devpi_server, devpi_index


class CliTest(unittest.TestCase):
    def test_basic(self):
        with devpi_server() as server_url, devpi_index(server_url, 'test', 'wheels') as (destination_index, password):
            main(['tests/sample_simple.txt', destination_index])

            devpi_client = devpi.Client(destination_index)
            self.assert_(devpi_client.package_version_exists('progressbar', '2.2'))


if __name__ == '__main__':
    unittest.main()