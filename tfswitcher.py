#!/usr/bin/env python3
# Author: Rafael Romero Carmona <rafaelromcar@gmail.com>
import argparse
import re
import os
import sys


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
    parser.add_argument('version', metavar='X.Y.Z', help='The version of Terraform you want to use with the script.')

    args = parser.parse_args()
    switch_to_version(args.version)
