#!修改下载的Mp3文件名称为正确的Mp3文件
def ModifyMp3FileInfo(filename):

    mp3Id3V1 = {
        "tag":{"valuepos":(0,3),"value":""},
        "SongName":{"valuepos":(3,33),"value":""},
        "SongPeople":{"valuepos":(33,63),"value":""},
        "Zj":{"valuepos":(63,93),"value":""},
        "Year":{"valuepos":(93,97),"value":""},
        "Bak":{"valuepos":(97,125),"value":""}
    }
    try:
        f = open(filename,'rb')
        f.seek(-128,2)
        sdata = f.read(3)
        if sdata == 'TAG':
            f.seek(-128,2)
            sdata = f.read(128)
            for tag,subitem in mp3Id3V1.items():
                subitem["value"] = sdata[subitem["valuepos"][0]:subitem["valuepos"][1]].replace('/00','').strip()
                print('%s='%tag,'%s'%subitem["value"],'/n')
            f.close()
            import os
            if mp3Id3V1["SongName"]["value"]!='':
                test = [os.path.dirname(filename),'//']
                test.append(mp3Id3V1["SongName"]["value"])
                test.append('.mp3')
                newfilename = ''.join(test)
                print(newfilename)
                if os.path.exists(newfilename):
                    test = ['Filename ',newfilename,' Has Existed']
                    print(''.join(test))
                else:
                    try:
                        os.rename(filename,newfilename)
                    except WindowsError as e:
                        if e.winerror:
                            print('Modify filename failed ,maybe the file is inuse')
                        else:
                            print('UnKnown error')
            else:
                print('Is not a MP3 file')
    except IOError as e:
        print('Open file failed')


if __name__ == '__main__':
    ModifyMp3FileInfo(r'E:\CloudMusic\Alyssa Reid - Tomorrow.mp3')


#! /usr/bin/env python

#coding utf-8

# import os
# import re
# import sys
# import eyed3
# from appdirs import unicode
#
# if __name__ == "__main__":
#     if len(sys.argv) != 2:
#         # print('please input MP3 directory')
#         exit()
#
#     patemplate=r'\.mp3'
#     repat=re.compile(patemplate)
#
#     # dir = sys.argv[1]
#     dir = "E:\CloudMusic\\"
#     for filename in os.listdir(dir):
#         filepath = os.path.join(dir, filename)
#         p = re.compile(r'(.*)-(.*)\.mp3', re.I)
#         m = p.match(filename)
#         if m:
#             id3=filename
#             id3 = repat.sub('', filename)
#             audiofile = eyed3.load(filepath)
#             audiofile.initTag()
#             audiofile.tag.title = unicode(id3)
#             audiofile.tag.artist = u"NCE2"
#             audiofile.tag.album = u"NCE2"
#             audiofile.tag.album_artist = u"NCE2"
#             audiofile.tag.track_num = 0
#             audiofile.tag.comment=u"NCE2"
#             audiofile.tag.save()
#         else:
#             pass
