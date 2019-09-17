# [START sheets_quickstart]
from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from YostarMediaListDataHandle import YMediaListDataHandle
from YStargazerDataHandle import YStargazerDataHandle
import time

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

def main(formKey, sheetKey):
    # formKey 1.Stargazer Database 2.Yo-Star Media List Database
    # sheetKey 1.YTB Gamer 2.Artist 3.Cosplayer 4.Media List
    formDict = {'1':'111nzxcRVzCxMnelPnMDt4uEIt336eJVEQax4X-pJzWc', '2':'1SMN0vgSqfSHJ6EcYGDPhvo3exXA_QHT_AhPZxduPE-Q'}
    sheetDict = {'1':'YTB Gamer', '2':'Artist', '3':'Cosplayer', '4':'Media List'}
    # The ID and range of a sample spreadsheet.
    SAMPLE_SPREADSHEET_ID = formDict[formKey]
    if int(formKey) == 1:
        SAMPLE_RANGE_NAME = '%s!B2:P' %sheetDict[sheetKey]
    else:
        SAMPLE_RANGE_NAME = '%s!B2:E' %sheetDict[sheetKey]
    
    handleForm(SAMPLE_SPREADSHEET_ID, SAMPLE_RANGE_NAME, int(sheetKey))

def handleForm(SAMPLE_SPREADSHEET_ID, SAMPLE_RANGE_NAME, sheetKeyInt):
    startTime = time.time()
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('YostarPython/token.pickle'):
        with open('YostarPython/token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'YostarPython/credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('YostarPython/token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API, 读取Youtube数据
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])

    # 处理获取的数据
    if sheetKeyInt == 1:
        # YouTube需要订阅数和也不需要观看人数
        handle = YStargazerDataHandle(values, '1')
        values = handle.handleData()
    elif sheetKeyInt == 4:
        handle = YMediaListDataHandle(values)
        values = handle.handleData()
    else:
        # YouTube需要订阅数，不需要观看人数
        handle = YStargazerDataHandle(values, '0')
        values = handle.handleData()

    # 写入数据
    body = {
        'values': values
    }
    result = service.spreadsheets().values().update(
        spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME,
        valueInputOption='USER_ENTERED', body=body).execute()
    print('{0} cells updated.'.format(result.get('updatedCells')))
    
    endTime = time.time()
    print("共耗时 %s 秒" %(endTime - startTime))


if __name__ == '__main__':
    i = 1
    while i:
        formKey = input('请输入工作簿名称序号：1.Stargazer Database 2.Yo-Star Media List Database\n')
        sheetKey = input('请输入电子表格名称序号：1.YTB Gamer 2.Artist 3.Cosplayer 4.Media List\n')
        formKeyInt = int(formKey)
        sheetKeyInt = int(sheetKey)

        if formKeyInt == 1:
            if sheetKeyInt > 0 and sheetKeyInt < 4:
                i = 0
            else:
                print('输入序列号错误，请重新输入')
        elif formKeyInt == 2:
            if sheetKeyInt == 4:
                i = 0
            else:
                print('输入序列号错误，请重新输入')
        else:
            print('输入序列号错误，请重新输入')

    main(formKey, sheetKey)
# [END sheets_quickstart]