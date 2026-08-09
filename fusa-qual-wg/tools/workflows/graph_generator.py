import base64
import os
import requests
import glob
import sys

OUTPUT_DIR = "generated_graph"

def render_mermaid_to_png(mmd_file_path):
    # Extract just the filename without any folder paths or extensions
    base_name = os.path.splitext(os.path.basename(mmd_file_path))[0]

    # Route the output file into the new directory
    output_png_path = os.path.join(OUTPUT_DIR, f"{base_name}.png")
    print(f"Processing: {mmd_file_path} -> {output_png_path}")

    try:
        with open(mmd_file_path, "r", encoding="utf-8") as f:
            graph_code = f.read()

        graphbytes = graph_code.encode("utf8")
        base64_bytes = base64.urlsafe_b64encode(graphbytes)
        base64_string = base64_bytes.decode("ascii")

        api_url = f"https://mermaid.ink/img/{base64_string}"
        response = requests.get(api_url)
        response.raise_for_status() 

        with open(output_png_path, "wb") as f_out:
            f_out.write(response.content)

        print(f"Successfully saved: {output_png_path}")
        return True

    except Exception as e:
        print(f"Error processing {mmd_file_path}: {e}", file=sys.stderr)
        return False

if __name__ == '__main__':
    # Create the target folder if it doesn't exist yet
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Check if specific filenames were passed in the terminal
    if len(sys.argv) > 1:
        mmd_files = sys.argv[1:] 
    else:
        mmd_files = glob.glob("*.mmd") 

    if not mmd_files:
        print("No .mmd files found to process.", file=sys.stderr)
        sys.exit(1)

    failed = 0
    for file in mmd_files:
        if not os.path.exists(file):
            print(f"Error: The file '{file}' does not exist.", file=sys.stderr)
            failed += 1
        elif not render_mermaid_to_png(file):
            failed += 1

    if failed:
        print(f"{failed} of {len(mmd_files)} file(s) failed.", file=sys.stderr)
        sys.exit(1)
