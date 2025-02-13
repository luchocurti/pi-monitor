# src/main.py
from monitoring import check_system

def main():
    print("Starting Pi Monitor...")
    check_system()

if __name__ == "__main__":
    main()
