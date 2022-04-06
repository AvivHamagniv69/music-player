#!/usr/bin/python3
import random
import vlc
import time
import os

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
    if inp == "stop":
        quit()

    if inp == "exit":
        song.stop()

    if inp == "pause":
        song.pause()
        continu = input("would you like to resume? y/n ")
        if continu == "y":
            song.play()
            while is_song_playing == 1:
                print(is_song_playing)
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
    print(value)

    command = input("do what you want: ")

    run_action_by_command(media_player, command, value)


def pd():
    number_of_song_playing = 0
    for f in range(list_of_files_len):
        play_music(list_of_files[number_of_song_playing])
        number_of_song_playing = number_of_song_playing + 1


def play_music_on_loop(var, var1):
    media_player = vlc.MediaPlayer(var[var1])
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
            print(value)
            while value == 1:
                command2 = input("do what you want: ")
                run_action_by_command(media_player, command2, value)
        if continu == "n":
            time.sleep(0)

    if command == "skip":
        media_player.stop()


while True:
    chse = input("choose the number related to the song you want to play (type -help to see all commands) ")

    if chse == "exit":
        quit()

    try:
        chse_int = int(chse)
        print(list_of_files)
        play_music_on_loop(list_of_files, chse_int)
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
            for l in range(list_of_files_len):
                a = random.randint(0, list_of_files_len)
                if a > 0:
                    a = a-1
                play_music(list_of_files[a])

        if ask_automatic == "n":
            print(list_of_files_len)
            a = random.randint(0, list_of_files_len)
            if a > 0:
                a = a - 1
            play_music(list_of_files[a])
