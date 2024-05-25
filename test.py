import asyncio
from datetime import datetime
from typing import List, Optional

import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from pydantic import BaseModel

from src.infrastructure.repositories.product_repo import ProductRepo


class LimitInfo(BaseModel):
    name: str
    measure: str
    limit: str
    image_url: Optional[str]
    count: str

    class Config:
        from_attributes = True


# from src.domain.exceptions import raise_exception
filename = "src/infrastructure/services/dmtt.json"


class DataModel(BaseModel):
    product_name: str
    count: float


class SheetDataFetcher():
    def __init__(self):
        self.filename = filename
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name(
            filename)
        self.client = gspread.authorize(self.credentials)

    def get_data(self,
                 sheet_url="https://docs.google.com/spreadsheets/d/1-Uz2puXapAvyNw2bkrdwQLRZ4rRn6gd8Tnh2Ck6vvvA/edit?copiedFromTrash#gid=0",
                 sheet_name="December"
                 ):
        try:
            spreadsheet = self.client.open_by_url(sheet_url)
            worksheet = spreadsheet.worksheet(sheet_name)
            data = worksheet.get_all_values()
            return data
        except Exception as e:
            print(e.args)
            return None

    def add_data(
        self,
        sheet_url="https://docs.google.com/spreadsheets/d/1qZOyAbCyfUv7lxpld_ToDqGKuw9kCLvxmPJC9aN6sdk/edit#gid=0",
        sheet_name="May",
        data_list: List[DataModel] = []
    ):
        try:
            spreadsheet = self.client.open_by_url(sheet_url)
            worksheet = spreadsheet.worksheet(sheet_name)
            values = worksheet.get_all_values()

            headers = values[0]
            row_count = len(values)

            new_coumn_index = -1
            new_name = self._get_date()
            new_data = []
            if new_name not in headers:
                total_columns = len(headers) if headers else 0
                new_coumn_index = total_columns-1
                worksheet.insert_cols(
                    [None], col=new_coumn_index, value_input_option='RAW', inherit_from_before=False)
                new_data = [0]*row_count
                new_data[0] = new_name
            else:
                new_coumn_index = headers.index(new_name)
                new_data = [0 if item[new_coumn_index] ==
                            '' else item[new_coumn_index] for item in values]
                new_coumn_index += 1

            for item in data_list:
                new_index = -1
                for value in values[1:]:
                    if value[1] == item.product_name:
                        new_index = int(value[0])
                        break
                if new_index > -1:

                    new_data[new_index] = float(new_data[new_index])+item.count
            print(new_data)
            cell_list = worksheet.range(
                1, new_coumn_index, len(new_data), new_coumn_index)
            for i, cell in enumerate(cell_list):
                if new_data[i] != 0:
                    cell.value = float(new_data[i])
                # print(cell
            worksheet.update_cells(cell_list)
            return True
        except Exception as e:
            print(e.args)
            return None

    def _get_date(self):
        current_date = datetime.now()
        formatted_date = current_date.strftime('%d/%m/%y')
        return formatted_date

# Example usage:


_product_repo = ProductRepo()
# Example usage:


async def test():
    s = SheetDataFetcher()
    # k = s.get_data()
    data = s.get_data()
    limit_info_list = []

    for index, row in enumerate(data):
        name = row[1]
        measure = row[2]
        limit = row[3]
        count = row[-1]
        if index == 0:
            continue
        product = await _product_repo.get_or_create(name, measure)

        limit_info = LimitInfo(
            name=name,
            measure=measure,
            limit=limit,
            count=count,
            image_url=product.image_url
        )
        limit_info_list.append(limit_info)
    return limit_info_list
p = asyncio.run(test())
print(p)
