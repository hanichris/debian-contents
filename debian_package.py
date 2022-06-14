"""Class to download packages and return the top 10 by file count.

Author: Chris Hani.
"""
import gzip
import re
from collections import defaultdict
from io import BytesIO

import requests


class PackageStats:
    """PackageStats class for downloading packages from a Debian mirror.

    The PackageStats class downloads the packages and sorts them in
    descending order based on their file count. The top 10 packages
    obtained are returned in a list data structure with their
    corresponding file count.
    """

    def __init__(self, arch: str = '') -> None:
        """Initialize the PackageStats class.

        Attributes
        arch (str): system architecture of interest.
        base_url (str): url of the Debian mirror site.
        package_details (dict) : An architecture with its associated
        gzip file and gzip installation file.
        package_list (list): list of packages in sorted in descending order.
        """
        self.arch = arch
        self.base_url = "http://ftp.uk.debian.org/debian/dists/stable/main/"
        self.package_details = self._get_package_details()
        self.package_list = None

    def _get_package_details(self) -> None:
        """Retrieve package details from debian mirror site.

        Make a get request to the given url and preprocess the response
        obtained before building a json response from it that captures
        the details about the various packages.
        """
        response = requests.get(self.base_url)
        response = response.text.split("\r\n")
        return self._build_json_response(response)

    def _build_json_response(self, res: list):
        """Filter out the required keywords from the response.

        Process the input to filter out the necessary portions of the
        get response.
            res - list of strings containing preprocessed get request.
        """
        filtered_response = []
        for entry in res:
            if "Contents-" in entry and ".gz" in entry:
                filtered_response.append(entry)
        return self._build_json_data(filtered_response)

    def _build_json_data(self, res: list) -> dict[dict]:
        """Populate a json dataset with the response obtained.

        With the filtered response passed to the function, generate json
        data detailing the particular architecture and the information
        around it.
            res - List of responses that have been filtered to get
            relevant keywords.
        """
        json_data = defaultdict(dict)
        info_pat = re.compile(r"\"Contents-([a-z0-9]*)-?([a-z0-9]*).gz\"")
        arch_pat = re.compile(r"([a-z0-9]*).gz")
        for entry in res:
            info = info_pat.search(entry)[0].strip('\"')
            arch = arch_pat.search(info)[1]
            json_data = self._create_json(arch, info, json_data)
        return json_data

    def _create_json(self, arch: str, info: str,
                     json_data: dict) -> dict[dict]:
        """Build out the actual json dataset.

            arch - string name of the particular system architecture.
        info - string name pertaining to the zip file of the architecture.
        json_data - dict{dict}.
        """
        if "Contents-udeb" in info:
            json_data[arch]['udeb-zip_filename'] = info
        else:
            json_data[arch]['zip_filename'] = info
        return json_data

    def _download_packages(self, arch: str) -> gzip.GzipFile:
        """Download the gzip file from the mirror site.

        arch - string name of the particular system architecture.
        Return - gzip file descriptor.
        """
        url = self.base_url + self.package_details[arch]['zip_filename']
        content = BytesIO(requests.get(url).content)
        return gzip.open(content, "rt")

    def _get_package_and_filename(self, line: str) -> tuple:
        """Pick out the filename and package name from the downloaded file.

        line - string containing the name of the file and the package it is
        associated with.
        """
        packages = []
        info = line.split()
        if ',' in info[1]:
            package_list = info[1].split(',')
            for package in package_list:
                package = package.split('/')[-1]
                packages.append(package)
            return info[0], packages
        package = info[1].split('/')[-1]
        packages.append(package)
        return info[0], packages

    def _create_dict(self, packages: list, package_dict: dict) -> dict:
        """Create a dictionary from the package name and number of files."""
        for package in packages:
            if package not in package_dict:
                package_dict[package] = 1
            else:
                package_dict[package] += 1
        return package_dict

    def _build_package_list(self, package_details: gzip.GzipFile, arch: str):
        """Build a sorted list of packages with their file count."""
        package_dict = {}
        for line in package_details.readlines():
            filename, packages = self._get_package_and_filename(line)
            if filename != "EMPTY_PACKAGE":
                package_dict = self._create_dict(packages, package_dict)
        return sorted(package_dict.items(), key=lambda x: x[1], reverse=True)

    def get_package_stats(self):
        """Get the top 10 packages with the most files in descending order."""
        self.is_valid_arch(self.arch)
        package_data = self._download_packages(self.arch)
        self.package_list = self._build_package_list(package_data, self.arch)
        package_data.close()
        return self.package_list[:10]

    def get_archs(self) -> list:
        """Return a list of the recognized system architectures."""
        archs = self.package_details.keys()
        return archs

    def is_valid_arch(self, arch: str):
        """Determine whether the provided architecture is valid or not.

            The validity of the architecture is determined by whether an
        exception is raised or not. If an exception is raised, then the
        architecture in question is not recognized. However, if no
        exceptions are raised, then the architecture is valid.
        """
        if arch not in self.get_archs():
            raise Exception(
                f"{arch} is not a recognized system architecture.")
