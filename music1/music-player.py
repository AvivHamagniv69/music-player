#!/usr/bin/python3
import random
import vlc
import time
import os


list_of_files = []
g = 0
for file in os.listdir("."):
    if file.endswith(".m4a"):
        print(g, os.path.join(".", file))
        list_of_files.append(file)
        g = g+1
    if file.endswith(".mp3"):
        print(g, os.path.join(".", file))
        list_of_files.append(file)
        g = g+1
g = g-1
list_of_files_len = len(list_of_files)
print(g)


def play_music(var):
    media_player = vlc.MediaPlayer(var)
    media_player.play()
    time.sleep(1)
    value = media_player.get_media()
    print(value)

    command = input("do what you want: ")

    if command == "stop":
        quit()

    if command == "exit":
        media_player.stop()

    if command == "pause":
        media_player.pause()
        continu = input("would you like to resume? y/n ")
        if continu == "y":
            media_player.play()
        if continu == "n":
            time.sleep(0)

    if command == "skip":
        media_player.stop()

def pd():
    drlist = []
    for file1 in os.listdir("."):
        if file1.endswith(".m4a"):
            drlist.append(file1)
        if file1.endswith(".mp3"):
            drlist.append(file1)
    drlist_len = len(drlist)
    g = 0
    for f in range(drlist_len):
        media_player = vlc.MediaPlayer(drlist[g])
        media_player.play()
        time.sleep(1)
        value = media_player.get_media()
        print(value)

        g = g+1
        command = input("do what you want: ")

        if command == "exit":
            quit()

        if command == "stop":
            media_player.stop()
            break

        if command == "skip":
            media_player.stop()

        if command == "pause":
            media_player.pause()
            continu = input("would you like to resume? y/n ")
            if continu == "y":
                media_player.play()
            if continu == "n":
                time.sleep(0)


def play_music_2(var, var1):
    media_player = vlc.MediaPlayer(var[var1])
    media_player.play()
    time.sleep(1)
    value = media_player.get_media()
    print(value)

    while True:
        command = input("do what you want: ")

        if command == "stop":
            quit()

        if command == "exit":
            media_player.stop()

        if command == "pause":
            media_player.pause()
            continu = input("would you like to resume? y/n ")
            if continu == "y":
                media_player.play()
            if continu == "n":
                time.sleep(0)

        if command == "skip":
            media_player.stop()

        else:
            continue


while True:
    chse = input("choose the number related to the song you want to play (type -help to see all commands) ")

    if chse == "exit":
        quit()

    if ".m4a" in chse:
        play_music(chse)
    if ".mp3" in chse:
        play_music(chse)

    try:
        chse_int = int(chse)
        print(list_of_files)
        play_music_2(list_of_files, chse_int)
    except:
        pass

    if chse == "pd":
        pd()

    if chse == "-help":
        print('''list of all commands:
-help = lists all commands
exit = exits the app
stop = stops the music
pd = plays your entire directory:
    stop = exits the program and stops the music
    skip = skips the song and moves to the next song in line
    pause = pauses the song and allows you to resume it later
    resume = resumes the paused song
                        ''')

    if chse == "-random":
        ask_automatic = input("make it pass to the next song automaticlly? y/n ")
        if ask_automatic == "y":
            print(list_of_files_len)
            for l in range(list_of_files_len):
                a = random.randint(0, list_of_files_len)
                print(a)
                play_music(list_of_files[a])

        if ask_automatic == "n":
            print(list_of_files_len)
            a = random.randint(0, list_of_files_len)
            print(a)
            play_music(list_of_files[a])
