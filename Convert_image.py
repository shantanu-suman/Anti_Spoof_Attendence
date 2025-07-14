from PIL import Image
import os

input_folder = "images/known_faces"
output_folder = "images/known_faces_rgb"
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        input_path = os.path.join(input_folder, filename)
        name_only = os.path.splitext(filename)[0]
        output_path = os.path.join(output_folder, f"{name_only}.jpg")
        try:
            with Image.open(input_path) as img:
                rgb_image = img.convert("RGB")
                rgb_image.save(output_path, format='JPEG')
                print(f"✅ Converted and saved: {output_path}")
        except Exception as e:
            print(f"❌ Failed to convert {filename}: {e}")
