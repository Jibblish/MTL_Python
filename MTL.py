import csv
import datetime
import openpyxl

class MTL_Record:
  def __init__(self,DETAIL_LIST):
    self.Full_Tag_Name = DETAIL_LIST[0]
    self.Equip_Number = DETAIL_LIST[1]
    self.Main_Equipment = DETAIL_LIST[2]
    self.Unique_Number = DETAIL_LIST[3]
    self.Colloquial_Name = DETAIL_LIST[4]
    self.Element_Type = DETAIL_LIST[5]
    self.PLC_Tag = DETAIL_LIST[6]
    self.UDT_Type = DETAIL_LIST[7]
    self.Data_Type = DETAIL_LIST[8]
    self.Units = DETAIL_LIST[9]

def XLSX_Read(xlsxFile,wbSheet):
    try:
        with openpyxl.load_workbook(xlsxFile) as wb:
            ws = wb[wbSheet]
    except:
        print "No xlsx file found!"
    
wb = openpyxl.load_workbook("HMI Tag and Scaling Summary 11-8-19.xlsx")
ws = wb['Sheet1']
for row in ws.rows:
    for cell in row:
        if cell.value:
            print cell.value
    #print row
'''
for row in wb.rows:
    for cell in row:
        print cell.value
'''
