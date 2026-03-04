import sys, csv
def analyze(filepath):
    try:
        with open(filepath, 'r') as f:
            data = list(csv.DictReader(f))
            tools = [row.get('Tool', '') for row in data if row.get('Tool')]
            dupes = set([x for x in tools if tools.count(x) > 1])
            print(f"Records analyzed: {len(data)} | Duplicate Tools Found: {dupes}")
    except Exception as e: print(f"Error: {e}")
if __name__ == "__main__":
    if len(sys.argv) > 1: analyze(sys.argv[1])
