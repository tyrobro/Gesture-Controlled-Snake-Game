import cv2 
import mediapipe as mp
cam = cv2.VideoCapture(0)
frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('recording.mp4', fourcc, 20.0, (frame_width, frame_height))
THRESHOLD = 50
prev_x, prev_y = 0, 0
timer = 0
COOLDOWN_FRAMES = 10
while True: 
    ret, frame = cam.read()
    frame = cv2.flip(frame, 1)
    rgbframe = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgbframe)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            index_finger = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            h, w, c = frame.shape
            cx, cy = int(index_finger.x*w), int(index_finger.y*h)
            dx = cx - prev_x
            dy = cy - prev_y
            if(timer == 0):
                if dx > THRESHOLD:
                    print("SWIPE RIGHT")
                    timer = COOLDOWN_FRAMES
                elif dx < -THRESHOLD:
                    print("SWIPE LEFT")
                    timer = COOLDOWN_FRAMES
                elif dy > THRESHOLD:
                    print("SWIPE DOWN")
                    timer = COOLDOWN_FRAMES
                elif dy <- THRESHOLD:
                    print("SWIPE UP")
                    timer = COOLDOWN_FRAMES
        prev_x, prev_y = cx, cy
    if timer > 0:
        timer -=1
    out.write(frame)
    cv2.imshow('Camera', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
out.release()
cv2.destroyAllWindows()