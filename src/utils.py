import os

def save_to_file(output_path, lines):
    try:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            for line in lines:
                f.write(line + "\n")
        print(f"\n✅ Results saved to: {output_path}")
    except Exception as e:
        print(f"❌ Could not save report: {e}")
