import os
import platform
from colorama import Fore as c
from colorama import Back as b
from .frame import frame

def fetch(width):
    data = platform.freedesktop_os_release()

    name = data['NAME']
    version = data['VERSION']

    kernel = platform.system()
    kernel_version = platform.release()
    shell = os.environ['SHELL']
    username = os.environ['USER']

    architecture = platform.machine()

    distro_icon = f'{c.WHITE}{c.RESET}'
    match(name):
        case 'Ubuntu':
            distro_icon = f'{c.YELLOW}{c.RESET}'
        case 'Debian':
            distro_icon = f'{c.RED}{c.RESET}'
        case 'Fedora':
            distro_icon = f'{c.CYAN}{c.RESET}'
        case 'Arch':
            distro_icon = f'{c.CYAN}{c.RESET}'
        case 'Kali':
            distro_icon = f'{c.CYAN}{c.RESET}'
        case 'Mint':
            distro_icon = f'{c.LIGHTGREEN_EX}{c.RESET}'
        case 'RedHat':
            distro_icon = f'{c.RED}{c.RESET}'
        case 'Mageia':
            distro_icon = f'{c.CYAN}{c.RESET}'

    print(frame(
f"""{c.GREEN}{c.RESET} {kernel} {kernel_version}
{distro_icon} {name} {version} {architecture}
{c.BLUE}󰆍{c.RESET} {shell}
{c.YELLOW}{c.RESET} {username}

{b.BLACK}   {b.RED}   {b.GREEN}   {b.YELLOW}   {b.BLUE}   {b.MAGENTA}   {b.CYAN}   {b.WHITE}   {b.RESET}
{b.LIGHTBLACK_EX}   {b.LIGHTRED_EX}   {b.LIGHTGREEN_EX}   {b.LIGHTYELLOW_EX}   {b.LIGHTBLUE_EX}   {b.LIGHTMAGENTA_EX}   {b.LIGHTCYAN_EX}   {b.LIGHTWHITE_EX}   {b.RESET}"""
, width))
   