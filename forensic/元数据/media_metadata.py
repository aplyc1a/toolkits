from pymediainfo import MediaInfo
import pprint
import optparse

def printMeta(fileName):
    media_info = MediaInfo.parse(fileName)
    data = media_info.to_data()
    pprint.pprint(data)
    #data=data['tracks']
    #pprint.pprint(data[0])
    #pprint.pprint(data[1])

def main():
    parser = optparse.OptionParser('usage %prog -F <MediaInfo file name>')
    parser.add_option('-F', dest='fileName', type='string',\
    help='specify MediaInfo file name')

    (options, args) = parser.parse_args()
    fileName = options.fileName
    if fileName == None:
        print parser.usage
        exit(0)
    else:
        printMeta(fileName)

if __name__ == '__main__':
    main()
