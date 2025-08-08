from src.backend_checker import load_error_patterns, check_backend_logs
from src.ui_checker import load_endpoints, check_endpoints
from src.utils import save_to_file

PATTERN_FILE = "config/error_patterns.txt"
LOG_DIR = "logs"  # Change to /var/log/opsmx for real usage
ENDPOINT_FILE = "config/endpoints.txt"
OUTPUT_FILE = "output/ssd_issues_report.txt"

def main():
    print("🔍 Starting OpsMx SSD Bug Scanner...")

    # Backend
    print("\n🔧 Checking backend logs...")
    patterns = load_error_patterns(PATTERN_FILE)
    backend_issues = check_backend_logs(LOG_DIR, patterns)

    # UI / API
    print("\n🌐 Checking UI/API endpoints...")
    endpoints = load_endpoints(ENDPOINT_FILE)
    ui_issues = check_endpoints(endpoints)

    # Combine
    all_issues = backend_issues + ui_issues

    if all_issues:
        print(f"\n❗ Found {len(all_issues)} issues.")
        for issue in all_issues:
            print(issue)
        save_to_file(OUTPUT_FILE, all_issues)
    else:
        print("✅ No issues found.")

if __name__ == "__main__":
    main()
