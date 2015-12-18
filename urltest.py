import requests
import argparse
import csv
import io


def test_url(url):
    """Perform a HTTP HEAD request to the provided URL.

    Args:
        url (str): The URL to test

    Returns:
        int: HTTP status code
    """
    try:
        r = requests.head(url)
        return r.status_code
    except Exception as e:
        return e


def test_urls(urls):
    results = []

    for url in urls:
        url = url.strip()
        status = test_url(url)
        results.append((url, status,))

    return results


def write_results_tab(results):
    for result in results:
        print("{}\t{}".format(*result))


def write_results_csv(results, f):
    writer = csv.writer(ouptut_buffer, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    writer.writerows(results)

    return f


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Check HTTP status of a number of URLs.')
    parser.add_argument('filename', type=str, help='an file with one URL per line')
    args = parser.parse_args()

    with open(args.filename) as f:
        results = test_urls(f)
        ouptut_buffer = io.StringIO()
        write_results_csv(results, ouptut_buffer)
        print(ouptut_buffer.getvalue())
