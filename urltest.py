"""Test URL accessibility."""

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
    """Test a list of URLs.

    Args:
        urls (iterable): A list of URLs to test.

    Returns:
        list: A list of tuples containing url and http status code, or Exception on failure.
    """
    results = []

    for url in urls:
        url = url.strip()
        status = test_url(url)
        results.append((url, status,))

    return results


def write_results_tab(results, f):
    """Write results as tab separated data to the provided file-like object.

    Args:
        results (list): A list of url/status tuples
        f (file): A file-like object to write to

    Returns:
        file: The file-like object provieded to the function
    """
    for result in results:
        f.write("{}\t{}\n".format(*result))
    return f


def write_results_csv(results, f):
    """Write results as CSV data to the provided file-like object.

    Args:
        results (list): A list of url/status tuples
        f (file): A file-like object to write to

    Returns:
        file: The file-like object provieded to the function
    """
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
