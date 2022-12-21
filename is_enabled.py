# import subprocess


# def is_discord_enabled():
#     for process in subprocess.check_output("tasklist").split():
#         if "Discord.exe" in process.decode("utf-8"):
#             return True
#     return False

import psutil


def is_discord_enabled():
    for process in psutil.process_iter():
        if process.name() == "Discord.exe":
            return True
    return False


if __name__ == "__main__":
    if is_discord_enabled():
        print("Discord is enabled.")
    else:
        print("Discord is not enabled.")
