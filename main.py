from FaceAndEyeRecognition import FaceEyeRecognition
import tkinter as tk
import ObjectDetection
root = tk.Tk()
root.title("Image Recognition")
root.geometry("400x400")
def clear_window(window):
    for widget in window.winfo_children():
        widget.destroy()
def open_object_recognition_window():
    root.withdraw()
    ObjectDetection.UploadImage()
    root.deiconify()


def open_face_eye_recognition_window():
    root.withdraw()
    FaceEyeRecognition()
    root.deiconify()

main_label = tk.Label(root, text="pick which option you want to try",font=("Helvetica", 16))

main_label.pack(pady=20)

button_frame = tk.Frame(root)
button_frame.pack()

first_button = tk.Button(button_frame, text="Object Recognition",width=20,height=3, command=open_object_recognition_window)
first_button.pack(side="left", padx=10)

second_button = tk.Button(button_frame, text="Face and Eye Recognition",width=20,height=3, command=open_face_eye_recognition_window)
second_button.pack(side="left", padx=10)

root.mainloop()
