import requests
import time
import csv

proxies_to_test = [
    {
        "name": "Provider 1",
        "proxy": "http://USERNAME:PASSWORD@PROXY_HOST:PORT"
    },
    {
        "name": "Provider 2",
        "proxy": "http://USERNAME:PASSWORD@PROXY_HOST:PORT"
    }
]

test_url = "https://httpbin.org/ip"
requests_per_proxy = 5
timeout = 10

results = []

for item in proxies_to_test:
    provider_name = item["name"]
    proxy_url = item["proxy"]

    success_count = 0
    total_time = 0

    print(f"Testing {provider_name}...")

    for i in range(requests_per_proxy):
        proxies = {
            "http": proxy_url,
            "https": proxy_url
        }

        start_time = time.time()

        try:
            response = requests.get(test_url, proxies=proxies, timeout=timeout)
            elapsed_time = time.time() - start_time

            if response.status_code == 200:
                success_count += 1
                total_time += elapsed_time

        except requests.exceptions.RequestException:
            pass

    success_rate = (success_count / requests_per_proxy) * 100
    average_latency = total_time / success_count if success_count > 0 else None

    results.append({
        "provider": provider_name,
        "success_rate": success_rate,
        "average_latency_seconds": average_latency
    })

with open("proxy_benchmark_results.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["provider", "success_rate", "average_latency_seconds"])
    writer.writeheader()
    writer.writerows(results)

print("Benchmark complete. Results saved to proxy_benchmark_results.csv")
