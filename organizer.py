import os
import shutil
import logging
from datetime import datetime
from pathlib import Path

# Which extensions go into which folder
FILE_TYPES = {
    "Images":    [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg"],
    "PDFs":      [".pdf"],
    "Documents": [".doc", ".docx", ".txt", ".md", ".odt", ".rtf"],
    "Videos":    [".mp4", ".mov", ".avi", ".mkv"],
    "Audio":     [".mp3", ".wav", ".flac", ".aac"],
    "Archives":  [".zip", ".rar", ".tar", ".gz"],
    "Others":    [],
}

# Build a lookup: ".jpg" -> "Images"
EXT_LOOKUP = {}
for folder_name, exts in FILE_TYPES.items():
    for ext in exts:
        EXT_LOOKUP[ext.lower()] = folder_name


def get_folder_name(file):
    ext = file.suffix.lower()
    return EXT_LOOKUP.get(ext, "Others")


def setup_log(folder):
    log_file = folder / "organizer.log"
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s  |  %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            logging.FileHandler(log_file, encoding="utf-8"),
            logging.StreamHandler(),
        ],
    )
    return logging.getLogger()


def organize(folder_path):
    folder = Path(folder_path).resolve()

    if not folder.exists():
        print(f"ERROR: Folder does not exist: {folder}")
        return

    logger = setup_log(folder)
    logger.info(f"Starting to organize: {folder}")

    moved = 0
    for item in folder.iterdir():
        # Skip folders and the log file itself
        if item.is_dir() or item.name == "organizer.log":
            continue

        dest_folder = folder / get_folder_name(item)
        dest_folder.mkdir(exist_ok=True)

        dest = dest_folder / item.name

        # If a file with same name exists, add a timestamp
        if dest.exists():
            ts = datetime.now().strftime("%H%M%S")
            dest = dest_folder / f"{item.stem}_{ts}{item.suffix}"

        shutil.move(str(item), str(dest))
        logger.info(f"MOVED  {item.name}  -->  {get_folder_name(item)}/")
        moved += 1

    logger.info(f"Done! {moved} file(s) organized.")


# ---- Run the script ----
if __name__ == "__main__":
    import sys
    # If you pass a folder path: python organizer.py C:/Users/You/Downloads
    # If nothing passed: organizes the current folder
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    organize(target)
