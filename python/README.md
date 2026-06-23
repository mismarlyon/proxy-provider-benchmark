# Python Proxy Benchmark

This folder contains a simple Python script for benchmarking residential proxy success rates and latency.

## File included

### proxy_benchmark.py
Tests proxy providers by sending repeated requests through each proxy and measuring:

- Success rate
- Average response time
- Failed requests

## Replace these values

```txt
USERNAME
PASSWORD
PROXY_HOST
PORT
Provider 1
Provider 2
```

## Run the script

Install requests:

```txt
pip install requests
```

Run:

```txt
python proxy_benchmark.py
```

## Output

The script creates:

```txt
proxy_benchmark_results.csv
```

## Notes
- Do not commit real proxy credentials.
- Use neutral provider names if publishing public results.
- Run tests responsibly and avoid sending excessive requests.
