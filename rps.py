# https://adventofcode.com/2022/day/2
from sys import argv as sysargv
from os.path import abspath

m0 = {
    'A' :'r', # 🗻
    'B' :'p', # 📃
    'C' :'s', # ✂️
    'X' :'r', # 🗻
    'Y' :'p', # 📃
    'Z' :'s', # ✂️
}


m2 = {
    ('r', 'r'): 4,
    ('r', 'p'): 8,
    ('r', 's'): 3,
    ('p', 'p'): 5,
    ('p', 'r'): 1,
    ('p', 's'): 9,
    ('s', 's'): 6,
    ('s', 'r'): 7,
    ('s', 'p'): 2,
}

def score_round(theirs:str=None, ours:str=None, v:bool=False):
    theirs, ours= m0.get(theirs), m0.get(ours)
    score=m2.get((theirs,ours))
    if v:
        print(f"theirs:{theirs}   ours:{ours}   score:{score}")
    return(score)

if __name__ == '__main__':
    fp=abspath(sysargv[1])
    with open(fp, 'rt') as tf:
        ts=0 #`tourney score`
        for line in tf.readlines():
            ts+=score_round(*line.split())
        print(f"final score pt1: {ts}") # 13565


############################

m_win = { 'r':'p',
        'p':'s',
        's':'r'}

m_lose = {'r':'s',
        'p':'r',
        's':'p'}

m_draw = {'r':'r',
        'p':'p',
        's':'s'}

m_pick={"X" : m_lose,
       "Y" : m_draw,
       "Z" : m_win,
}

def score_round2(theirs:str=None, ours:str=None):
    score=m2.get((theirs,ours))
    return(score)

if __name__ == '__main__':
    fp=abspath(sysargv[1])
    with open(fp, 'rt') as tf:
        ts=0 #tourney score
        for line in tf.readlines():
            r=line.split()
            theirs_= m0.get(r[0])
            ours_= m_pick.get(r[1]).get(theirs_)
            ts+= score_round2(theirs_,ours_)
        print(f"final score pt2: {ts}") # 12424
