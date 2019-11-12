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

#CSV to read from CSV file in directory'''
def CSV_Read(SeedFile):
	try:
		with open(SeedFile, 'rb') as f:
			reader = csv.reader(f)
			csv_list = list(reader)
	except:
		print "No SEED.csv file found!"		
	return csv_list

def CSV_Write(WriteList):
	with open("output.csv", "wb") as f:
		writer = csv.writer(f)
		writer.writerows(WriteList)

def Txt_File_Handler_Scaling(HeadersFile, Filename):
	HeadersFile = open(HeadersFile,"r")
	SP_Par_File = open(Filename,"w")
    
MTLseedList = CSV_Read("Seed_Alarming.csv")
MTL_Record_List = [ ]
for i in MTLseedList:
    MTL_Record_List.append(MTL_Record(i))
    


for i in MTL_Record_List:
    print i.Full_Tag_Name