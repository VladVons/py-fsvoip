# VladVons@gmail.com
# 2019.12.30

import os
import xlrd
from pyexcel_ods import get_data
from openpyxl import load_workbook, Workbook
from openpyxl.utils import column_index_from_string


class TFields():
  pass


class TXls():
  def __init__(self, aSheet, aCode, aName, aPrice):
    self.Fields = TFields()
    self.Fields.Sheet = aSheet
    self.Fields.Code  = column_index_from_string(aCode)  - 1
    self.Fields.Name  = column_index_from_string(aName)  - 1
    self.Fields.Price = column_index_from_string(aPrice) - 1
    pass


  def LoadFile_xlsx(self, aFile):
    wb = load_workbook(filename = aFile, read_only = True, data_only = True)

    if (self.Fields.Sheet):
      ws = wb[self.Fields.Sheet]
    else:
      ws = wb.active

    Result = {}
    for row in ws.rows:
      Code = row[self.Fields.Code].value
      if (Code is not None):
        Result[Code] = {"Name": row[self.Fields.Name].value, "Price" : row[self.Fields.Price].value}

    print('File:', aFile,  ', Sheet:', ws.title, ', Records:', ws.max_row)
    return Result


  def LoadFile_xls(self, aFile):
    wb = xlrd.open_workbook(aFile)

    if (self.Fields.Sheet):
      ws = wb.sheet_by_name(self.Fields.Sheet)
    else:
      ws = wb.sheet_by_index(0)

    Result = {}
    for i in range(0, ws.nrows):
      Code = ws.cell(i, self.Fields.Code).value
      if (Code):
        Result[Code] = {"Name": ws.cell(i, self.Fields.Name).value, "Price" : ws.cell(i, self.Fields.Price).value}

    print('File:', aFile,  ', Sheet:', ws.name, ', Records:', ws.nrows)
    return Result


  def LoadFile_ods(self, aFile):
    Result = {}

    Data = get_data(aFile)
    if (self.Fields.Sheet):
      Sheet = self.Fields.Sheet
    else:
      Sheets = list(Data.keys())
      Sheet = Sheets[0]

    Items = Data.get(Sheet)
    for Item in Items:
      MaxIdx = max(self.Fields.Code, self.Fields.Name, self.Fields.Price)
      if (MaxIdx <= len(Item)):
        Code = Item[self.Fields.Code]
        if (Code):
          Result[Code] = {"Name": Item[self.Fields.Name], "Price" : Item[self.Fields.Price]}

    print('File:', aFile,  ', Sheet:', Sheet, ', Records:', len(Items))
    return Result

  def Compare(self, aFile1, aFile2):
    Result = []

    Ext = os.path.splitext(aFile1)[1].lower()
    if (Ext == '.xls'):
      Items1 = self.LoadFile_xls(aFile1)
      Items2 = self.LoadFile_xls(aFile2)
    elif (Ext == '.xlsx'):
      Items1 = self.LoadFile_xlsx(aFile1)
      Items2 = self.LoadFile_xlsx(aFile2)
    elif (Ext == '.ods'):
      Items1 = self.LoadFile_ods(aFile1)
      Items2 = self.LoadFile_ods(aFile2)
    else:
      print('unknown format %s' % Ext)
      return Result

    # find missed items and items with different prices
    for Code in Items1:
      Name = Items1[Code].get('Name')
      Price1 = Items1[Code].get('Price', 0)
      if (Items2.get(Code)):
        Price2 = Items2[Code].get('Price', 0)
        if (Price1 != Price2):
          Result.append([Code, Name, Price1, Price2, round(Price2 - Price1, 3), round(100 - Price1 / Price2 * 100, 2)])
      else:
          Result.append([Code, Name, Price1, 0, 0, 0])

    # find new items
    for Code in Items2:
      Name = Items2[Code].get('Name')
      if (not Items1.get(Code)):
          Price2 = Items2[Code].get('Price', 0)
          Result.append([Code, Name, 0, Price2, 0, 0])

    return Result


  @staticmethod
  def Export(aData, aFile):
    wb = Workbook()
    ws = wb.active
    ws.append(['Code', 'Name', 'Price1', 'Price2', 'Diff', 'PCent'])
    for Item in aData:
      ws.append(Item)
    wb.save(aFile)


class TBrend():
  def __init__(self):
    self.Arr = {}
    self.Arr['laktalis'] = {'Sheet': 'по брендам', 'Code': 'B', 'Name': 'J', 'Price': 'AH'}
    self.Arr['lusdorf'] =  {'Sheet': '',           'Code': 'C', 'Name': 'D', 'Price': 'J'}

  def Compare(self, aBrend, aFile1, aFile2, aFileOut):
    Brend = self.Arr.get(aBrend)
    Xls = TXls(aSheet = Brend['Sheet'], aCode = Brend['Code'], aName = Brend['Name'], aPrice = Brend['Price'])
    Data = Xls.Compare(aFile1, aFile2)
    Xls.Export(Data, aFileOut)


#Brend = TBrend()
#Brend.Compare('laktalis', 'lactalis-p1.xlsx', 'lactalis-p2b.xlsx', 'p3.xlsx')
#Brend.Compare('lusdorf',  'ld-1.xlsx',         'ld-2.xlsx', 'p3.xlsx')
#Brend.Compare('lusdorf',  'ld-1.xls',         'ld-2.xls', 'p3.xlsx')
#Brend.Compare('lusdorf',  'ld-1.ods',         'ld-2.ods', 'p3.xlsx')
