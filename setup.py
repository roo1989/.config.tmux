import os
import shutil

from pathlib import Path

if __name__ == '__main__':
    print("Checking if Homebrew is installed...")
    if shutil.which("brew") is None:
        install_brew = input("Homebrew is not installed. Would you like me to install it Y/n: ")
        if install_brew.lower() == "y":
            os.system("/bin/bash -c \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\"")

    print("Checking dependencies...")
    if shutil.which("tmux") is None:
        install_tmux = input("Tmux is not installed. Would you like me to install it Y/n: ")
        if install_tmux.lower() == "y":
            os.system("brew install tmux")


    print("Checking if tmux plugin manager is installed...")
    if Path("~/.tmux/plugins/").exists() is False:
        install_tpm = input("Tmux Plugin Manager is not installed. Would you like me to install it Y/n: ")
        if install_tpm.lower() == "y":
            os.system("git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm")

    print("Symlinking tmux configuration...")
    os.system("ln -s -f .tmux.conf ~/.tmux.conf")

    print("Done...")
