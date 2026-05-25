from PIL import Image, ImageDraw, ImageFont
import os

# ── Settings ──────────────────────────────────────────────
WIDTH, HEIGHT = 700, 420
BG_DARK      = "#1e1e2e"   # dark background
BG_PANEL     = "#2a2a3e"   # slightly lighter panel
ACCENT_RED   = "#f38ba8"   # for messy files
ACCENT_GREEN = "#a6e3a1"   # for organised folders
ACCENT_BLUE  = "#89b4fa"   # folder icons
TEXT_WHITE   = "#cdd6f4"
TEXT_DIM     = "#6c7086"
TEXT_YELLOW  = "#f9e2af"
TEXT_PURPLE  = "#cba6f7"

def get_font(size, bold=False):
    """Try to load a nice font, fall back to default."""
    font_names = [
        "C:/Windows/Fonts/consola.ttf",        # Windows Consolas
        "C:/Windows/Fonts/cour.ttf",           # Windows Courier
        "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",  # Linux
        "/System/Library/Fonts/Menlo.ttc",     # Mac
    ]
    for path in font_names:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()

def draw_rounded_rect(draw, xy, radius, fill):
    x1, y1, x2, y2 = xy
    draw.rounded_rectangle([x1, y1, x2, y2], radius=radius, fill=fill)

def make_before_image():
    img  = Image.new("RGB", (WIDTH, HEIGHT), BG_DARK)
    draw = ImageDraw.Draw(img)

    title_font  = get_font(18, bold=True)
    header_font = get_font(14)
    file_font   = get_font(13)
    small_font  = get_font(11)

    # ── Title bar ──
    draw_rounded_rect(draw, [0, 0, WIDTH, 44], 0, "#11111b")
    draw.text((20, 13), "📁  Downloads  — Before organizing", font=title_font, fill=TEXT_WHITE)

    # ── Panel ──
    draw_rounded_rect(draw, [20, 60, WIDTH-20, HEIGHT-20], 10, BG_PANEL)

    # ── Column header ──
    draw.text((44, 74), "Name", font=header_font, fill=TEXT_DIM)
    draw.text((380, 74), "Type", font=header_font, fill=TEXT_DIM)
    draw.text((520, 74), "Size", font=header_font, fill=TEXT_DIM)

    # ── Divider ──
    draw.line([(34, 94), (WIDTH-34, 94)], fill="#313244", width=1)

    # Messy files — all dumped in one place
    files = [
        ("📄", "holiday_2023.jpg",         "JPG Image",       "3.2 MB", ACCENT_RED),
        ("📄", "invoice_march.pdf",         "PDF Document",    "1.1 MB", ACCENT_RED),
        ("📄", "meeting_notes.txt",         "Text File",       "12 KB",  ACCENT_RED),
        ("📄", "project_backup.zip",        "ZIP Archive",     "45 MB",  ACCENT_RED),
        ("📄", "vacation_video.mp4",        "MP4 Video",       "220 MB", ACCENT_RED),
        ("📄", "resume_final_v3.docx",      "Word Document",   "890 KB", ACCENT_RED),
        ("📄", "birthday_photo.png",        "PNG Image",       "5.1 MB", ACCENT_RED),
        ("📄", "song_playlist.mp3",         "MP3 Audio",       "8.4 MB", ACCENT_RED),
        ("📄", "random_script.py",          "Python File",     "2 KB",   ACCENT_RED),
        ("📄", "tax_return_2023.pdf",       "PDF Document",    "3.3 MB", ACCENT_RED),
    ]

    for i, (icon, name, ftype, size, color) in enumerate(files):
        y = 106 + i * 27
        # Alternating row bg
        if i % 2 == 0:
            draw_rounded_rect(draw, [30, y-2, WIDTH-30, y+22], 4, "#313244")
        draw.text((40,  y), icon,  font=file_font, fill=color)
        draw.text((62,  y), name,  font=file_font, fill=TEXT_WHITE)
        draw.text((380, y), ftype, font=file_font, fill=TEXT_DIM)
        draw.text((520, y), size,  font=file_font, fill=TEXT_DIM)

    # ── Footer ──
    draw.text((40, HEIGHT-38), "10 files  •  all mixed together  •  hard to find anything",
              font=small_font, fill=TEXT_DIM)

    img.save("images/before.png")
    print("✅ Saved: images/before.png")


def make_after_image():
    img  = Image.new("RGB", (WIDTH, HEIGHT), BG_DARK)
    draw = ImageDraw.Draw(img)

    title_font  = get_font(18, bold=True)
    header_font = get_font(14)
    file_font   = get_font(13)
    small_font  = get_font(11)

    # ── Title bar ──
    draw_rounded_rect(draw, [0, 0, WIDTH, 44], 0, "#11111b")
    draw.text((20, 13), "📁  Downloads  — After organizing", font=title_font, fill=TEXT_WHITE)

    # ── Panel ──
    draw_rounded_rect(draw, [20, 60, WIDTH-20, HEIGHT-20], 10, BG_PANEL)

    # ── Column header ──
    draw.text((44, 74),  "Name",    font=header_font, fill=TEXT_DIM)
    draw.text((300, 74), "Contains",font=header_font, fill=TEXT_DIM)
    draw.text((520, 74), "Files",   font=header_font, fill=TEXT_DIM)

    # ── Divider ──
    draw.line([(34, 94), (WIDTH-34, 94)], fill="#313244", width=1)

    # Neat folders
    folders = [
        ("🖼️",  "Images",     ".jpg  .png  .gif  .webp",  "2 files",  ACCENT_GREEN),
        ("📕",  "PDFs",       ".pdf",                      "2 files",  ACCENT_GREEN),
        ("📝",  "Documents",  ".txt  .docx  .md  .odt",   "2 files",  ACCENT_GREEN),
        ("🎵",  "Audio",      ".mp3  .wav  .flac  .aac",  "1 file",   ACCENT_GREEN),
        ("🎬",  "Videos",     ".mp4  .mov  .avi  .mkv",   "1 file",   ACCENT_GREEN),
        ("📦",  "Archives",   ".zip  .rar  .tar  .gz",    "1 file",   ACCENT_GREEN),
        ("💻",  "Code",       ".py  .js  .html  .css",    "1 file",   ACCENT_GREEN),
        ("📋",  "organizer.log", "log of every move",      "—",        TEXT_YELLOW),
    ]

    for i, (icon, name, contains, count, color) in enumerate(folders):
        y = 106 + i * 32
        if i % 2 == 0:
            draw_rounded_rect(draw, [30, y-2, WIDTH-30, y+24], 4, "#313244")
        draw.text((40,  y+2), icon,     font=file_font, fill=color)
        draw.text((72,  y+2), name,     font=file_font, fill=TEXT_WHITE)
        draw.text((300, y+2), contains, font=small_font, fill=TEXT_DIM)
        draw.text((540, y+2), count,    font=small_font, fill=color)

    # ── Footer ──
    draw.text((40, HEIGHT-38),
              "10 files  •  sorted into 7 folders  •  easy to find everything",
              font=small_font, fill=ACCENT_GREEN)

    img.save("images/after.png")
    print("✅ Saved: images/after.png")


# ── Run both ──────────────────────────────────────────────
os.makedirs("images", exist_ok=True)
make_before_image()
make_after_image()
print("\nDone! Check your images/ folder.")