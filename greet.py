import sys

def greet(name):
    print(f"👋 Hello, {name}! Welcome to GitHub Actions.")

if __name__ == "__main__":
    name = sys.argv[1] if len(sys.argv) > 1 else "Developer"
    greet(name)
