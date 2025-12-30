#pyinstaller --onefile --name my_exe my_exe.py
import sys
import argparse
from datetime import datetime
from reg import Registry
import numpy as np
def main():
    parser = argparse.ArgumentParser(description="Process a filename and a date.")
    parser.add_argument("filename", help="The name of the file to work on")
    parser.add_argument("date", help="The date to work on (format: YYYY-MM-DD)")

    args = parser.parse_args()

    # Optional: Validate the date format
    try:
        parsed_date = datetime.strptime(args.date, "%Y-%m-%d")
        print(f"File: {args.filename}")
        print(f"Date: {parsed_date.strftime('%Y-%m-%d')} (valid)")
    except ValueError:
        print(f"Error: '{args.date}' is not a valid date in YYYY-MM-DD format.")
        sys.exit(1)
        
    # License
    for file in [args.filename]:
        d = Registry.restore(file)
        print(d)
        d.xcode(np.random.choice(['346A','346B']))
        d.d_mac["expiry_date"] = parsed_date.strftime('%Y-%m-%d')
        d.d_mac["expired"] = "no"
        reg = Registry(**d.d_mac)
        reg.update()
        print(reg.check_xcode())
        print(reg.check_exp_date())
        print(reg.d_mac)

if __name__ == "__main__":
    main()