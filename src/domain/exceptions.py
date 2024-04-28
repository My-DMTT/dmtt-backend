from fastapi import HTTPException

image_not_found = HTTPException(
    status_code=404, detail="image url is not"
)
not_permission_error_login = HTTPException(
    status_code=405, detail="Sizga ruxasta yo'q")

invalid_image = HTTPException(status_code=400, detail="Invalid image file")

user_not_found = HTTPException(
    status_code=401, detail="Username or password incorect")


def raise_exception(data):
    raise HTTPException(status_code=401, detail=str(data))


def not_found_exception(name):
    raise HTTPException(status_code=404, detail=f"{name} not found")


def bad_request_exception(error):
    raise HTTPException(status_code=400, detail=error)
