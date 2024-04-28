import gspread
from oauth2client.service_account import ServiceAccountCredentials

filename = "/src/infrastructure/services/dmtt.json"


credentials = ServiceAccountCredentials.from_json_keyfile_name(filename)

# Authorize the client
client = gspread.authorize(credentials)


# Open a spreadsheet by its title
spreadsheet = client.open_by_url(
    "https://docs.google.com/spreadsheets/d/1rblVzQahN49HfWqUnFub-riA7kfXT3f-IUyomhi7IrA/edit?usp=sharing")


worksheet = spreadsheet.worksheets()[0]

worksheet.insert_cols(list(range(1, 40)), 13)
