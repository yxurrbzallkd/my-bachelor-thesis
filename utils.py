import cv2


def play_video(path,w=600,h=300):
    cap = cv2.VideoCapture(path)

    while True:
        ret, frame = cap.read()
        if not ret:
            print('not ret')
            break
        cv2.imshow('video', cv2.resize(frame,(w,h)))
        if cv2.waitKey(1) == ord('q'): break
            
    cv2.destroyAllWindows()


def play_videos(paths, w=600, h=300, N=300):
    caps = [cv2.VideoCapture(path) for path in paths]
    
    i, bad = 0, [0]*len(caps)
    while i < N:
        for n,(path,cap) in enumerate(zip(paths,caps)):
            ret, frame = cap.read()
            if not ret:
                print("not ret")
                bad[n] += 1
            else:
                cv2.imshow(path, cv2.resize(frame,(w,h)))
        if cv2.waitKey(1) == ord('q'): break
        i += 1

    for cap in caps:
        cap.release()
    cv2.destroyAllWindows()
    return bad

   

