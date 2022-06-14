#!../bin/python
"""Display top 10 packages with the most files.

Downloads the Contents file associated to a system architecture
passed as an argument and displays the top 10 packages having the
most files.
Author: Chris Hani.
"""
import argparse
from debian_package import PackageStats

# Create the parser
arg_parser = argparse.ArgumentParser(prog="package_statistics",
                                     description="Output the statistics\
                                    of the top 10 packages with the most\
                                    files associated with them for a\
                                    particular system architecture.",
                                     epilog="Enjoy the program! ;)")

# Add argument
arg_parser.add_argument("Arch",
                        metavar='arch',
                        type=str,
                        help='Architecture whose contents are to be\
                            downloaded and analyzed.')

# Execute the parse_args() method
args = arg_parser.parse_args()

package = PackageStats(args.Arch)
package_stats = package.get_package_stats()
print(f"\n{'#':>2}  {'Package':>30}\t{'File Count':>}\n")
for index, (package, file_count) in enumerate(package_stats, start=1):
    print(f"{index:>2}. {package:>30}\t{file_count:>5} files")
