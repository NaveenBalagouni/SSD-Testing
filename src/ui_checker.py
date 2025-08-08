import requests

def load_endpoints(file_path):
    try:
        with open(file_path, 'r') as f:
            return [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"❌ Could not load endpoints: {e}")
        return []

def check_endpoints(endpoints):
    errors = []
    for url in endpoints:
        try:
            response = requests.get(url, timeout=5)
            if response.status_code != 200:
                errors.append(f"❌ {url} returned {response.status_code}")
        except Exception as e:
            errors.append(f"❌ {url} unreachable: {e}")
    return errors
