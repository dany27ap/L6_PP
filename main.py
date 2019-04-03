import glob, os
import math
import numpy as np


class GenericFile:
    def __init__(self, PathAbsolut, frecvente, file):
        pass
    def GetPath(self):
        pass
    def GetFirstTag(self):
        pass


class TextASCII(GenericFile):

    def __init__(self, PathAbsolut, freq, file):
        self.PathAbsolut = PathAbsolut
        self.freq = freq
        self.file = file

    def GetPath(self):
        return self.PathAbsolut

    def GetFreq(self):
        self.freqs = [0] * 256
        for line in self.file:
            for char in line:
                self.freqs[char] += 1
        return self.freq


class TextUNICODE(GenericFile):

    def __init__(self, PathAbsolut, frecvente, file):
        self.PathAbsolut = PathAbsolut
        self.frecvente = frecvente
        self.file = file

    def GetPath(self):
        return self.PathAbsolut

    def GetFreq(self):
        freqs = [0] * 256

        for line in self.file:
            for char in line:
                freqs[char] += 1
            temp = 0
            for i in range(0, 255):
                temp += i
        procentZero = (100*freqs[48]) / temp
        return procentZero


class Binary(GenericFile):

    def __init__(self, PathAbsolut, frecvente, file):
        self.PathAbsolut = PathAbsolut
        self.frecvente = frecvente
        self.file = file

    def GetPath(self):
        return self.PathAbsolut

    def GetFreq(self):
        return self.frecvente

class XmlFile(TextASCII):

    def __init__(self, FirtstTag):
        self.FirstTag = FirtstTag

    def GetFirstTag(self):
        return self.FirstTag


class BMP(Binary):

    def __init__(self, Width, Height, BPP):
        self.Width = Width
        self.Height = Height
        self.BPP = BPP

    def ShowInfo(self):
        pass

def whatFileType(file):
    freqs = [0] * 256
    sumHigh = 0
    sumLow = 0
    temp = 0

    for line in file:
        for char in line:
            freqs[char] += 1



    for i in range(32, 127):
        sumHigh += freqs[i]

    sumHigh = freqs[9] + freqs[10] + freqs[13]

    for i in range(128, 255):
        sumLow += freqs[i]
    for i in range(15,31):
        sumLow += freqs[i]

    for i in range(0, 255):
        temp += i

    procentZero = (100*freqs[48]) / temp

    if procentZero >= 30:
        print("UNICODE/UTF16")
    elif sumHigh > sumLow:
        print("ASCII/UTF8")
    elif math.isclose(find_nearest(freqs, freqs[0]), freqs[1], rel_tol=1e-09, abs_tol=0.0) :
        print("BINARY")
    elif os.stat(file).st_size == 0:
        print("Empty")

def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]

def main():

    print('Enter directory: ')
    rootdir = input()

    for root, subdir, files in os.walk(rootdir):
        print(files)
        for file in os.listdir(root):
            filePath = os.path.join(root, file)
            if os.path.isdir(filePath):
                pass
            else:
                f = open(filePath, 'rb')
                whatFileType(f)
                try:
                    content = f.read()
                finally:
                    f.close()


main()

