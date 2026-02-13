import requests
import time
import os

# Configuration
API_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9wZmEuZm9yZWNhLmNvbVwvYXV0aG9yaXplXC90b2tlbiIsImlhdCI6MTc3MDM3ODIxMywiZXhwIjo5OTk5OTk5OTk5LCJuYmYiOjE3NzAzNzgyMTMsImp0aSI6IjQwNjQ3NTUzYWQ3ZjYyNjEiLCJzdWIiOiJla2VrYXoiLCJmbXQiOiJYRGNPaGpDNDArQUxqbFlUdGpiT2lBPT0ifQ.7BqUkDXZ_Swqd_nEz2NSYT4w3OK-3kR33JRFHx5n_J0"  # Replace with your valid token
BASE_URL = "https://pfa.foreca.com"
INPUT_FILE = "City.cfg"   # Your file in the format "Country/City"
OUTPUT_FILE = "new_city.cfg"


def search_city_id(original_search_string):
    """
    Searches for a location ID. Tries multiple query strategies.
    """
    import re
    import urllib.parse

    # 1. Extract and clean parts from the original line (e.g.
    # 'Estonia/Kohtla-Järve')
    parts = [p.strip() for p in original_search_string.split('/') if p.strip()]
    if len(parts) < 2:
        return None

    target_country = parts[0]   # 'Estonia'
    city_name_raw = parts[-1]   # 'Kohtla-Järve'

    # 2. CRITICAL CLEANUP: remove hyphens FROM THE CITY NAME for searching
    #    but keep the original name for the final output format.
    #    Convert 'Kohtla-Järve' into 'Kohtla Järve' for the query.
    city_name_for_query = city_name_raw.replace(
        '-', ' ').replace('_', ' ').strip()
    # Also remove any parentheses
    city_name_for_query = re.sub(r'\s*\(.*?\)', '', city_name_for_query)

    # 3. Define search strategies using the CLEANED name
    search_strategies = [
        city_name_for_query,                          # 1. Clean name: 'Kohtla Järve'
        # 2. 'Kohtla Järve, Estonia'
        f"{city_name_for_query}, {target_country}",
        # 3. 'Kohtla Järve Estonia'
        f"{city_name_for_query} {target_country}",
    ]

    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    found_locations = None

    # 4. TRY SEARCH STRATEGIES
    for query in search_strategies:
        print(f"  Search attempt: '{query}'")
        url = f"{BASE_URL}/api/v1/location/search/{urllib.parse.quote(query)}"
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            data = response.json()
            if data.get('locations'):
                found_locations = data['locations']
                print(f"     Found {len(found_locations)} results.")
                break
            time.sleep(0.1)
        except Exception as e:
            print(f"     Search error: {e}")
            continue

    # 5. IF RESULTS FOUND, SELECT AND FORMAT
    if not found_locations:
        print(f"  Failed: no results for {city_name_for_query}.")
        return None

    selected_location = None
    for loc in found_locations:
        if target_country.lower() in loc.get('country', '').lower():
            selected_location = loc
            break

    if not selected_location:
        print(
            f"  Warning: no result for country '{target_country}'. Using the first available result.")
        selected_location = found_locations[0]

    # 6. BUILD FINAL FORMAT STRING
    city_id = selected_location['id']
    # Use the ORIGINAL city name for output, preserving hyphens
    final_name = selected_location['name'].replace(' ', '-')
    final_country = selected_location['country'].replace(' ', '-')
    new_entry = f"{city_id}/{final_name}-{final_country}"

    print(f"     Success: {new_entry}")
    return new_entry


def main():
    if not os.path.exists(INPUT_FILE):
        print(f"Input file '{INPUT_FILE}' not found.")
        return

    migrated_count = 0
    skipped_count = 0
    total_requests = 0  # To monitor the 1000/day limit

    with open(INPUT_FILE, 'r', encoding='utf-8') as infile, \
            open(OUTPUT_FILE, 'w', encoding='utf-8') as outfile:

        for line_num, original_line in enumerate(infile, 1):
            original_line = original_line.strip()

            # Copy comments and empty lines as-is
            if not original_line or original_line.startswith('#'):
                outfile.write(original_line + '\n')
                continue

            try:
                # Keep the ORIGINAL line for the search function
                original_for_search = original_line  # "Albania/Berat"

                # Extract parts for logic/validation if needed (optional)
                parts = original_line.split('/')
                if len(parts) < 2:
                    print(f"  Invalid format, skipping: '{original_line}'")
                    outfile.write(f"# INVALID FORMAT: {original_line}\n")
                    skipped_count += 1
                    continue

                print(f"[{line_num}] Searching: {parts[-1]} ({parts[0]})...")

                total_requests += 1
                # PASS THE ORIGINAL LINE TO THE FUNCTION
                new_entry = search_city_id(original_for_search)

                if new_entry:
                    outfile.write(new_entry + '\n')
                    outfile.flush()  # <-- FORCE WRITE TO DISK NOW
                    migrated_count += 1
                    print(f"     -> Found and SAVED: {new_entry}")
                else:
                    outfile.write(f"# MIGRATION FAILED: {original_line}\n")
                    outfile.flush()  # <-- FORCE WRITE TO DISK NOW
                    skipped_count += 1

                # Pause to respect API limits
                time.sleep(0.1)

            except Exception as e:
                print(f"[{line_num}] Error processing line '{original_line}': {e}")
                outfile.write(f"# PROCESSING ERROR: {original_line}\n")
                skipped_count += 1

    print(f"\n--- Migration completed ---")
    print(f"Cities successfully migrated: {migrated_count}")
    print(f"Cities skipped/not found: {skipped_count}")
    print(f"Estimated total API requests: {total_requests}")
    print(f"New file saved as: {OUTPUT_FILE}")
    if total_requests >= 950:
        print(
            "⚠️  Warning: You have used over 950 requests today. Respect the daily limit.")


if __name__ == "__main__":
    main()
