# Automated File Organizer

A simple Python script that automatically sorts files in any folder into subfolders by type — and logs every move with a timestamp.

## What it does

Drops your messy folder files into neat subfolders:

```
Downloads/
  Images/      ← .jpg .png .gif
  PDFs/        ← .pdf
  Documents/   ← .doc .docx .txt
  Videos/      ← .mp4 .mov
  Audio/       ← .mp3 .wav
  Archives/    ← .zip .rar
  Others/      ← everything else
  organizer.log  ← record of every move
```

## How to use

```bash
# Organize a specific folder
python organizer.py C:/Users/YourName/Downloads

# Organize the current folder
python organizer.py
```

## Requirements

- Python 3.8 or newer
- No extra packages needed — uses only built-in Python libraries

## Sample log output

```
2024-06-01 14:22:01  |  Starting to organize: C:/Users/You/Downloads
2024-06-01 14:22:01  |  MOVED  holiday.jpg  -->  Images/
2024-06-01 14:22:01  |  MOVED  invoice.pdf  -->  PDFs/
2024-06-01 14:22:01  |  MOVED  notes.txt    -->  Documents/
2024-06-01 14:22:01  |  Done! 3 file(s) organized.
```
