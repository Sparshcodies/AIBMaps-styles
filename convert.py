import os
import subprocess

def convert_svgs_to_png_inkscape(input_folder, output_folder, width=None, height=None):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.svg'):
            input_path = os.path.join(input_folder, filename)
            output_filename = os.path.splitext(filename)[0] + '.png'
            output_path = os.path.join(output_folder, output_filename)

            cmd = [
                'inkscape', input_path,
                '--export-type=png',
                f'--export-filename={output_path}'
            ]

            if width:
                cmd.append(f'--export-width={width}')
            if height:
                cmd.append(f'--export-height={height}')

            try:
                subprocess.run(cmd, check=True)
                print(f"Converted: {filename} → {output_filename}")
            except subprocess.CalledProcessError as e:
                print(f"Error converting {filename}: {e}")

# Example usage
input_folder = '/home/ssahu/tileserver/tiles/styles/light-mode/sprite_images'
output_folder = '/home/ssahu/tileserver/tiles/styles/light-mode/sprite_images_png'
convert_svgs_to_png_inkscape(input_folder, output_folder, width=64, height=64)
