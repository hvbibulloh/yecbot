from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from PIL import Image


def validate_image_size(value):
    try:
        img = Image.open(value)
        img.verify()
    except Exception as e:
        raise ValidationError("Kechirasiz bu Fayl rasm emas, Iltimos Rasm kiriting!")

    max_size = 20 * 1024 * 1024
    if value.size > max_size:
        raise ValidationError("Fayl hajmi ko'pi bilan 10 MB bo'lishi mumkin!")


def validate_image(value):
    FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])(value)
    validate_image_size(value)
