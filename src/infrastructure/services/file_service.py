import os
import uuid
from typing import BinaryIO

from PIL import Image as PILImage

from src.domain.exceptions import invalid_image


class ImageUploader():

    def _get_file_extension(self, filename):
        extension = filename.split('.')[-1].lower()
        return extension

    def _generate_uuid(self):
        return str(uuid.uuid4())

    def save_image(self, filename: str, file_data: BinaryIO, folder="") -> str:
        try:
            if not self._is_image(filename):
                raise invalid_image
            file_name = f"{self._generate_uuid()}.{self._get_file_extension(filename)}"
            directory = os.path.join("uploads", folder)
            file_path = os.path.join(directory, file_name)
            os.makedirs(directory, exist_ok=True)
            with open(file_path, "wb") as buffer:
                buffer.write(file_data.read())
            file_path = file_path.replace("\\", "/")
            return file_path
        except Exception as e:
            raise ValueError(str(e))

    def _is_image(self, filename: str) -> bool:
        """
        Verify if the file with the given filename is an image.
        """
        allowed_extensions = {".jpg", ".jpeg", ".png", ".gif"}
        _, file_extension = os.path.splitext(filename)
        return file_extension.lower() in allowed_extensions

    # def _is_valid_image(self, filename: str) -> bool:
    #     """
    #     Verify if the file with the given filename is a valid image.
    #     """
    #     try:
    #         image = PILImage.open(filename)
    #         image.verify()  # Verify if it's actually an image
    #         return True
    #     except Exception as e:
    #         return False
