from datetime import datetime
from typing import List

import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from pydantic import BaseModel

filename = "src/infrastructure/services/dmtt.json"


class DataModel(BaseModel):
    product_name: str
    count: float


class SheetDataFetcher:
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
        sheet_url="https://docs.google.com/spreadsheets/d/1-Uz2puXapAvyNw2bkrdwQLRZ4rRn6gd8Tnh2Ck6vvvA/edit?copiedFromTrash#gid=0",
        sheet_name="December",
        data_list: List[DataModel] = []
    ):
        try:
            spreadsheet = self.client.open_by_url(sheet_url)
            worksheet = spreadsheet.worksheet(sheet_name)
            df = pd.DataFrame(worksheet.get_all_records())
            headers = [item for item in df.head(0)]
            row_count = df.count(axis='rows')["T/r"]

            new_name = self._get_date()
            if new_name not in headers:
                total_columns = len(headers) if headers else 0
                new_coumn_index = total_columns-1
                worksheet.insert_cols(
                    [None], col=new_coumn_index, value_input_option='RAW', inherit_from_before=False)
                new_data = [0]*row_count
                new_data[0] = new_name

                for item in data_list:

                    row_data = df[df['Mahsulot nomi'] == item.product_name]
                    result_list = [row['T/r']
                                   for index, row in row_data.iterrows()]
                    for result in result_list:
                        new_data[result] = item.count

                cell_list = worksheet.range(
                    1, new_coumn_index, len(new_data), new_coumn_index)
                for i, cell in enumerate(cell_list):
                    cell.value = new_data[i]
                worksheet.update_cells(cell_list)
            return True
        except Exception as e:
            print(e.args)
            return None

    def _get_date(self):
        current_date = datetime.now()
        formatted_date = current_date.strftime('%d/%m/%Y')
        return formatted_date


# Example usage:
s = SheetDataFetcher()

s.add_data(data_list=[
    DataModel(product_name="Manniy yormasi", count=5),
    DataModel(product_name="Bug'doy uni", count=10)
])
