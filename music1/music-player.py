import random
import vlc
import time
import os
import numpy

stop_or_nah = None


list_of_files, counter = [], 0
for file in os.listdir("."):
    if file.endswith(".m4a") or file.endswith(".mp3"):
        print(len(list_of_files), os.path.join(".", file))
        list_of_files.append(file)
list_of_files_len = len(list_of_files)


def play_music(song_number):
    print ('play music')
    media_player = vlc.MediaPlayer(song_number)
    media_player.play()
    time.sleep(1)
    value = media_player.is_playing()
    print(value)
    music_command = input("do what you want now")
    run_action_by_command(media_player, music_command)


def play_directory(directory):
    print ('pd')
    number_of_song_playing = 0
    for f in range(list_of_files_len):
        print(stop_or_nah)
        if stop_or_nah == 1:
            return
        print("youre in pd loop")
        play_music(directory[number_of_song_playing])
        number_of_song_playing = number_of_song_playing + 1


def run_action_by_command(song, inp):
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
        play_directory(list_of_files)

    if inp == "e":
        exit()

    if inp == "sk":
        song.stop()

    if inp == "s":
        song.stop()
        global stop_or_nah
        stop_or_nah = 1

    if inp == "p":
        song.pause()
        continu = input("would you like to resume? y/n ")
        if continu == "y":
            song.play()
        if continu == "n":
            time.sleep(0)

    if inp == "r":
        ask_automatic = input("make it pass to the next song automatically? y/n ")
        if ask_automatic == "y":
            random_list_of_files = numpy.array(list_of_files)
            numpy.random.shuffle(random_list_of_files)
            print("the playlist is:",
random_list_of_files)
            play_directory(random_list_of_files)

        if ask_automatic == "n":
            a = random.randint(0, list_of_files_len)
            if a > 0:
                a = a - 1
            play_music(list_of_files[a])


while True:
    main_command = input('''
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
    run_action_by_command(song="pass", inp=main_command)
