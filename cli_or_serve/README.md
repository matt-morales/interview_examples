### CLI or Serve application

## Getting Started

You must have Python 3 downloaded, then run the following argument to download the dependencies. (Only 1 dependency used)

```bash
pip install -r requirements.txt
```

## Running the program

To see how to use the application, run the following command
```bash
```

# CLI Example

```bash
python -m cli_or_serve --aggregate sum 1 2 3
```

# Web Server Example

```bash
python -m cli_or_serve --aggregate sum --port 8080
```

Then you can make a request to the web server with the arguments:
```bash
curl 'localhost:8080?N=1+3+2+1'
```

