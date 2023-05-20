NAME = "ia8"

import argparse
from typing import Callable, Tuple


def entry(options: argparse.Namespace):
    from certipy.commands import ia8

    ia8.entry(options)


def add_subparser(subparsers: argparse._SubParsersAction) -> Tuple[str, Callable]:
    subparser = subparsers.add_parser(NAME, help="NTLM Relay to AD CS HTTP Endpoints")

    subparser.add_argument(
        "-ca",
        action="store",
        metavar="hostname",
        required=True,
        help="IP address or hostname of certificate authority",
    )
    subparser.add_argument("-debug", action="store_true", help="Turn debug output on")
    group = subparser.add_argument_group("certificate request options")
    group.add_argument("-dns", action="store", metavar="alternative DNS")

    group.add_argument(
        "-key-size",
        action="store",
        metavar="RSA key length",
        help="Length of RSA key. Default: 2048",
        default=2048,
        type=int,
    )
    group = subparser.add_argument_group("connection options")

    group.add_argument(
        "-dc-ip",
        action="store",
        metavar="ip address",
        help="IP Address of the domain controller. If omitted it will use the domain part (FQDN) specified in "
             "the target parameter",
    )

    group = subparser.add_argument_group("server options")
    group.add_argument(
        "-interface",
        action="store",
        metavar="ip address",
        help="IP Address of interface to listen on",
        default="0.0.0.0",
    )
    group.add_argument(
        "-port",
        action="store",
        help="Port to listen on",
        default=445,
        type=int,
    )

    group = subparser.add_argument_group("connection options")
    group.add_argument(
        "-timeout",
        action="store",
        metavar="seconds",
        help="Timeout for connections",
        default=5,
        type=int,
    )

    return NAME, entry
