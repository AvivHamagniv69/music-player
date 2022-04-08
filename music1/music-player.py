#!/usr/bin/python3
import random
import vlc
import time
import os
import numpy

list_of_files = []
counter = 0
for file in os.listdir("."):
    if file.endswith(".m4a") or file.endswith(".mp3"):
        print(counter, os.path.join(".", file))
        list_of_files.append(file)
        counter = counter + 1
counter = counter - 1
list_of_files_len = len(list_of_files)
print(counter)


def run_action_by_command(song, inp, is_song_playing):
    if inp == "exit":
        exit()

    if inp == "stop":
        song.stop()

    if inp == "pause":
        song.pause()
        continu = input("would you like to resume? y/n ")
        if continu == "y":
            song.play()
            while is_song_playing == 1:
                command = input("do what you want: ")
                run_action_by_command(song, command, is_song_playing)
        if continu == "n":
            time.sleep(0)
    if inp == "skip":
        song.stop()


def play_music(song_number):
    media_player = vlc.MediaPlayer(song_number)
    media_player.play()
    time.sleep(1)
    value = media_player.is_playing()

    while value == 1:
        command = input("do what you want: ")

        run_action_by_command(media_player, command, value)


def pd():
    number_of_song_playing = 0
    for f in range(list_of_files_len):
        play_music(list_of_files[number_of_song_playing])
        number_of_song_playing = number_of_song_playing + 1


while True:
    chse = input("choose the number related to the song you want to play (type -help to see all commands) ")

    if chse == "exit":
        quit()

    try:
        chse_int = int(chse)
        print(list_of_files)
        play_music(list_of_files[chse_int])
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
-random = plays the entire directory in random order.
stop = exits the program and stops the music
skip = skips the song and moves to the next song in line
pause = pauses the song and allows you to resume it later
resume = resumes the paused song
                        ''')

    if chse == "-random":
        ask_automatic = input("make it pass to the next song automatically? y/n ")
        if ask_automatic == "y":
            random_list_of_files = numpy.array(list_of_files)
            numpy.random.shuffle(random_list_of_files)
            print("the playlist is:",
                  random_list_of_files)
            counter1 = 0
            for l in range(list_of_files_len):
                play_music(random_list_of_files[counter1])
                counter1 = counter1+1

        if ask_automatic == "n":
            print(list_of_files_len)
            a = random.randint(0, list_of_files_len)
            if a > 0:
                a = a - 1
            play_music(list_of_files[a])
