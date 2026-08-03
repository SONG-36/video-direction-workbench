import unittest

import video_direction_workbench


class PackageSmokeTest(unittest.TestCase):
    def test_package_version(self) -> None:
        self.assertEqual(video_direction_workbench.__version__, "0.1.0")


if __name__ == "__main__":
    unittest.main()
