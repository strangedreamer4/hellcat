import tkinter as tk
from tkinter import ttk
import subprocess
from tkinter import messagebox

class InstallerApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Installer")
        self.root.geometry("400x300")

        self.welcome_label = tk.Label(self.root, text="Welcome to HellCat!", font=("Arial", 18))
        self.welcome_label.pack(pady=20)

        self.progress_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.progress_label.pack(pady=10)

        self.progress_bar = ttk.Progressbar(self.root, length=300, mode="determinate")
        self.progress_bar.pack(pady=10)

        self.install_button = tk.Button(self.root, text="Install", command=self.install_dependencies)
        self.install_button.pack()

        self.run_button = tk.Button(self.root, text="Run App", command=self.launch_app)
        self.run_button.pack()

        self.exit_button = tk.Button(self.root, text="Exit", command=self.exit_app)
        self.exit_button.pack()

        self.dependencies = ["tk", "Pillow", "pyrebase4"]
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
        self.instructions_label = tk.Label(self.root, text="Installation complete!\nClick the 'Run App' button to launch the HellCat application.", font=("Arial", 12))
        self.instructions_label.pack(pady=20)

    def launch_app(self):
        try:
            subprocess.Popen(["python3", "hellcat.py"])  # Launch the HellCat application
        except Exception as e:
            print("Error launching the app:", e)

    def exit_app(self):
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.root.quit()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = InstallerApp()
    app.run()
