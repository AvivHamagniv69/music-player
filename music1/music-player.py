import random
import vlc
import time
import os
import numpy
from multiprocessing import *

list_of_files, counter = [], 0
for file in os.listdir("."):
    if file.endswith((".m4a", ".mp3", ".flac")):
        print(len(list_of_files), os.path.join(".", file))
        list_of_files.append(file)
list_of_files_len = len(list_of_files)


def music_check(check, song, inp):
    while check == 1:
        time.sleep(1)
    else:
        song.stop()
        inp = False


def play_music(song_number):
    media_player = vlc.MediaPlayer(song_number)
    media_player.play()
    time.sleep(0.1)
    value = media_player.is_playing()
    music_command = None
    playing_check = Process(target=music_check, args=(value, media_player, music_command))
    playing_check.start()
    music_command = input("do what you want now | ")
    run_action_by_command(media_player, music_command, playing_check)


stop_or_nah = None
def play_directory(directory):
    number_of_song_playing = 0
    for f in range(list_of_files_len):
        if stop_or_nah == 1:
            return
        play_music(directory[number_of_song_playing])
        number_of_song_playing = number_of_song_playing + 1


def kill_process(song_2, process_check):
    try:
        song_2.stop()
        process_check.kill()
    except:
        pass
def run_action_by_command(song, inp, process):
    global stop_or_nah
    try:
        play_music(list_of_files[int(inp)])
    except:
        pass

    if inp == "h":
        print('''
        list of all commands:
        h = lists all commands
        e = exits the app
        s = stops the music 
        pd = plays your entire directory:
        r = plays the entire directory in random order.
        sk = skips the song and moves to the next song in line
        p = pauses the song and allows you to resume it later
        r = resumes the paused song

        ''')

    if inp == "pd":
        stop_or_nah = 0
        kill_process(song, process)
        play_directory(list_of_files)

    if inp == "e":
        try:
            process.kill()
        except:
            pass
        exit()

    if inp == "sk":
        kill_process(song, process)

    if inp == "s":
        kill_process(song, process)
        stop_or_nah = 1

    if inp == "p":
        try:
            song.pause()
            should_stop = input("would you like to resume? y/n | ")
            if should_stop == "y":
                song.play()
                music_command = input("do what you want now | ")
                run_action_by_command(song, music_command)
            if should_stop == "n":
                time.sleep(0)
        except:
            pass

    if inp == "r":
        kill_process(song, process)
        ask_automatic = input("make it pass to the next song automatically? y/n | ")
        if ask_automatic == "y":
            random_list_of_files = numpy.array(list_of_files)
            numpy.random.shuffle(random_list_of_files)
            print("the playlist is:",
                  random_list_of_files)
            play_directory(random_list_of_files)

        if ask_automatic == "n":
            random_music = random.randint(0, list_of_files_len)
            if random_music > 0:
                random_music = random_music - 1
            play_music(list_of_files[random_music])

    else:
        pass


while True:
    main_command = input('''
list of all commands:
choose a song number
d = print the entire directory
h = lists all commands
e = exits the app
s = stops the music
pd = plays your entire directory:
r = plays the entire directory in random order.
sk = skips the song and moves to the next song in line
p = pauses the song and allows you to resume it later
r = resumes the paused song

enter your command here:
''')
    run_action_by_command(song="nothing", inp=main_command, process="none")
