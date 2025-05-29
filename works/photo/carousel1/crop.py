import os
from PIL import Image

def crop_to_3_2(image):
    width, height = image.size
    target_ratio = 3 / 2

    # 最大可能的裁剪宽度（从左上角开始）
    max_width = min(width, int(height * 2 / 3))
    max_height = int(max_width * 3 / 2)

    crop_box = (0, 0, max_width, max_height)
    return image.crop(crop_box)

def process_and_replace_images(folder):
    supported_extensions = ('.jpg', '.jpeg', '.png')
    for filename in os.listdir(folder):
        if filename.lower().endswith(supported_extensions):
            filepath = os.path.join(folder, filename)
            try:
                with Image.open(filepath) as img:
                    cropped_img = crop_to_3_2(img)
                    cropped_img.save(filepath)
                    print(f"Cropped and replaced: {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    current_folder = os.path.dirname(os.path.abspath(__file__))
    process_and_replace_images(current_folder)
