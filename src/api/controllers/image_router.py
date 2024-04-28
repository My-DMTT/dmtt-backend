from fastapi import APIRouter, File, HTTPException, UploadFile

from src.infrastructure.services.file_service import ImageUploader

router = APIRouter(tags=["Image"])
image_uploader = ImageUploader()


@router.post("/image/upload/")
async def upload_image(file: UploadFile = File(...)):

    file_path = image_uploader.save_image(file.filename, file.file, "products")
    return {"file_path": file_path}


@router.post("/image/check_validity/")
async def check_image_validity(file: UploadFile = File(...)):
    is_valid = image_uploader.is_valid_image(file.filename)
    return {"is_valid": is_valid}
