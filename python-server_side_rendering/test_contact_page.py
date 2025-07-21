#!/usr/bin/env python3
import urllib.request

def test_contact_page():
    try:
        with urllib.request.urlopen("http://127.0.0.1:5000/contact") as response:
            content = response.read().decode('utf-8')
            assert 'Contact Us' in content, "Failed: Contact page content mismatch"
            print("Test passed.")
    except Exception as e:
        print(f"Test failed: {e}")

if __name__ == "__main__":
    test_contact_page()
