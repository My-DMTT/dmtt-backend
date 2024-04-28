from typing import List

from fastapi import APIRouter, HTTPException

from src.api.schemas.product import ProductCreate, ProductInfo, ProductUpdate
from src.services.product_service import ProductService

router = APIRouter(tags=["Product"])
product_service = ProductService()


@router.post("/products/", response_model=ProductCreate)
async def create_product(product_data: ProductCreate):
    return await product_service.create_product(product_data)


@router.get("/products/", response_model=List[ProductInfo])
async def create_product():
    return await product_service.get_all_product()


@router.get("/products/{product_id}/", response_model=ProductInfo)
async def get_product_by_id(product_id: int):
    product = await product_service.get_product_by_id(product_id)
    if product:
        return product
    else:
        raise HTTPException(status_code=404, detail="Product not found")


@router.put("/products/{product_id}/", response_model=ProductInfo)
async def update_product(product_id: int, product_data: ProductUpdate):
    product = await product_service.update_product(product_id, product_data)
    if product:
        return product
    else:
        raise HTTPException(status_code=404, detail="Product not found")


@router.delete("/products/{product_id}/")
async def delete_product(product_id: int):
    await product_service.delete_product(product_id)
    return {"detail": "success"}
