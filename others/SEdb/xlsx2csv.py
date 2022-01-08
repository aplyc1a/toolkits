import os
import xlrd
import csv
import codecs 
import optparse

def clean_csv(file):
    try:
        workbook = xlrd.open_workbook(file)
    except:
        print("[error] %s" %(file))
        return
    sheetsList = workbook.sheet_names() 
    sheetNum = len(sheetsList)
    for i in range(sheetNum):
        table = workbook.sheet_by_index(i)
        csv_file=os.path.splitext(file)[0]+'-utf8-sheet'+str(i)+'.csv'
        if os.path.isfile(csv_file):
            os.remove(csv_file)

def xls_to_csv(file):
    try:
        workbook = xlrd.open_workbook(file)
    except:
        print("[error] %s" %(file))
        return
    sheetsList = workbook.sheet_names() 
    sheetNum = len(sheetsList)
    for i in range(sheetNum):
        table = workbook.sheet_by_index(i)
        csv_file=os.path.splitext(file)[0]+'-utf8-sheet'+str(i)+'.csv'
        if os.path.isfile(csv_file) and os.path.getsize(csv_file):
            print("[skip] "+file)
            continue
        print("[create] "+csv_file)
        with codecs.open(csv_file, 'w', encoding='utf-8') as f:
            write = csv.writer(f)
            for row_num in range(table.nrows):
                row_value = table.row_values(row_num)
                write.writerow(row_value)

def get_XLSfiles(file_path):
    os.chdir(file_path)
    all_file = os.listdir()
    files = []
    for f in all_file:
        if os.path.isdir(f):
            files.extend(get_XLSfiles(file_path+'/'+f))
            os.chdir(file_path)
        else:
            if "xls" in f.split('.')[-1]:
                files.append(os.path.abspath(os.curdir)+'/'+f)
            if "XLS" in f.split('.')[-1]:
                files.append(os.path.abspath(os.curdir)+'/'+f)
    return files

if __name__ == '__main__':
    parser = optparse.OptionParser('usage : python3 % prog [-f <xlsx_file>]/[[-d <xlsx_folder>][-c][-r]]' )
    parser.add_option('-f', '--file', dest = 'xls_file', type = 'string', help = 'xls(x) filename')
    parser.add_option('-d', '--files_path', dest = 'path',  type = 'string', help = 'the folder which contain xls(x)')
    parser.add_option('-c', '--clean_csv', dest = 'clean_flag', action="store_true", default=False, help = 'clean csv only')
    parser.add_option('-r', '--rebuild_csv', dest = 'rebuild_flag', action="store_true", default=False, help = 'rebuild csv from xls(x)')

    (options,args) = parser.parse_args()
    file = options.xls_file
    path = options.path

    if path :
        path = options.path
        files = get_XLSfiles(path)
        for file in files:
            if options.clean_flag:
                clean_csv(file)
                continue
            if options.rebuild_flag:
                clean_csv(file)
                xls_to_csv(file)
    elif file :
        xls_to_csv(file)
