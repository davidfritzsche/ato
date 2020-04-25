# SPDX-FileCopyrightText: 2020 David Fritzsche
# SPDX-License-Identifier: Apache-2.0 OR MIT
import argparse
import sys


def main(argv=None) -> int:
    from . import __version__ as ato_version

    argv = argv if argv is not None else sys.argv
    p = argparse.ArgumentParser(prog="ato")
    p.add_argument("--version", action="version", version=f"{ato_version}")
    p.parse_args(args=argv[1:])
    return 0


if __name__ == "__main__":
    sys.exit(main())
