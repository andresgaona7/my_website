import os
import shutil
from pathlib import Path

def copy_everything(input_path, output_path):
    for filename in os.listdir(input_path):
        in_path = os.path.join(input_path, filename)
        out_path = os.path.join(output_path, filename)
        
        if os.path.isdir(in_path):
            copy_everything(in_path, out_path)
            
        if filename.endswith((".webp", ".mp4")):
            print('\t', in_path , ' to ', out_path)
            src = Path(in_path)
            dst = Path(out_path)
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(src, dst)
        
copy_everything("older/", "new/")