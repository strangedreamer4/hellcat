import tkinter as tk
from tkinter import ttk, messagebox
import subprocess

class InstallerApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Installer")
        self.root.geometry("600x200")

        self.header_frame = tk.Frame(self.root)
        self.header_frame.pack(side="top", fill="x")

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(side="top", fill="x")

        self.create_header()
        self.create_buttons()

    def create_header(self):
        self.welcome_label = tk.Label(self.header_frame, text="Welcome to HellCat!", font=("Arial", 18))
        self.welcome_label.pack(pady=20)

        self.progress_label = tk.Label(self.header_frame, text="", font=("Arial", 12))
        self.progress_label.pack(pady=10)

        self.progress_bar = ttk.Progressbar(self.header_frame, length=400, mode="determinate")
        self.progress_bar.pack(pady=10)

    def create_buttons(self):
        self.install_button = tk.Button(self.button_frame, text="Install", command=self.install_dependencies)
        self.install_button.pack(side="left", padx=10)

        self.uninstall_button = tk.Button(self.button_frame, text="Uninstall", command=self.uninstall_app)
        self.uninstall_button.pack(side="left", padx=10)

        self.update_button = tk.Button(self.button_frame, text="Update", command=self.update_app)
        self.update_button.pack(side="left", padx=10)

        self.run_button = tk.Button(self.button_frame, text="Run App", command=self.launch_app)
        self.run_button.pack(side="left", padx=10)

        self.exit_button = tk.Button(self.button_frame, text="Exit", command=self.exit_app)
        self.exit_button.pack(side="right", padx=10)

        self.dependencies = ["tk", "Pillow", "pyrebase4", "firebase", "gTTS", "playsound"]
        self.current_dependency_index = 0

    def install_dependencies(self):
        self.install_button.config(state="disabled")
        self.progress_label.config(text="Installing dependencies...")

        self.progress_bar["maximum"] = len(self.dependencies)
        self.progress_bar["value"] = 0

        self.install_next_dependency()

    def install_next_dependency(self):
        if self.current_dependency_index < len(self.dependencies):
            dependency = self.dependencies[self.current_dependency_index]
            self.progress_label.config(text=f"Installing {dependency}...")

            try:
                subprocess.check_call(["pip3", "install", dependency])
            except subprocess.CalledProcessError as e:
                self.progress_label.config(text="Failed to install dependencies.")
                return

            self.progress_bar["value"] += 1
            self.current_dependency_index += 1
            self.root.after(100, self.install_next_dependency)
        else:
            self.progress_label.config(text="Dependencies installed.")
            self.display_instructions()

    def display_instructions(self):
        self.instructions_label = tk.Label(self.header_frame, text="Installation complete!\nClick the 'Run App' button to launch the HellCat application.", font=("Arial", 12))
        self.instructions_label.pack(pady=20)

    def launch_app(self):
        try:
            subprocess.Popen(["python3", ".hellcat.py"])  # Launch the HellCat application
        except Exception as e:
            print("Error launching the app:", e)

    def uninstall_app(self):
        try:
            subprocess.Popen(["./uninstall.sh"])  # Run the uninstall script
        except Exception as e:
            print("Error running uninstall script:", e)

    def update_app(self):
        try:
            subprocess.Popen(["./update.sh"])  # Run the update script
        except Exception as e:
            print("Error running update script:", e)

    def exit_app(self):
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.root.quit()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = InstallerApp()
    app.run()
