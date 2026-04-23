import os
import imageio
import numpy as np
from PIL import Image


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
    
    
def process_folder(folder):
    for filename in os.listdir(folder):
        path = os.path.join(folder, filename)
        print("\t", path)
        
        if os.path.isdir(path):
            process_folder(path)

        if filename.endswith((".jpg", ".png", ".jpeg")):
            convert_image(path, path.replace(".jpg", ".webp").replace(".png", ".webp"))

        elif filename.endswith(".gif"):
            gif_to_mp4(path, path.replace(".gif", ".mp4"))


process_folder("older/")