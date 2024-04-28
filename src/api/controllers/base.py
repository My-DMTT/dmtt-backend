from fastapi import APIRouter

from src.api.controllers.auth_router import router as auth_router
from src.api.controllers.company_router import router as company_router
from src.api.controllers.contract_router import router as contract_router
from src.api.controllers.dmtt_router import router as dmmt_router
from src.api.controllers.image_router import router as image_router
from src.api.controllers.limit_router import router as limit_router
from src.api.controllers.product_router import router as product_router
from src.api.controllers.user_router import router as manager_router

router = APIRouter(prefix='')


router.include_router(auth_router)
router.include_router(dmmt_router)
router.include_router(limit_router)
router.include_router(contract_router)

router.include_router(product_router)
router.include_router(image_router)
router.include_router(manager_router)
router.include_router(company_router)
