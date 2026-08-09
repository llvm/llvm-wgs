import argparse
import base64
import os
import requests
import glob
import sys

def render_mermaid_to_png(mmd_file_path, output_dir):
    # Extract just the filename without any folder paths or extensions
    base_name = os.path.splitext(os.path.basename(mmd_file_path))[0]

    # Route the output file into the new directory
    output_png_path = os.path.join(output_dir, f"{base_name}.png")
    print(f"Processing: {mmd_file_path} -> {output_png_path}")

    try:
        with open(mmd_file_path, "r", encoding="utf-8") as f:
            graph_code = f.read()

        graphbytes = graph_code.encode("utf8")
        base64_bytes = base64.urlsafe_b64encode(graphbytes)
        base64_string = base64_bytes.decode("ascii")

        # mermaid.ink serves JPEG unless a type is requested explicitly
        api_url = f"https://mermaid.ink/img/{base64_string}?type=png"
        response = requests.get(api_url)
        response.raise_for_status()

        content_type = response.headers.get("Content-Type", "")
        if not content_type.startswith("image/png"):
            raise ValueError(f"expected a PNG response, got '{content_type}'")

        with open(output_png_path, "wb") as f_out:
            f_out.write(response.content)

        print(f"Successfully saved: {output_png_path}")
        return True

    except Exception as e:
        print(f"Error processing {mmd_file_path}: {e}", file=sys.stderr)
        return False

def parse_args():
    parser = argparse.ArgumentParser(
        description="Render Mermaid (.mmd) diagrams to PNG using mermaid.ink."
    )
    parser.add_argument(
        "files",
        nargs="*",
        metavar="FILE",
        help="Specific .mmd files to render (default: every .mmd file in --source-dir)",
    )
    parser.add_argument(
        "-s", "--source-dir",
        default=os.getcwd(),
        help="Directory to scan for .mmd files when no FILE is given (default: %(default)s)",
    )
    parser.add_argument(
        "-o", "--output-dir",
        default=os.path.join(os.getcwd(), "generated_graph"),
        help="Directory to write the generated PNGs into (default: %(default)s)",
    )
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()

    # Resolve up front so every message reports a full path, even when the
    # user passed a relative directory on the command line.
    source_dir = os.path.abspath(args.source_dir)
    output_dir = os.path.abspath(args.output_dir)

    mmd_files = args.files or sorted(glob.glob(os.path.join(source_dir, "*.mmd")))

    if not mmd_files:
        print(f"No .mmd files found to process in '{source_dir}'.", file=sys.stderr)
        sys.exit(1)

    # Create the target folder if it doesn't exist yet
    os.makedirs(output_dir, exist_ok=True)

    failed = 0
    for file in mmd_files:
        if not os.path.exists(file):
            print(f"Error: The file '{file}' does not exist.", file=sys.stderr)
            failed += 1
        elif not render_mermaid_to_png(file, output_dir):
            failed += 1

    if failed:
        print(f"{failed} of {len(mmd_files)} file(s) failed.", file=sys.stderr)
        sys.exit(1)
