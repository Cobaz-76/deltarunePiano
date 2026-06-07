# wait time is how longer after pressing enter the program waits (in seconds) before starting the macro
waitTime = 5

# noteList is (duh) what notes will be played. This uses the midi scale (Google it). The program will try to find how to transpose the song to allow the most of these to be played. 
# You can also just input these directions to bypass the conversion: ● ➡ ⬊ ⬇ ⬋ ⬅ ⬉ ⬆ ○ ⇨ ⬂ ⇩ ⬃ ⇦ ⬁ ⇧
noteList = [74, 71, 67, 62, 64, 66, 67, 64, 67, 62, 69, 74, 71, 67, 64, 66, 67, 69, 71, 69, 71, 72, 71, 69, 74, 71, 69, 67, 69, 71, 67, 64, 67, 64, 62, 62, 67, 71, 69, 62, 67, 71, 69, 71, 72, 74, 71, 67, 69, 62, 67]

# beatList is how long each note is played. It corresponds 1 to 1 with the notes list. Each value is in quarter seconds. So 4 will play it for a full second.
beatList = [3, 3, 3, 3, 1, 1, 1, 2, 1, 6, 3, 3, 3, 3, 1, 1, 1, 2, 1, 5, 1, 1, 1, 1, 2, 1, 1, 4, 1, 2, 1, 2, 1, 1, 4, 1, 2, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 5]

# If you want to post a video of a song played with this script, please link to the repository and/or my youtube channel in the description:
# Repository https://github.com/Cobaz-76/deltarunePiano
# YT channel: https://www.youtube.com/@cobaz-76


import time
try:
    import keyboard
except ModuleNotFoundError:
    print("You do not have the keyboard modules intalled. Please run [pip install keyboard].")
    while True:
        input('')

allowedNotes = {
        71:'c',
        73:'c, right',
        75:'c, right, down',
        76:'c, down',
        78:'c, left, down',
        80:'c, left',
        82:'c, up, left',
        83:'c, up',
        85:'right',
        87:'right, down',
        88:'down',
        90:'down, left',
        92:'left',
        94:'up, left',
        95:'up',
        '●':'c, up',
        '➡':'right',
        '⬊':'right, down',
        '⬇':'down',
        '⬋':'left, down',
        '⬅':'left',
        '⬉':'left, up',
        '⬆':'up',
        '○':'c',
        '⇨':'c, right',
        '⬂':'c, right, down',
        '⇩':'c, down',
        '⬃':'c, down, left',
        '⇦':'c, left',
        '⬁':'c, up, left',
        '⇧':'c, up'
}

arrows = {
        71:'○',
        73:'⇨',
        75:'⬂',
        76:'⇩',
        78:'⬃',
        80:'⇦',
        82:'⬁',
        83:'●',
        85:'➡',
        87:'⬊',
        88:'⬇',
        90:'⬋',
        92:'⬅',
        94:'⬉',
        95:'⬆'
}

bestNum = [0, 1000]

for item in ['●', '➡', '⬊', '⬇', '⬋', '⬅', '⬉', '⬆', '○', '⇨', '⬂', '⇩', '⬃', '⇦', '⬁', '⇧']:
    if item in noteList:
        check = False
        break
    else:
        check = True

if check:
    for num in range(25):
        notes = noteList
        yes = 0
        no = 0

        notes = [note+(71-min(notes)+num) for note in notes]

        for note in notes:
            if note in allowedNotes:
                yes += 1
            else:
                no += 1
        if no == 0:
            print(f"Found working configuration! Offset: {num}")
            output = "Final directions: "
            for item in notes:
                output += f"{arrows[item]} "
            print(output)
            break
        elif num == 24:
            print(f"Couldn't find working configuration, using {bestNum[0]} offset which had {bestNum[1]} missing notes.")
            notes = [note+(71-min(notes)+bestNum[0]) for note in notes]
        elif no < bestNum[1]:
            bestNum[0] = num
            bestNum[1] = no

inp = input('\nPress enter to start countdown\n')
if inp != '':
    notes = [note+(71-min(notes)+int(inp)) for note in notes]
    yes = 0
    no = 0
    for note in notes:
        if note in allowedNotes:
            yes += 1
        else:
            no += 1
    print(f"Hard switching to offset {inp} which has {no} missing notes.")

for num in range(waitTime):
    print(f"Starting song in {num*-1 + waitTime} seconds")
    time.sleep(1)

for count in range(len(notes)):
    try:
        if count != 0:
            keyboard.release(allowedNotes[notes[count-1]])
        keyboard.press(allowedNotes[notes[count]])
        keyboard.press('z')
        time.sleep(((1/4)*beatList[count])/2)
        keyboard.release('z')
        time.sleep(((1/4)*beatList[count])/2)
    except KeyError:
        time.sleep((1/4)*beatList[count])

try:
    keyboard.release(allowedNotes[notes[-1]])
except KeyError:
    pass