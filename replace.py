"""
Update Discord classes in CSS/SCSS files.
"""


from lib.file import read_from_file, write_to_file
from lib.input import get_params
from lib.pairs import get_pairs, replace_pairs

if __name__ == "__main__":
    use_local_diff, diff_location, css_filenames = get_params()
    class_pairs = get_pairs(use_local_diff, diff_location)

    TOTAL_REPLACE_COUNT = 0
    FILES_CHANGED_COUNT = 0

    for css_filename in css_filenames:
        # Get CSS file content
        css_string = read_from_file(css_filename)

        # Convert old classes and old class pairs to new classes.
        css_string, replace_count = replace_pairs(css_string, class_pairs)
        if replace_count > 0:
            FILES_CHANGED_COUNT += 1
            TOTAL_REPLACE_COUNT += replace_count

        # Write CSS to file
        write_to_file(css_filename, css_string)

    print(f"\nReplaced {TOTAL_REPLACE_COUNT} classes in {FILES_CHANGED_COUNT} files.")
