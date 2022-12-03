# calories.py
from sys import argv as sysargv
from os.path import abspath

class ElfCaloriesCounter():
    '''
    https://adventofcode.com/2022/day/1
    '''
    def __init__(
        self,
        cal_fp:str=None,
        topn:int=3):
        self.cal_fp, self.topn, =cal_fp, topn
        self.max_load = float('-inf')
        self.topn_l = [0 for i in range(topn)]

    def read_whole_file(self):
        with open(self.cal_fp) as f:
            this_elf_ttl=0
            for line in f.readlines():
                if line=='\n':
                    if this_elf_ttl > self.topn_l[0]:
                        self.topn_l.append(this_elf_ttl)
                        self.topn_l.sort()
                        self.topn_l=self.topn_l[1:]
                    this_elf_ttl=0
                else:
                    this_elf_ttl+=int(line)             
        self.max_load=self.topn_l[-1]
        self.sum_top3=sum(self.topn_l)

if __name__ == '__main__':

    ecc=ElfCaloriesCounter(
        cal_fp=abspath(sysargv[1]),
        topn=3)
    ecc.read_whole_file()

    print(f"greatest load: {ecc.max_load}")     #  69626
    print(f"sum of top3 elves {ecc.sum_top3}")  # 206780
