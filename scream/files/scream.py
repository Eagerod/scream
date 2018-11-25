try:
    import configparser
except ImportError:
    import ConfigParser as configparser
import logging
import os

from .util import File
from ..package import Package, PackageDoesNotExistException
from ..utils import WHITELISTED_FILES

TEMPLATE = """\
[scream]
"""


class Scream(File):
    """
    This class knows how to write and fetch configs from the .scream config file.
    It is used for initializing and maintaining configurations.
    """

    def __init__(self, root_dir):
        """
        Args:
            root_dir (str): The directory of a valid scream monorepo.
        """
        self.root_dir = root_dir
        self.config = self.get_config(root_dir)['scream']

        # User provided configs (example for how we might set additional user configs here)
        # self.pyversions = [v.strip().replace('.', '') for v in self.config.get('pyversions').split(',')]

        # Autogenerated configs
        self.packages = self.get_packages(self.root_dir)

        super(Scream, self).__init__(
            '.scream',
            TEMPLATE.format()
        )

    @staticmethod
    def get_config(root_dir):
        config_path = os.path.join(root_dir, '.scream')
        if not os.path.isfile(config_path):
            raise IOError("{} does not contain a valid `.scream` file".format(root_dir))

        config = configparser.ConfigParser()
        config.read(config_path)

        return config

    @staticmethod
    def get_packages(root_dir):
        package_dirs = next(os.walk(root_dir))[1]

        packages = []
        for package in package_dirs:
            if package not in WHITELISTED_FILES:
                try:
                    p = Package(package_dir=package)
                except PackageDoesNotExistException:
                    logging.warning("{} is not a valid package. Skipping...".format(package))
                else:
                    packages.append(p)

        return packages
