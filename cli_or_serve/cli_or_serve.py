import argparse
from flask import Flask, jsonify, request


parser = argparse.ArgumentParser(
    prog = 'cli_or_serve'
)

parser.add_argument(
    "-a",
    "--aggregate",
    type=str,
    help="The operation to run on the arguments: sum or max"
)

parser.add_argument(
    "-p",
    "--port",
    type=int,
    help="the port to run the web server"
)

parser.add_argument(
    "nums",
    type=int,
    nargs="*",
    help="the numbers to use in the operation (will be disregarded if port is provided)"
)

funcs = {
    "sum": sum,
    "max": max
}

def run_app(port, aggregate):
    app = Flask(__name__)

    @app.route("/")
    def serve_run():
        str_nums = request.args["N"].split(" ")
        nums = [int(num) for num in str_nums]

        res = run(aggregate, nums)

        return jsonify(res), 200

    app.run(port=port)

def run(name, args):
    return funcs[name](args)

if __name__ == "__main__":
    args = parser.parse_args()
    aggregate = args.aggregate
    nums = args.nums
    port = args.port
    if port:
        run_app(port, aggregate)
        print(f"Running on port {port}")
    else:
        print(run(aggregate, nums))

