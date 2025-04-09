def parse_headers(raw_headers):
    print("📧 Parsed Email Headers:\n")
    for line in raw_headers.splitlines():
        if line.startswith(("From:", "To:", "Subject:", "Date:", "Received:")):
            print(line)

if __name__ == "__main__":
    print("Paste full email headers below. Press Ctrl+D when done:")
    try:
        raw = ""
        while True:
            raw += input() + "\n"
    except EOFError:
        parse_headers(raw)
