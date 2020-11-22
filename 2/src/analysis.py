import os
import time
from music import switch_music
from video import switch_video
def ana(media):
    emotions = {
        'anger': 0,
        'disgust': 1,
        'fear': 2,
        'happy': 3,
        'sad': 4,
        'surprised': 5,
        'neutral': 6,
        'contempt': 7
    }
    out = [0] * 8;
    with  open("./res.txt", 'r') as fp:
        tmp = fp.readlines();
        for i in range(0, len(tmp)):
            tmp[i] = tmp[i].rstrip('\n')
            out[emotions[tmp[i]]] += 1;
    fp.close()
    if out[6] >= 90:
        num = 6
    else:
        out[6] = 0
        num = out.index(max(out))
        print(out)
    choice1 = 0
    fout = open("./f_em.txt", 'w');
    if num == 0 or num == 1 or num == 2 or num == 4:
        choice1 = 1
    elif num == 6 or num == 7:
        choice1 = 2
    elif num == 3 or num == 5:
        choice1 = 3
    if media == 1:
        switch_music(choice1)
    else:
        switch_video(choice1)
    fout.truncate()
    fout.write(str(num))
    fout.close()



