import gspread
from oauth2client.service_account import ServiceAccountCredentials as sac
from pprint import pprint
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = sac.from_json_keyfile_name("seipsheet.json",scope)









def main():


	# client = gspread.authorize(creds)
	# sheets = client.open("zymejimai").worksheets()
	# sheet = sheets[1]
	# col = sheet.col_values(2)
	
	# sheet.update_cell(1,2,"aa")



	client = gspread.authorize(creds)
	sheets = client.open("zymejimai").worksheets()
	sheet = sheets[1]
	col = sheet.col_values(2)
	print(col)

















main()


























