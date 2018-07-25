#!/usr/bin/env python
import sys
import os
from cli.client.simple import Client

_config_file = os.getenv("KCLIENT_CONFIG", None)
_log_file = os.getenv("KCLIENT_LOG", None)


def main():
    d = Client()
    d.run(sys.argv[1:])

if __name__ == '__main__':
    main()
