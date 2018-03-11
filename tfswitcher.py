#!/usr/bin/env python3
# Author: Rafael Romero Carmona <rafaelromcar@gmail.com>
import argparse
import re
import os
import sys


def remove_version(version):
    """
    Remove the given version if it is installed
    :param version:
    """
    # Paths
    link_path = "/usr/local/bin/terraform"
    terraform_install_folder = "/usr/local/bin/"
    version_path = terraform_install_folder + "terraform-" + version

    # Check if the version is using the correct syntax
    pattern = re.compile(r"\d+\.\d+\.\d+")
    if pattern.match(version) is None:
        print("The version should have the format NUMBER.NUMBER.NUMBER")
        sys.exit(1)

    # Check if the version is the one linked, remove the link in that case
    if os.path.exists(link_path) and version in os.readlink(link_path):
        try:
            os.remove(link_path)
        except PermissionError:
            print("The user does not have permissions on the link path {}".format(link_path))
            sys.exit(1)

    # Remove the version if it is present on the system
    if os.path.exists(version_path):
        try:
            os.remove(version_path)
            print("Version removed.")
        except PermissionError:
            print("The user does not have permissions on the version path {}".format(version_path))
            sys.exit(1)
    else:
        print("The version is not installed on the system.")


def switch_to_version(version):
    """
    Create a symlink on /usr/local/bin/terraform to the version /usr/local/bin/terraform-VERSION
    """
    # Paths
    link_destination = "/usr/local/bin/terraform"
    terraform_install_folder = "/usr/local/bin/"
    version_path = terraform_install_folder + "terraform-" + version

    # Parse the arg to be sure the version has the good format
    pattern = re.compile(r"\d+\.\d+\.\d+")
    if pattern.match(version) is None:
        print("Switch not possible.\nThe version should have the format NUMBER.NUMBER.NUMBER")
        sys.exit(1)

    # Check if version exists on the system
    if not os.path.exists(version_path):
        print("Switch not possible.\nThe version you want to use must be installed before on the path {}".format(version_path))
        sys.exit(1)

    # Remove the old symlink
    if os.path.exists(link_destination):
        try:
            os.remove(link_destination)
        except PermissionError:
            print("The user does not have permissions on the destination path for the link {}".format(link_destination))
            sys.exit(1)

    # Link the terraform path to the wished version
    try:
        os.symlink(version_path, link_destination)
    except PermissionError:
        print("The user does not have permissions on the destination path for the link {}".format(link_destination))
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='This script switches between Terraform versions.')
    parser.add_argument("--remove", dest="remove", action="store_true",
                        help="Add the flag to uninstall the given version, if it is installed on the system.")
    parser.add_argument('version', metavar='X.Y.Z', help='The version of Terraform you want to use with the script.')

    args = parser.parse_args()
    if args.remove:
        remove_version(version=args.version)
    else:
        switch_to_version(args.version)
