#coding=utf-8
import os,os.path
import re
import zipfile
class GenerateZIP:
    filelist = []

    def getFileInList(self, filenames, zipfilename):
        for dirname in filenames:
            if os.path.isfile(dirname):
                self.filelist.append(dirname)
            else:
                for root, dirs, files in os.walk(dirname):
                    for name in files:
                        self.filelist.append(os.path.join(root, name))

        zf = zipfile.ZipFile(zipfilename, "w", zipfile.zlib.DEFLATED)
        for tar in self.filelist:
            # arcname = tar[len(dirname):]
            arcname = re.split('[/ \\\\]',tar)[-1]
            # print arcname
            zf.write(tar, arcname)
        zf.close()

if __name__ == '__main__':
    z = GenerateZIP()
    z.getFileInList(["E:\CloudMusic"],"E:\CloudMusic\\zip.zip")