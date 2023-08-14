
import tkinter as tk
from PIL import Image, ImageTk
import pyrebase
import time
import tkinter.messagebox
from gtts import gTTS
import playsound

# Firebase configuration
firebaseConfig = {
    "apiKey": "AIzaSyBCBUGoKQecD5R-uWc9CLs3TNa5ll9jA4M",
    "authDomain": "vip-95a43.firebaseapp.com",
    "databaseURL": "https://vip-95a43-default-rtdb.europe-west1.firebasedatabase.app",
    "projectId": "vip-95a43",
    "storageBucket": "vip-95a43.appspot.com",
    "messagingSenderId": "787111306016",
    "appId": "1:787111306016:web:c54ab830474afb9a06ad45",
    "measurementId": "G-PZJVC849Y4"
}

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

# Tkinter GUI
class ChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hacker Chat Terminal")
        self.root.geometry("800x800")
        self.root.configure(bg="black")

        # Load the animation image
        self.animation_image = Image.open(".animation .jpg")
        self.animation_photo = ImageTk.PhotoImage(self.animation_image)
        self.animation_label = tk.Label(self.root, image=self.animation_photo, bg="black")
        self.animation_label.place(relx=0.5, rely=0.5, anchor="center")

        # Call a function to show loading effect
        self.root.after(3000, self.show_loading_effect)

    def generate_welcome_audio(self):
        welcome_text = "Opening Hellcat"  # Customize the welcome message
        tts = gTTS(text=welcome_text, lang="en")
        tts.save("welcome_message.mp3")

    def show_loading_effect(self):
        self.animation_label.destroy()  # Remove the animation label
        self.generate_welcome_audio()  # Generate the welcome audio

        # Play the welcome audio
        playsound.playsound("welcome_message.mp3", True)  # Replace with the path to your welcome message audio file

        # Display loading message
        self.loading_label = tk.Label(self.root, text="Loading...", fg="green", bg="black")
        self.loading_label.place(relx=0.5, rely=0.5, anchor="center")

        # Simulate loading delay
        self.root.after(2000, self.start_app)

    def start_app(self):
        self.loading_label.destroy()  # Remove the loading label

        self.username_frame = tk.Frame(self.root, bg="black")
        self.username_frame.pack(pady=10)

        self.username_label = tk.Label(self.username_frame, text="Username:", fg="green", bg="black")
        self.username_label.pack(side=tk.LEFT)

        self.username_entry = tk.Entry(self.username_frame, bg="black", fg="green", insertbackground="green")
        self.username_entry.pack(side=tk.LEFT)

        self.message_frame = tk.Frame(self.root, bg="black")
        self.message_frame.pack(pady=10)

        self.messages_text = tk.Text(self.message_frame, bg="black", fg="green", insertbackground="green", wrap=tk.WORD)
        self.messages_text.pack(fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.message_frame, command=self.messages_text.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.messages_text.config(yscrollcommand=self.scrollbar.set)

        self.input_field = tk.Entry(self.root, bg="black", fg="green", insertbackground="green")
        self.input_field.pack(pady=10, padx=20, fill=tk.X, expand=True)

        self.button_frame = tk.Frame(self.root, bg="black")
        self.button_frame.pack()

        self.send_button = tk.Button(self.button_frame, text="Send", bg="black", fg="green", command=self.send_message)
        self.send_button.pack(side=tk.LEFT, padx=10)

        self.clear_button = tk.Button(self.button_frame, text="Clear", bg="black", fg="green", command=self.clear_messages)
        self.clear_button.pack(side=tk.LEFT, padx=10)

        self.exit_button = tk.Button(self.button_frame, text="Exit", bg="black", fg="green", command=self.exit_app)
        self.exit_button.pack(side=tk.LEFT, padx=10)

        self.messages_ref = db.child("messages")
        self.stream = self.messages_ref.stream(self.on_message_change)

        # Bind Enter key to send_message function
        self.root.bind("<Return>", self.send_message)

    def send_message(self, event=None):
        username = self.username_entry.get()
        message = self.input_field.get()
        self.input_field.delete(0, tk.END)
        if username and message:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")  # Get current date and time
            db.child("messages").push({"username": username, "message": message, "timestamp": timestamp})

    def on_message_change(self, message):
        if message["event"] == "put":
            data = message["data"]
            if data:
                username = data.get("username", "")
                message_text = data.get("message", "")
                timestamp = data.get("timestamp", "")
                if username and message_text:
                    self.messages_text.insert(tk.END, f"{timestamp} - {username}: {message_text}\n")
                    self.messages_text.see(tk.END)

    
    def clear_messages(self):
        self.messages_text.delete("1.0", tk.END)

    def exit_app(self):
        if tkinter.messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.stream.close()
            self.root.quit()
            
        # Save chat history to a text file
        chat_history = self.messages_text.get("1.0", tk.END)
        with open("chat_log.txt", "w") as file:
            file.write(chat_history)

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatApp(root)
    root.mainloop()
