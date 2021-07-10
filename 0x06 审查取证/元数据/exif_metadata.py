import pprint
import optparse
from PIL import Image
from PIL.ExifTags import TAGS

def get_exif_data(fname):
    """Get embedded EXIF data from image file."""
    ret = {}
    try:
        img = Image.open(fname)
        if hasattr( img, '_getexif' ):
            exifinfo = img._getexif()
            if exifinfo != None:
                for tag, value in exifinfo.items():
                    decoded = TAGS.get(tag, tag)
                    ret[decoded] = value
    except IOError:
        print ('IOERROR ' + fname)
    return ret
 
if __name__ == '__main__':
    parser = optparse.OptionParser('usage %prog -F <exif file name>')
    parser.add_option('-F', dest='fileName', type='string',\
    help='specify exif file name')

    (options, args) = parser.parse_args()
    fileName = options.fileName
    if fileName == None:
        print(parser.usage)
        exit(0)
    else:
        exif = get_exif_data(fileName)
        for i in exif.items():
            pprint.pprint(i)
