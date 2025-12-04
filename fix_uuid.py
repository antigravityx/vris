import re
from pathlib import Path

# Files to update
files = [
    'app/models/chat.py',
    'app/models/event.py',
    'app/models/prediction.py'
]

for file_path in files:
    path = Path(file_path)
    if path.exists():
        content = path.read_text(encoding='utf-8')
        updated_content = re.sub(r'UUID\(as_uuid=True\)', 'UUID()', content)
        path.write_text(updated_content, encoding='utf-8')
        print(f"✅ Updated {file_path}")
    else:
        print(f"❌ File not found: {file_path}")

print("\n✨ All files updated!")
