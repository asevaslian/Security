import cv2
from django.shortcuts import render
from django.http import StreamingHttpResponse
from django.http import HttpResponse


def generate_frames():
    camera = cv2.VideoCapture(0)  # Use 0 for the default camera
    while True:
        success, frame = camera.read()
        if not success:
            break

        # Encode the frame as JPEG
        _, jpeg = cv2.imencode('.jpg', frame)

        # Yield the frame in byte form
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')

    camera.release()

def camera_1(request):
    response = StreamingHttpResponse(generate_frames(),content_type='multipart/x-mixed-replace; boundary=frame')
    return response