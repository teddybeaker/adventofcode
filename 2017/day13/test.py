import unittest

from firewall import Firewall


class FirewallTest(unittest.TestCase):

    def test_smoke_severity(self):
        layers = {0: 3,
                  1: 2,
                  4: 4,
                  6: 4}
        firewall = Firewall(layers)
        severity = firewall.calculate_severity()
        self.assertEqual(severity, 24)  # 0*3 + 6*4

    def test_smoke_safe_path(self):
        layers = {0: 3,
                  1: 2,
                  4: 4,
                  6: 4}
        firewall = Firewall(layers)
        offset = firewall.get_safe_path()
        self.assertEqual(offset, 10)


if __name__ == '__main__':
    unittest.main()
