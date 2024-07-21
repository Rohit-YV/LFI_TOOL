import argparse
import requests
import sys
import time

def read_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def read_stdin():
    return [line.strip() for line in sys.stdin]

def check_lfi(url, payloads, delay):
    for payload in payloads:
        test_url = url.replace("abcd", payload)
        print(f"Testing: {test_url}")
        try:
            response = requests.get(test_url)
            if response.status_code == 200:
                if "root:x:" in response.text:
                    print(f"LFI Vulnerability found with payload: {payload}")
                    return
            else:
                print(f"Received status code: {response.status_code}")
        except requests.RequestException as e:
            print(f"Error: {e}")
        time.sleep(delay)  # Add delay between requests
    
    print("LFI vulnerability not found")

def main(urls, payload_file, delay):
    payloads = read_file(payload_file)

    for url in urls:
        print(f"Checking URL: {url}")
        check_lfi(url, payloads, delay)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="LFI Checker")
    parser.add_argument("-u", "--urls", help="File containing list of URLs")
    parser.add_argument("-p", "--payloads", required=True, help="File containing list of payloads")
    parser.add_argument("-d", "--delay", type=float, default=1.0, help="Delay between requests in seconds")
    args = parser.parse_args()

    if args.urls:
        urls = read_file(args.urls)
    else:
        urls = read_stdin()

    main(urls, args.payloads, args.delay)
