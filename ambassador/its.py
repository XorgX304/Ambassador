import os
import sys

on_linux = sys.platform.startswith('linux')
"""Whether or not the current platform is Linux."""
on_windows = sys.platform.startswith('win')
"""Whether or not the current platform is Windows."""

py_v3 = sys.version_info[0] == 3
"""Whether or not the current Python version is 3.x."""
