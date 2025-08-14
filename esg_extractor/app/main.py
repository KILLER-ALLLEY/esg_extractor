import os

# Path to your project folder
project_root = "esg_extractor"

for root, dirs, files in os.walk(project_root):
    init_path = os.path.join(root, "__init__.py")
    if not os.path.exists(init_path):
        with open(init_path, "w", encoding="utf-8") as f:
            pass  # Empty file
        print(f"Created: {init_path}")

print("✅ All __init__.py files created.")
