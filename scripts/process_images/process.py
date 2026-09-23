import os
import subprocess
import imageio
import imageio_ffmpeg
import numpy as np
from PIL import Image
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent


def convert_image(input_path, output_path, width=1400, quality=80):
    img = Image.open(input_path)

    # Keep aspect ratio
    w_percent = width / float(img.size[0])
    height = int((float(img.size[1]) * float(w_percent)))

    img = img.resize((width, height), Image.LANCZOS)

    # Convert to RGB if needed (important for PNG with alpha)
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")

    img.save(output_path, "WEBP", quality=quality)


def gif_to_mp4(input_path, output_path):
    reader = imageio.get_reader(input_path)

    meta = reader.get_meta_data()
    duration = meta.get('duration', 100)
    fps = min(15, 1000 / duration)  # cap FPS for web

    writer = imageio.get_writer(
        output_path,
        fps=fps,
        macro_block_size=None  # we handle resizing ourselves
    )

    for frame in reader:
        frame = np.asarray(frame, dtype=np.uint8)

        # Fix channel mismatch (RGBA → RGB)
        if frame.shape[-1] == 4:
            frame = frame[:, :, :3]

        # Fix EVEN dimensions (critical for H264)
        h, w = frame.shape[:2]

        if w % 2 != 0:
            frame = frame[:, :w-1]

        if h % 2 != 0:
            frame = frame[:h-1, :]

        writer.append_data(frame)

    writer.close()


def video_to_mp4(input_path, output_path):
    """Convert MOV and WebM videos to browser-friendly MP4 files."""
    subprocess.run(
        [
            imageio_ffmpeg.get_ffmpeg_exe(),
            "-y",
            "-i", str(input_path),
            "-map", "0:v:0",
            "-map", "0:a:0?",
            "-map_metadata", "-1",
            "-vf", "fps=30,scale=trunc(iw/2)*2:trunc(ih/2)*2",
            "-c:v", "libx264",
            "-crf", "23",
            "-preset", "medium",
            "-pix_fmt", "yuv420p",
            "-c:a", "aac",
            "-b:a", "128k",
            "-movflags", "+faststart",
            str(output_path),
        ],
        check=True,
    )
    
    
def process_folder(folder):
    for filename in os.listdir(folder):
        path = os.path.join(folder, filename)
        print("\t", path)
        extension = Path(filename).suffix.lower()
        
        if os.path.isdir(path):
            process_folder(path)

        if extension in (".jpg", ".png", ".jpeg"):
            convert_image(path, Path(path).with_suffix(".webp"))

        elif extension == ".gif":
            gif_to_mp4(path, Path(path).with_suffix(".mp4"))

        elif extension in (".mov", ".webm"):
            video_to_mp4(path, Path(path).with_suffix(".mp4"))


if __name__ == "__main__":
    process_folder(SCRIPT_DIR / "older")
