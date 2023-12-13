import cv2
import numpy as np
from tracker import *
import cvzone
import mediapipe as mp
import json
from websockets.sync.client import connect
from ultralytics import YOLO

project_name = "PEOPLE COUNTER"

# câmera: 0, 1...
# video: "./[nome].[formato]"
video_capture = cv2.VideoCapture("two.mp4")

cv2.namedWindow(project_name)
tracker = Tracker()

# largura e altura da tela
win_width = 1028
win_height = 500


# a largura das caixas
a2 = win_width
b1 = 0

# posição das caixas no eixo y
a1 = 400
b2 = a1 - 60

# complemento de distância das caixas no eixo y
M = -270

# a distancia entre as duas caixas
d = 300

area1 = [(b1, a1 + M), (b1, b2 + M), (a2, b2 + M), (a2, a1 + M)]
area2 = [(vertex[0], vertex[1] + d) for vertex in area1]

er = {}
ex = {}

counter1 = []
counter2 = []

red = (0, 0, 255)
green = (0, 255, 0)
white = (255, 255, 255)

model = YOLO("yolov8n.pt")

with connect("ws://localhost:8002") as websocket:
    while True:
        ret, frame = video_capture.read()

        if not ret:
            break

        frame = cv2.resize(frame, (win_width, win_height))

        list = []

        results = model.predict(frame)
        detection_count = 0
        person_count = 0

        for r in results:
            boxes = r.boxes
            detection_count = r.boxes.shape[0]
        
            for i in range(detection_count):
                cls = int(boxes.cls[i].item())
                bb = boxes.xyxy[i]

                if cls == 0:  # Destaque tanto pessoas (cls == 0) quanto bolsas (cls == 26)
                    x, y, w, h = map(int, bb)
                    
                    if cls == 0:
                        cv2.rectangle(frame, (x, y), (w, h), (0, 255, 0), 3)  # Cor verde para pessoas
                        list.append([x, y, w, h])
                        person_count += 1

        bbox_idx = tracker.update(list)
        for bbox in bbox_idx:
            x1, y1, x2, y2, id = bbox
            cx = int(x1 + x1 + x2) // 2
            cy = int(y1 + y1 + y2) // 2

            result = cv2.pointPolygonTest(np.array(area1, np.int32), ((cx, cy)), False)

            if result >= 0:
                er[id] = (cx, cy)

            if id in er:
                result1 = cv2.pointPolygonTest(
                    np.array(area2, np.int32), ((cx, cy)), False
                )

                if result1 >= 0:
                    cv2.rectangle(frame, (x1, y1), (x2 + x1, y2 + y1), green, 3)
                    cvzone.putTextRect(frame, f"{id}", (cx, cy), 2, 2)
                    cv2.circle(frame, (cx, cy), 5, green, -1)

                    if counter1.count(id) == 0:
                        try:
                            websocket.send(json.dumps({"payload": "ENTER"}))
                        except Exception:
                            print("Erro ao enviar websocket")
                        counter1.append(id)

            result2 = cv2.pointPolygonTest(np.array(area2, np.int32), ((cx, cy)), False)

            if result2 >= 0:
                ex[id] = (cx, cy)

            if id in ex:
                result3 = cv2.pointPolygonTest(
                    np.array(area1, np.int32), ((cx, cy)), False
                )

                if result3 >= 0:
                    cv2.rectangle(frame, (x1, y1), (x2 + x1, y2 + y1), red, 3)
                    cvzone.putTextRect(frame, f"{id}", (cx, cy), 2, 2)
                    cv2.circle(frame, (cx, cy), 5, green, -1)

                    if counter2.count(id) == 0:
                        try:
                            websocket.send(json.dumps({"payload": "ENTER"}))
                        except Exception:
                            print("Erro ao enviar websocket")
                        counter2.append(id)

        cv2.polylines(frame, [np.array(area1, np.int32)], True, red, 2)
        cv2.polylines(frame, [np.array(area2, np.int32)], True, red, 2)

        Enter = len(counter1)
        Exit = len(counter2)

        cvzone.putTextRect(frame, f"EXIT:-{Enter}", (50, 60), 2, 2)
        cvzone.putTextRect(frame, f"ENTER:-{Exit}", (50, 130), 2, 2)
        cvzone.putTextRect(frame, f"Quantity:-{person_count}", (50, 200), 2, 2)

        cv2.imshow(project_name, frame)

        # Press 'Esc' to exit
        if cv2.waitKey(30) & 0xFF == 27:
            break


# Release the video capture and close windows
video_capture.release()
cv2.destroyAllWindows()
