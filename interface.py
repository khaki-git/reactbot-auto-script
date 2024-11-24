import customtkinter as ctk
from tkinter import filedialog
import video

class Core(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x300")
        self.title("ReactBot Video Generator")
        self.iconbitmap("reactbot.ico")

        self.selection_video = ""

        self.title_label = ctk.CTkLabel(self, text="Reactbot Video Generator", font=("Arial", 25))
        self.title_label.pack(padx=5, pady=15)

        self.select_button = ctk.CTkButton(self, text="Select Video", command=self.select_vid)
        self.select_button.pack(padx=5, pady=5)

        self.render_button = ctk.CTkButton(self, text="Render", command=self.render)
        self.render_button.pack(padx=5, pady=5)

    def select_vid(self):
        opened_contents = filedialog.askopenfilename(filetypes=[("Image Files", ".jpg .png"), ("Video Files", ".mp4")])
        self.selection_video = opened_contents

    def render(self):
        if self.selection_video == "":
            return
        output_path = filedialog.asksaveasfilename(filetypes=[("MP4 Video Files", ".mp4")])
        if not output_path.endswith(".mp4"):
            output_path = output_path + ".mp4"
        print(self.selection_video, output_path)
        if output_path != "":
            video.generate_video(self.selection_video, output_path)

window = Core()
window.mainloop()