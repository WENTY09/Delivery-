from PIL import Image, ImageDraw, ImageFont
import os

def create_delivery_image():
    image = Image.new('RGB', (800, 600), color='white')
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    draw.text((100, 100), "Доставка завершена!", font=font, fill='black')
    output_path = "static/images/deliveries/delivery_complete.jpg"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    image.save(output_path)
    return output_path
