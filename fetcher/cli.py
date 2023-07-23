import argparse
from fetcher import fetch

def main():
    parser = argparse.ArgumentParser(
        description="Simple and minimalistic fetching software, requires python 3 and nerdfonts"
    )
    parser.add_argument('-w', '--width', required=True)
    args = parser.parse_args()
    fetch(int(args.width))

if __name__ == "__main__":
    main()
