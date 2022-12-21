from tkinter import *
from disable import disable_discord
from enable import enable_discord
from is_enabled import is_discord_enabled

app = Tk()
app.resizable(width=False, height=False)
# Always keep window on top of others
app.call("wm", "attributes", ".", "-topmost", "true")
app.title("BenDiscord")


label = Label(
    text=f"Current: {'Enabled!' if is_discord_enabled() else 'Disabled!'}")
label.grid(row=0, columnspan=2, pady=(0, 8))  # margin of 8 to the bottom


def update_label():
    label.configure(
        text=f"Current: {'Enabled!' if is_discord_enabled() else 'Disabled!'}")
    app.after(200, update_label)


app.configure(padx=10, pady=10)

Button(text="✔️Enable", padx=30, bg="#007820",
       fg="white", command=enable_discord).grid(row=1, column=0, padx=(0, 10))  # margin of 10 to the right
Button(text="❌     Disable", padx=30, bg="#780016",
       fg="white", command=disable_discord).grid(row=1, column=1)

app.after(200, update_label)
app.mainloop()
