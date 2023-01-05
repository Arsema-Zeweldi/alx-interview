#!/usr/bin/python3
""" Checks if n number of boxes can be unlocked """


def canUnlockAll(boxes):
    """ Boxes is a list of lists """
    keychain = [0]
    for onekey in keychain:
        for key in boxes[onekey]:
            if key not in keychain and key < len(boxes):
                keychain.append(key)
    if len(keychain) == len(boxes):
        return True
    return False
