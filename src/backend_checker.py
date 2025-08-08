import os
import re

def load_error_patterns(file_path):
    try:
        with open(file_path, 'r') as f:
            return [re.compile(rf'\b{line.strip()}\b', re.IGNORECASE) for line in f if line.strip()]
    except Exception as e:
        print(f"❌ Could not load error patterns: {e}")
        return []

def check_backend_logs(log_dir, patterns):
    issues = []
    for root, dirs, files in os.walk(log_dir):
        for file in files:
            if file.endswith(".log"):
                path = os.path.join(root, file)
                try:
                    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                        for line_num, line in enumerate(f, 1):
                            for pattern in patterns:
                                if pattern.search(line):
                                    issues.append(f"[{file} | Line {line_num}]: {line.strip()}")
                                    break
                except Exception as e:
                    print(f"❌ Could not read {path}: {e}")
    return issues
