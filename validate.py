import os

print("🔍 Starting validation...")

if os.path.exists("README.md"):
    print("✅ README.md found")
else:
    print("❌ README.md is missing!")
    exit(1)  # exit code 1 = failure

print("✅ All checks passed!")
exit(0)  # exit code 0 = success
