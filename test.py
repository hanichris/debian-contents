"""Class to test the methods of the PackageStats class.

Author: Chris Hani.
"""
import gzip
import unittest
from io import BytesIO

import requests

from debian_package import PackageStats


class testPackageStatsClass(unittest.TestCase):
    """testPackageStatsClass tests the various methods of PackageStats."""

    def setUp(self) -> None:
        """Initialize the various variables to be used throughout the test."""
        self.package = PackageStats('amd64')
        self.key_tuple = ('amd64', 'arm64', 'armel',
                          'armhf', 'i386', 'mips64el',
                          'mipsel', 'ppc64el', 's390x')

    def tearDown(self) -> None:
        """Clean up the variables after the test method has run."""
        self.package = None
        self.key_tuple = None

    def test_initialization(self) -> None:
        """Test the initialization of the class with string 'amd64'."""
        self.assertEqual(self.package.arch, 'amd64', 'Incorrect architecture')
        for element in self.key_tuple:
            self.assertIn(element, self.package.package_details)

    def test_get_archs(self) -> None:
        """Check the architectures that are available at the given url."""
        arch_list = self.package.get_archs()
        for element in self.key_tuple:
            self.assertIn(element, arch_list)

    def test_is_valid_arch(self) -> None:
        """Test to raise an exception.

        Check whether an exception is raised when an unrecognized
        system architecture is encountered.
        """
        arch = 'Not an architecture'
        with self.assertRaises(Exception) as cm:
            self.package.is_valid_arch(arch)
        self.assertTrue(
            f"{arch} is not a recognized system architecture." in
            str(cm.exception)
        )

    def test_get_amd64_stats(self) -> None:
        """Ensure that piglit is the package with the most files.

        Confirm that piglit is a package and that it is the package
        with the most files. Checks to ensure that the returned list
        is 10 elements long and is in descending order.
        """
        stats = self.package.get_package_stats()
        self.assertEqual(stats[0][0], "piglit")
        self.assertTrue(stats[0][1] > stats[1][1])
        self.assertTrue(stats[9][1] < stats[8][1])
        self.assertEqual(len(stats), 10)

        # Verify that piglit is infact a package
        url = self.package.base_url + "binary-amd64/Packages.gz"
        content = BytesIO(requests.get(url).content)
        data = gzip.open(content, "rt")
        info = data.read()
        data.close()
        self.assertTrue("Package: piglit" in info)

        # Verify the count of piglit package
        url = self.package.base_url + "Contents-amd64.gz"
        content = BytesIO(requests.get(url).content)
        data = gzip.open(content, "rt")
        info = data.read()
        data.close()
        self.assertEqual(info.count("devel/piglit"), stats[0][1])

    def test_get_arm64_stats(self) -> None:
        """Ensure that piglit is the package with the most files.

        Confirm that piglit is a package and that it is the package
        with the most files. Checks to ensure that the returned list
        is 10 elements long and is in descending order.
        """
        self.package.arch = 'arm64'
        stats = self.package.get_package_stats()
        self.assertEqual(stats[0][0], "piglit")
        self.assertTrue(stats[0][1] > stats[1][1])
        self.assertTrue(stats[9][1] < stats[8][1])
        self.assertEqual(len(stats), 10)

        # Verify that piglit is infact a package
        url = self.package.base_url + "binary-arm64/Packages.gz"
        content = BytesIO(requests.get(url).content)
        data = gzip.open(content, "rt")
        info = data.read()
        data.close()
        self.assertTrue("Package: piglit" in info)

        # Verify the count of piglit package
        url = self.package.base_url + "Contents-arm64.gz"
        content = BytesIO(requests.get(url).content)
        data = gzip.open(content, "rt")
        info = data.read()
        data.close()
        self.assertEqual(info.count("devel/piglit"), stats[0][1])

    def test_get_armel_stats(self) -> None:
        """Ensure that piglit is the package with the most files.

        Confirm that piglit is a package and that it is the package
        with the most files. Checks to ensure that the returned list
        is 10 elements long and is in descending order.
        """
        self.package.arch = 'armel'
        stats = self.package.get_package_stats()
        self.assertEqual(stats[0][0], "piglit")
        self.assertTrue(stats[0][1] > stats[1][1])
        self.assertTrue(stats[9][1] < stats[8][1])
        self.assertEqual(len(stats), 10)

        # Verify that piglit is infact a package
        url = self.package.base_url + "binary-armel/Packages.gz"
        content = BytesIO(requests.get(url).content)
        data = gzip.open(content, "rt")
        info = data.read()
        data.close()
        self.assertTrue("Package: piglit" in info)

        # Verify the count of piglit package
        url = self.package.base_url + "Contents-armel.gz"
        content = BytesIO(requests.get(url).content)
        data = gzip.open(content, "rt")
        info = data.read()
        data.close()
        self.assertEqual(info.count("devel/piglit"), stats[0][1])

    def test_get_armhf_stats(self) -> None:
        """Ensure that piglit is the package with the most files.

        Confirm that piglit is a package and that it is the package
        with the most files. Checks to ensure that the returned list
        is 10 elements long and is in descending order.
        """
        self.package.arch = 'armhf'
        stats = self.package.get_package_stats()
        self.assertEqual(stats[0][0], "piglit")
        self.assertTrue(stats[0][1] > stats[1][1])
        self.assertTrue(stats[9][1] < stats[8][1])
        self.assertEqual(len(stats), 10)

        # Verify that piglit is infact a package
        url = self.package.base_url + "binary-armhf/Packages.gz"
        content = BytesIO(requests.get(url).content)
        data = gzip.open(content, "rt")
        info = data.read()
        data.close()
        self.assertTrue("Package: piglit" in info)

        # Verify the count of piglit package
        url = self.package.base_url + "Contents-armhf.gz"
        content = BytesIO(requests.get(url).content)
        data = gzip.open(content, "rt")
        info = data.read()
        data.close()
        self.assertEqual(info.count("devel/piglit"), stats[0][1])

    def test_get_i386_stats(self) -> None:
        """Ensure that piglit is the package with the most files.

        Confirm that piglit is a package and that it is the package
        with the most files. Checks to ensure that the returned list
        is 10 elements long and is in descending order.
        """
        self.package.arch = 'i386'
        stats = self.package.get_package_stats()
        self.assertEqual(stats[0][0], "piglit")
        self.assertTrue(stats[0][1] > stats[1][1])
        self.assertTrue(stats[9][1] < stats[8][1])
        self.assertEqual(len(stats), 10)

        # Verify that piglit is infact a package
        url = self.package.base_url + "binary-i386/Packages.gz"
        content = BytesIO(requests.get(url).content)
        data = gzip.open(content, "rt")
        info = data.read()
        data.close()
        self.assertTrue("Package: piglit" in info)

        # Verify the count of piglit package
        url = self.package.base_url + "Contents-i386.gz"
        content = BytesIO(requests.get(url).content)
        data = gzip.open(content, "rt")
        info = data.read()
        data.close()
        self.assertEqual(info.count("devel/piglit"), stats[0][1])

    def test_get_mips64el_stats(self) -> None:
        """Ensure that piglit is the package with the most files.

        Confirm that piglit is a package and that it is the package
        with the most files. Checks to ensure that the returned list
        is 10 elements long and is in descending order.
        """
        self.package.arch = 'mips64el'
        stats = self.package.get_package_stats()
        self.assertEqual(stats[0][0], "piglit")
        self.assertTrue(stats[0][1] > stats[1][1])
        self.assertTrue(stats[9][1] < stats[8][1])
        self.assertEqual(len(stats), 10)

        # Verify that piglit is infact a package
        url = self.package.base_url + "binary-mips64el/Packages.gz"
        content = BytesIO(requests.get(url).content)
        data = gzip.open(content, "rt")
        info = data.read()
        data.close()
        self.assertTrue("Package: piglit" in info)

        # Verify the count of piglit package
        url = self.package.base_url + "Contents-mips64el.gz"
        content = BytesIO(requests.get(url).content)
        data = gzip.open(content, "rt")
        info = data.read()
        data.close()
        self.assertEqual(info.count("devel/piglit"), stats[0][1])

    def test_get_mipsel_stats(self) -> None:
        """Ensure that piglit is the package with the most files.

        Confirm that piglit is a package and that it is the package
        with the most files. Checks to ensure that the returned list
        is 10 elements long and is in descending order.
        """
        self.package.arch = 'mipsel'
        stats = self.package.get_package_stats()
        self.assertEqual(stats[0][0], "piglit")
        self.assertTrue(stats[0][1] > stats[1][1])
        self.assertTrue(stats[9][1] < stats[8][1])
        self.assertEqual(len(stats), 10)

        # Verify that piglit is infact a package
        url = self.package.base_url + "binary-mipsel/Packages.gz"
        content = BytesIO(requests.get(url).content)
        data = gzip.open(content, "rt")
        info = data.read()
        data.close()
        self.assertTrue("Package: piglit" in info)

        # Verify the count of piglit package
        url = self.package.base_url + "Contents-mipsel.gz"
        content = BytesIO(requests.get(url).content)
        data = gzip.open(content, "rt")
        info = data.read()
        data.close()
        self.assertEqual(info.count("devel/piglit"), stats[0][1])

    def test_get_ppc64el_stats(self) -> None:
        """Ensure that piglit is the package with the most files.

        Confirm that piglit is a package and that it is the package
        with the most files. Checks to ensure that the returned list
        is 10 elements long and is in descending order.
        """
        self.package.arch = 'ppc64el'
        stats = self.package.get_package_stats()
        self.assertEqual(stats[0][0], "piglit")
        self.assertTrue(stats[0][1] > stats[1][1])
        self.assertTrue(stats[9][1] < stats[8][1])
        self.assertEqual(len(stats), 10)

        # Verify that piglit is infact a package
        url = self.package.base_url + "binary-ppc64el/Packages.gz"
        content = BytesIO(requests.get(url).content)
        data = gzip.open(content, "rt")
        info = data.read()
        data.close()
        self.assertTrue("Package: piglit" in info)

        # Verify the count of piglit package
        url = self.package.base_url + "Contents-ppc64el.gz"
        content = BytesIO(requests.get(url).content)
        data = gzip.open(content, "rt")
        info = data.read()
        data.close()
        self.assertEqual(info.count("devel/piglit"), stats[0][1])

    def test_get_s390x_stats(self) -> None:
        """Ensure that piglit is the package with the most files.

        Confirm that piglit is a package and that it is the package
        with the most files. Checks to ensure that the returned list
        is 10 elements long and is in descending order.
        """
        self.package.arch = 's390x'
        stats = self.package.get_package_stats()
        self.assertEqual(stats[0][0], "piglit")
        self.assertTrue(stats[0][1] > stats[1][1])
        self.assertTrue(stats[9][1] < stats[8][1])
        self.assertEqual(len(stats), 10)

        # Verify that piglit is infact a package
        url = self.package.base_url + "binary-s390x/Packages.gz"
        content = BytesIO(requests.get(url).content)
        data = gzip.open(content, "rt")
        info = data.read()
        data.close()
        self.assertTrue("Package: piglit" in info)

        # Verify the count of piglit package
        url = self.package.base_url + "Contents-s390x.gz"
        content = BytesIO(requests.get(url).content)
        data = gzip.open(content, "rt")
        info = data.read()
        data.close()
        self.assertEqual(info.count("devel/piglit"), stats[0][1])


if __name__ == '__main__':
    unittest.main()
