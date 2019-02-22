from pydub import AudioSegment





class Trans:
    def trans_mp3_to_wav(self, filePath, exportPath):
        song = AudioSegment.from_mp3(filePath)
        song.export(exportPath, format="wav")


if __name__ == '__main__':
    tr = Trans()
    tr.trans_mp3_to_wav("Alyssa_Reid_Tomorrow.mp3","result.wav")