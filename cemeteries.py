error_file = open("cemeteries_error.txt", "w")
# print("error file created")

try:
        import requests
        import lxml.html
        import csv
        import datetime
        import traceback
except:
        error_file.write("Could not import required files")
        error_file.write(traceback.format_exc())
        print(traceback.format_exc())

try:
        now = datetime.datetime.now()
        # print program start time
        # print(str(now))

        # open new csv file
        #cemetery_data = open('//CHFS/Shared Documents/OpenData/datasets/staging/cemetery_data.csv', 'w')
        cemetery_data = open('./data/cemetery_data.csv', 'w')
        writer = csv.writer(cemetery_data)

        alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        h_written = False
        # print("created csv writer")

        # loop through each link based on alphabet
        for letter in alphabet:
                request = requests.get("http://townhall.townofchapelhill.org/facilities/cemeteries/old_cemetery/search3.asp?name=" + letter)
#                print(request.text)
                root = lxml.html.fromstring(request.text)

                # find header elements (th) and table data elements (td) in html page
                headers = root.xpath('//tr/th//text()')
                info = [td_elm.text_content() for td_elm in root.xpath('//tr/td')]
                # write header in csv file
                if(not h_written):
                        writer.writerow(headers)
                        h_written = True
                        count = 0
                        row= []
                # write rows in csv file
                for i in info:
                        row.append(i)
                        # print(i)
                        if(count == 4):
                                writer.writerow(row)
                                row = []
                                count = 0
                        else:
                                count += 1
#                now = datetime.datetime.now()
                # print program end time
#                print(str(now))
except:
        error_file.write(traceback.format_exc() + "\n")
        print(traceback.format_exc())
