import zipfile as zf 

#this func to read the file from the zip file 
#and store them into a list 
def Read_ZipFile(path):
    global sensor_list
    sensor_list=[]
    with zf.ZipFile(path) as z:
        # z.namelist() = ['dfile1.dt', 'dfile2.dt', 'dfile3.dt', 'dfile4.dt', 'dfile5.dt', 'dfile6.dt', 'dfile7.dt', 'dfile8.dt']
        for filename in z.namelist():
            with z.open(filename) as f:
                FileData = f.readlines()#he store them in byte's ,, [b'kasflhasjdlk...]
            for i in FileData:
                sensor_list.append(eval(i))#for remove the ([b/n/r]...)
    return sensor_list
    
def ConvertData(DataList):
    list = []
    for line in DataList:
        tempDict=dict()
        keys = ["temp","pressure","humidity","gas","battery"]
        for i in keys:
            tempDict[i] = GetValue(line[i],i)
        list.append(tempDict)
    return list

def GetValue(value,Type):
    res = 1
    if Type=="temp":
        res=(-10+(50/65535)*value)
    elif Type=="pressure":
        res=(9000/16777215)*value
    elif Type=="humidity":
        res = (100 / 255) * value
    elif Type == "gas":
        res = (1000 / 65535) * value
    elif Type == "battery":
        res=(3300+(900/255)*value)
    return res


def WritetoFile(FileName,list):
    with open(FileName, 'a') as the_file:
        the_file.write("temp,pressure,humidity,gas,battery\n")
        for i in list:
            line=''
            for j in ["temp", "pressure", "humidity", "gas", "battery"]:
                line+=str(i[j])
                line+=","
            line=line[:-1]
            line += "\n"
            the_file.write(line)     
    pass

def main(): # the defualt function that start 
    fileName = r'C:\Users\fuads\Desktop\full stack developer\python\python-forsatech\sensors_data\sensors_data.zip'
    list = []
    list =list+Read_ZipFile(fileName)
    list = ConvertData(list)
    FiletoWrite=r"C:\Users\fuads\Desktop\full stack developer\python\python-forsatech\sensors_data\output.csv"
    WritetoFile(FiletoWrite,list)
    pass

if __name__ == "__main__": # start the file, go to main 

    main()

