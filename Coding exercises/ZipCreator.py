import zipfile
import pathlib
def compact_file(files, file_location):
    dest_path = pathlib.Path(file_location, "compressed.zip")
    with zipfile.ZipFile(dest_path, 'w') as compressed:
        for filepath in files:
            filepath = pathlib.Path(filepath)
            compressed.write(filepath)