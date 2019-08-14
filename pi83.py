import os,sys
class Text_perform:
    File_name = input('Enter a file name.')
    @classmethod
    def File_search(cls):
        if os.path.isfile(cls.File_name):
            print('File is  exist')
            global read_data
            read_data = open(cls.File_name,'r')
            read_data = read_data.readlines()
        else:
            print('File is not found')
            sys.exit()
    @staticmethod
    def File_read():
        #print(read_data)
        count = 0
        global lcount,wcount,ccount
        lcount=wcount=ccount=0
        for p in read_data:
            lcount +=1
            wcount +=len(p.split())
            ccount +=len(p)
            '''if count == 5:
                break
            count +=1'''
    @staticmethod
    def Access():
        print('Line no inside file:',lcount)
        print('No of word inside file:',wcount)
        print('No of ccount inside file:',ccount)

data = Text_perform()
data.File_search()

data.File_read()
data.Access()
print('File content')
print(read_data)
