from typing import List, Optional

from src.api.schemas.company_schema import (CompanyCreate, CompanyInfo,
                                            CompanyUpdate)
from src.domain.exceptions import bad_request_exception, not_found_exception
from src.infrastructure.repositories.company_repo import CompanyRepo


class CompanyService:
    """
    Service class to manage company operations.
    """

    def __init__(self) -> None:
        self._repo = CompanyRepo()

    async def get_all_companies(self, user_id) -> List[CompanyInfo]:
        """
        Retrieve all companies.
        """
        return await self._repo.filter(user_id=user_id)

    async def create_company(self, user_id: int, data: CompanyCreate) -> CompanyInfo:
        """
        Create a new company if it does not exist.

        :param data: CompanyCreate instance containing the company data.
        :raises BadRequestException: If a company with the same STIR exists.
        """

        if await self._repo.is_exists(stir=data.stir):
            raise bad_request_exception("This STIR already exists.")
        return await self._repo.create(user_id, data)

    async def update_company(self, id: int, user_id: int, data: CompanyUpdate) -> CompanyInfo:
        """
        Update an existing company by ID.

        :param id: The ID of the company to update.
        :param data: CompanyUpdate instance with updated values.
        """
        company = await self._repo.get(instance_id=id)
        if company.user_id != user_id:
            raise not_found_exception(name="Company")
        return await self._repo.update(instance_id=id, obj_in=data)

    async def delete_company(self, id: int, user_id: int) -> dict:
        """
        Delete a company by its ID.

        :param id: The ID of the company to delete.
        :returns: A message indicating deletion.
        """
        company = await self._repo.get(instance_id=id)
        if not company:
            raise not_found_exception("Company")
        if company.user_id != user_id:
            raise not_found_exception(name="Company")
        await self._repo.delete(instance_id=id)
        return {"detail": "Company deleted successfully."}

    async def get_company_by_id(self, id: int, user_id: int) -> CompanyInfo:
        """
        Retrieve a company by its ID.

        :param id: The ID of the company to find.
        :raises NotFoundException: If no company is found with the provided ID.
        """
        company = await self._repo.get(instance_id=id)
        if not company or company.user_id != user_id:
            raise not_found_exception(name="Company")
        return company
