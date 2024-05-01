from datetime import datetime
from typing import List

import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from pydantic import BaseModel

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

    async def get_data(self, sheet_url, sheet_name):
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

            cell_list = worksheet.range(
                1, new_coumn_index, len(new_data), new_coumn_index)
            for i, cell in enumerate(cell_list):
                if new_data[i] != 0:
                    cell.value = new_data[i]
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


# Example usage:
s = SheetDataFetcher()
# k = s.get_data()
s.add_data(data_list=[
    DataModel(product_name="Manniy yormasi", count=6.0),
    DataModel(product_name="Birinchi navli un", count=10.4)
])
# print(k)
