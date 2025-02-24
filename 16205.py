import sys
import random

input = sys.stdin.readline

tnw = list(map(str, input().split()))

def cam2pas(var):
    word = list(var)
    word[0] = word[0].upper()
    return ''.join(word)

def cam2sna(var):
    word = list(var)
    result = []
    for cha in word:
        if cha.isupper():
            result.append('_')
            result.append(cha.lower())
        else:
            result.append(cha)
    return ''.join(result)

def sna2cam(var):
    word = list(var)
    result = []
    i = 0
    while i < len(word):
        if word[i] == '_':
            i += 1
            if i < len(word):
                result.append(word[i].upper())
        else:
            result.append(word[i])
        i += 1
    return ''.join(result)

def sna2pas(var):
    word = sna2cam(var)
    return cam2pas(word)

def pas2cam(var):
    word = list(var)
    word[0] = word[0].lower()
    return ''.join(word)

def pas2sna(var):
    word = pas2cam(var)
    return cam2sna(word)

match tnw[0]:
    case '1':  # cam
        print(tnw[1])
        print(cam2sna(tnw[1]))
        print(cam2pas(tnw[1]))
    case '2':  # sna
        print(sna2cam(tnw[1]))
        print(tnw[1])
        print(sna2pas(tnw[1]))
    case '3':  # pas
        print(pas2cam(tnw[1]))
        print(pas2sna(tnw[1]))
        print(tnw[1])