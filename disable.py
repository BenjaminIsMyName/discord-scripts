# import os


# """
# This module's purpose is to disable discord, to block incoming calls & messages.
# That's all.
# """


# def disable_discord():
#     return os.system("taskkill /f /im Discord.exe") == 0

import psutil


def disable_discord():
    found = False
    for process in psutil.process_iter():
        if process.name() == "Discord.exe":
            process.kill()
            found = True
    return found


# import win32process


# def disable_discord():
#     for process in win32process.EnumProcesses():
#         hProcess = win32process.OpenProcess(
#             win32process.PROCESS_QUERY_INFORMATION, False, process)
#         if hProcess:
#             exe_name = win32process.GetModuleFileNameEx(hProcess, 0)
#             if exe_name == "Discord.exe":
#                 win32process.TerminateProcess(hProcess, 0)
#                 return True
#     return False

# import psutil


# def disable_discord():
#     for proc in psutil.process_iter():
#         try:
#             if proc.name() == "Discord.exe":
#                 proc.terminate()
#                 return True
#         except psutil.NoSuchProcess:
#             pass
#     return False


if __name__ == "__main__":
    if disable_discord():
        input("Discord is disabled, click anywhere to exit")
    else:
        input("Discord is not activated")
