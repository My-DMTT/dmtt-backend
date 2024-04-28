import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

from src.domain.exceptions import raise_exception

filename = "src/infrastructure/services/dmtt.json"


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

            # df = pd.DataFrame(data)
            return data
        except Exception as e:
            raise_exception(e.args)
            return None


# Example usage:
