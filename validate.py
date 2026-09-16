import os

print("🔍 Starting validation...")

# Check 1: README exists
if os.path.exists("README.md"):
    print("✅ README.md found")
else:
    print("❌ README.md is missing!")
    exit(1)

# ✨ NEW CHECK: Make sure a 'src' file exists
if os.path.exists("app.py"):
    print("✅ app.py found")
else:
    print("❌ app.py is missing!")
    exit(1)

print("✅ All checks passed!")
exit(0)
