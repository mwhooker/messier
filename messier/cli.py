import argparse


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="subparser_name")

    server_parser = subparsers.add_parser("server",
                                          description="Capdash server")
    server_parser.\
        add_argument("-l",
                     "--listen-address",
                     default="0.0.0.0",
                     dest="address",
                     metavar="ADDRESS",
                     help="Listen on this address [default=%(default)s]")
    server_parser.\
        add_argument("-p",
                     "--listen-port",
                     default=8000,
                     type=int,
                     dest="port",
                     metavar="PORT",
                     help="Listen on this port [default=%(default)s]")

    args = parser.parse_args()

    if args.subparser_name == "server":
        server(args.address, args.port)


def server(address, port):
    import messier
    messier.app.run(host=address, port=port)


if __name__ == "__main__":
    main()
