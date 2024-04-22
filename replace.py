"""
ClassUpdate - Update class names of all themes in a folder.
"""

import asyncio
from datetime import datetime

from lib.input import get_params
from lib.pairs import get_pairs
from lib.replacer import replacer

if __name__ == "__main__":
    try:
        print("==== ClassUpdate by Saltssaumure ====\n")
        use_local_diff, diff_location, css_filenames = get_params()

        start = datetime.now()
        class_pairs = get_pairs(use_local_diff, diff_location)

        replace_counts = []
        total_replaced = 0
        files_changed = 0

        print("\nReplacing...")
        for css_filename in css_filenames:
            replace_counts.append(asyncio.run(replacer(css_filename, class_pairs)))

        for replace_count in replace_counts:
            if replace_count > 0:
                files_changed += 1
                total_replaced += replace_count

        end = datetime.now() - start
        duration = int(end.total_seconds() * 1000)
        print(f"\nReplaced {total_replaced} classes in {files_changed} files. ({duration}ms)")

    except KeyboardInterrupt:
        print("\nUser cancelled.")
