import ctypes
import datetime
import io
import os
import subprocess
import threading
import time
from ctypes import c_int
from datetime import datetime
from urllib.parse import unquote

import dearpygui.dearpygui as dpg
import DearPyGui_DragAndDrop as dpg_dnd
import psutil
import pyautogui
import pytesseract
import requests
import win32gui
from discord_webhook import DiscordWebhook
from filedialogs import open_file_dialog, save_file_dialog
from google_play_scraper import app
from PIL import Image
from pytz import timezone
from pyWinActivate import win_activate
from pywinauto import Application
from wscreenshot import Screenshot


def main():
    clear()
    set_title("PYAutomation")

    # Settings
    width = 600
    height = 300

    dpg.create_context()
    dpg.create_viewport(
        title="Viewport Title",
        width=width,
        height=height,
        decorated=False,
        clear_color=[0.0, 0.0, 0.0, 0.0],
    )

    # Drag handler
    def drag_viewport(sender, app_data):
        FRAME_PADDING_Y = 3
        _, drag_dx, drag_dy = app_data

        drag_start_y = dpg.get_mouse_pos(local=False)[1] - drag_dy
        title_bar_height = 2 * FRAME_PADDING_Y + dpg.get_text_size("")[1]
        if drag_start_y < title_bar_height:
            x_pos, y_pos = dpg.get_viewport_pos()
            dpg.set_viewport_pos((x_pos + drag_dx, max(0, y_pos + drag_dy)))

    with dpg.handler_registry():
        dpg.add_mouse_drag_handler(button=0, threshold=0, callback=drag_viewport)

    # Font
    with dpg.font_registry():
        dpg.add_font("font\\Roboto-Regular.ttf", 16, tag="ttf-font")

    dpg.bind_font("ttf-font")

    # Theme
    with dpg.theme() as global_theme:
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_style(dpg.mvStyleVar_TabRounding, 3)
            dpg.add_theme_style(dpg.mvStyleVar_GrabRounding, 3)
            dpg.add_theme_style(dpg.mvStyleVar_ChildRounding, 3)
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 3)
            dpg.add_theme_style(dpg.mvStyleVar_PopupRounding, 3)
            dpg.add_theme_style(dpg.mvStyleVar_WindowRounding, 3)
            dpg.add_theme_style(dpg.mvStyleVar_ScrollbarRounding, 3)

            dpg.add_theme_color(dpg.mvThemeCol_TabActive, (51, 105, 173))
            dpg.add_theme_color(dpg.mvThemeCol_Tab, (43, 80, 131))
            dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (21, 22, 23))
            dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (32, 50, 77))

    dpg.bind_theme(global_theme)

    # Window
    def set_viewport_always_top(sender, app_data):
        dpg.set_viewport_always_top(app_data)

    def exec_code_thread():
        try:
            code = dpg.get_value("code")
            exec(code)
        except Exception as error:
            print(error)

    def exec_code():
        try:
            thread = threading.Thread(target=exec_code_thread)
            thread.start()
        except Exception as error:
            print(error)

    def save_file():
        try:
            save_path = save_file_dialog()
            if save_path:
                with open(save_path, "w") as f:
                    f.write(dpg.get_value("code"))
        except Exception as error:
            dpg.set_value("popup_text", error)
            dpg.show_item("popup")

    def open_file():
        try:
            open_path = open_file_dialog()
            if open_path:
                with open(open_path, "r") as f:
                    content = f.read()
                    dpg.set_value("code", content)
                    return content
        except Exception as error:
            dpg.set_value("popup_text", error)
            dpg.show_item("popup")

    def on_f1_pressed():
        global mouse_pos1
        mouse_pos1 = dpg.get_mouse_pos()

    def on_f2_pressed():
        global mouse_pos2
        mouse_pos2 = dpg.get_mouse_pos()

    def on_f3_pressed():
        global mouse_pos3
        mouse_pos3 = dpg.get_mouse_pos()

    with dpg.handler_registry():
        dpg.add_key_press_handler(key=dpg.mvKey_F5, callback=exec_code)
        dpg.add_key_press_handler(key=dpg.mvKey_F1, callback=on_f1_pressed)
        dpg.add_key_press_handler(key=dpg.mvKey_F2, callback=on_f2_pressed)
        dpg.add_key_press_handler(key=dpg.mvKey_F3, callback=on_f3_pressed)

    with dpg.window(
        label="PYAutomation - Bt08s",
        width=width,
        height=height,
        on_close=lambda: dpg.stop_dearpygui(),
    ) as window:

        with dpg.menu_bar():
            with dpg.menu(label="File"):
                dpg.add_menu_item(label="Save", callback=save_file)
                dpg.add_menu_item(label="Open", callback=open_file)

            with dpg.menu(label="Settings"):
                dpg.add_menu_item(
                    label="Always on top", callback=set_viewport_always_top, check=True
                )

        dpg.add_input_text(multiline=True, width=584, height=205, tag="code")
        with dpg.group(horizontal=True, xoffset=294):
            dpg.add_button(
                label="EXECUTE",
                width=290,
                height=30,
                callback=exec_code,
                tag="execute_button",
            )
            with dpg.tooltip("execute_button"):
                dpg.add_text("F5")
            dpg.add_button(
                label="CLEAR",
                width=290,
                height=30,
                callback=lambda: dpg.set_value("code", ""),
                pos=(302, 261),
            )

        with dpg.window(modal=True, show=False, tag="popup", label="", pos=(225, 100)):
            dpg.add_text(tag="popup_text")

    # Drag and drop
    dpg_dnd.initialize()

    def drop(data, keys):
        dpg.set_value("code", "")
        with open(data[0], "r") as f:
            dpg.set_value("code", f"{f.read()}")

    dpg_dnd.set_drop(drop)

    # Setup
    dpg.set_primary_window(window, True)
    dpg.configure_item(window, no_title_bar=False, no_collapse=False)

    dpg.setup_dearpygui()
    dpg.show_viewport()

    class MARGINS(ctypes.Structure):
        _fields_ = [
            ("cxLeftWidth", c_int),
            ("cxRightWidth", c_int),
            ("cyTopHeight", c_int),
            ("cyBottomHeight", c_int),
        ]

    dwm = ctypes.windll.dwmapi
    hwnd = win32gui.FindWindow(None, "Viewport Title")
    margins = MARGINS(-1, -1, -1, -1)
    dwm.DwmExtendFrameIntoClientArea(hwnd, margins)

    dpg.start_dearpygui()
    dpg.destroy_context()


class growtopia:
    file_name = "Growtopia.exe"
    window_name = "Growtopia"

    path = os.path.join(os.path.expanduser("~"), "AppData", "Local", "Growtopia")
    exe_path = os.path.join(path, "Growtopia.exe")
    save_path = os.path.join(path, "save.dat")

    def get_game_detail():
        Result = {
            "Online_User": "",
            "WOTDLink": "",
            "WOTDName": "",
            "GTTime": "",
            "GTDate": "",
        }

        response = requests.get("https://www.growtopiagame.com/detail").json()

        Result["Online_User"] = response["online_user"]
        Result["WOTDLink"] = response["world_day_images"]["full_size"]
        Result["WOTDName"] = (
            Result["WOTDLink"]
            .replace("https://www.growtopiagame.com/worlds/", "")
            .replace(".png", "")
        ).upper()
        Result["GTTime"] = (
            datetime.datetime.now(timezone("UTC"))
            .astimezone(timezone("America/New_York"))
            .strftime("%X")
        )
        Result["GTDate"] = (
            datetime.datetime.now(timezone("UTC"))
            .astimezone(timezone("America/New_York"))
            .strftime("%x")
        )
        return Result

    def get_server_data(version, protocol=None):
        if not protocol:
            protocol = 205

        data = f"version=v{version}&platform=0&protocol={protocol}".encode()
        headers = {"User-Agent": "UbiServices_SDK_2022.Release.9_PC32_ansi_static"}

        response = requests.post(
            url="https://www.growtopia2.com/growtopia/server_data.php",
            headers=headers,
            data=data,
        )

        try:
            server_data_lines = response.text.splitlines()
            server_data = {}
            for line in server_data_lines:
                parts = line.split("|")
                if len(parts) >= 2:
                    key, value = parts[0], parts[1]
                    server_data[key] = value

            return server_data
        except:
            return response, response.text

    def get_game_info():
        return app("com.rtsoft.growtopia", lang="en", country="us")

    def download_image(url):
        os.makedirs("assets\\gt", exist_ok=True)

        url_segments = url.split("/")
        image_name = url_segments[-1]
        image_name = unquote(image_name)

        if not os.path.exists(f"assets\\gt\\{image_name}"):
            response = requests.get(url)
            if response.status_code == 200:
                with open(os.path.join("assets\\gt", image_name), "wb") as f:
                    f.write(response.content)

            return response
        else:
            return f"found image '{image_name}'"

    def get_save():
        def get_data(name):
            try:
                c = content.split(name)
                if len(c) > 1:
                    length = ord(c[1][0])
                    return "".join(c[1][4 + x] for x in range(length))
                else:
                    return
            except:
                return

        attr = ["tankid_name", "tankid_password", "lastworld"]

        with io.open(growtopia.save_path) as file:
            content = file.read()

        if content:
            content = content.replace("tankid_password_chk2", "")

            grow_id = get_data(content, attr[0])
            encoded_password = get_data(content, attr[1])
            last_world = get_data(content, attr[2])
            return grow_id, encoded_password, last_world

    def connect():
        if is_process_running("Growtopia.exe") is False:
            Application().start(growtopia.exe_path)

        app = Application().connect(path=growtopia.exe_path, title="Growtopia")
        return app.window(title="Growtopia")

    def send_key(app, key):
        return app.send_keystrokes(key)

    def screenshot():
        object = Screenshot("Growtopia")
        screenshot = object.screenshot()
        image = Image.fromarray(screenshot)
        image.save("gt_image.png")
        return image

    def image_to_text():
        strings = pytesseract.image_to_string("gt_image.png")
        search_text = "Activate Windows\nGo to Settings to activate Windows."
        return strings.replace(search_text, "").strip()

    def login():
        terminate_process("Growtopia.exe")
        app = growtopia.connect()
        growtopia.send_key(app, "{ENTER}")
        growtopia.send_key(app, "{ENTER}")
        return app


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def set_title(title):
    if os.name == "nt":
        import ctypes

        ctypes.windll.kernel32.SetConsoleTitleW(title)
    else:
        import sys

        sys.stdout.write(f"\033]0;{title}\007")
        sys.stdout.flush()


def get_mac_addresses():
    mac_addresses = {}
    for interface_name, addrs in psutil.net_if_addrs().items():
        if interface_name == "Wi-Fi" or interface_name == "Ethernet":
            for addr in addrs:
                if addr.family == psutil.AF_LINK:
                    mac_addresses[interface_name] = addr.address

    return mac_addresses


def is_process_running(process_name):
    for process in psutil.process_iter(["pid", "name"]):
        if process.info["name"] == process_name:
            return True
    return False


def run_process(path):
    try:
        return subprocess.Popen(path)
    except Exception as e:
        return e


def terminate_process(process_name):
    for process in psutil.process_iter(attrs=["pid", "name"]):
        if process.info["name"] == process_name:
            pid = process.info["pid"]
            try:
                p = psutil.Process(pid)
                p.terminate()
            except psutil.NoSuchProcess:
                pass


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def get_pid_by_process_name(process_name):
    for process in psutil.process_iter(["pid", "name"]):
        if process.info["name"] == process_name:
            return process.info["pid"]
    return


def screenshot(file_name, region=None):
    if region:
        left, top, width, height = region
        screenshot = pyautogui.screenshot(file_name, region=(left, top, width, height))
    else:
        screenshot = pyautogui.screenshot(file_name)

    screenshot.save(file_name)
    return screenshot


def image_to_text(image):
    pytesseract.pytesseract.tesseract_cmd = "Tesseract-OCR\\tesseract.exe"
    return pytesseract.image_to_string(Image.open(image))


def get_window_pos(window):
    window_handle = win32gui.FindWindow(None, window)

    rect = win32gui.GetWindowRect(window_handle)
    left, top, width, height = rect
    return left, top, width, height


def activate_window(window):
    active = win_activate(window_title=window, partial_match=False)
    return active


class tor:
    def configure():
        try:
            path = "tor\\torrc"
            ports = range(9000, 10000)

            with open(path, "w") as torrc_file:
                for port in ports:
                    line = f"SocksPort {port}\n"
                    torrc_file.write(line)
            return True
        except Exception as e:
            return e

    def start():
        if os.path.exists("tor\\torrc"):
            os.system("start tor\\tor.exe -f tor\\torrc")
        else:
            os.system("start tor\\tor.exe")

    def stop():
        os.system("taskkill /F /IM tor.exe")

    def enable_system_wide(port):
        os.system('reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings" /v ProxyEnable /t REG_DWORD /d 1 /f')
        os.system(f'reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings" /v ProxyServer /t REG_SZ /d "socks=127.0.0.1:{port}" /f')
        os.system('reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings" /v ProxyOverride /t REG_SZ /d "<local>" /f')

    def disable_system_wide():
        os.system('reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings" /v ProxyEnable /t REG_DWORD /d 0 /f')


class discord:
    def send_message_webhook(url, content, username=None, proxy=None):
        webhook = DiscordWebhook(
            url=url,
            content=content,
            username=username,
            proxy=proxy,
            rate_limit_retry=True,
        )
        response = webhook.execute()
        return response

    def send_message_client(token, channel_id, message, proxy=None):
        payload = {"content": message}

        headers = {
            "Authorization": token,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
        }

        url = f"https://discord.com/api/v9/channels/{channel_id}/messages"

        response = requests.post(url, data=payload, headers=headers, proxy=proxy)
        return response


class back_gui:
    def connect(file_name, file_path, window_name):
        if is_process_running(file_name) is False:
            Application().start(file_path)

        app = Application().connect(path=growtopia.exe_path, title=window_name)
        return app.window(title=window_name)

    def send_key(app, key):
        return app.send_keystrokes(key)


class gui:
    class mouse:
        def get_pos():
            return pyautogui.position()

        def set_pos(x=None, y=None):
            return pyautogui.moveTo(x=x, y=y)

        def move(x=None, y=None):
            return pyautogui.move(x=x, y=y)

        def drag(x=None, y=None, button=None):
            # Drag mouse to x,y while holding down mouse button
            return pyautogui.dragTo(x=x, y=y, button=button)

        def click(x=None, y=None, button=None, clicks=None, interval=None):
            # button = mouse button to click
            # clicks = number of left mouse button clicks
            # interval = standby time
            return pyautogui.click(
                x=x, y=y, button=button, clicks=clicks, interval=interval
            )

        def set_down(x=None, y=None, button=None):
            return pyautogui.mouseDown(x=x, y=y, button=button)

        def set_up(x=None, y=None, button=None):
            return pyautogui.mouseUp(x=x, y=y, button=button)

        def scroll(num_clicks, x=None, y=None, vertical=False):
            # up = +(x,y)
            # down = -(x,y)
            if vertical is True:
                return pyautogui.vscroll(num_clicks, x=x, y=y)
            else:
                return pyautogui.scroll(num_clicks, x=x, y=y)

    class keyboard:
        def write(text):
            return pyautogui.write(text)

        def press(key, presses=1):
            return pyautogui.press(key, presses=presses)

        def key_up(key):
            return pyautogui.keyUp(key)

        def key_down(key):
            return pyautogui.keyDown(key)

        def hotkey(*keys):
            return pyautogui.hotkey(*keys)

    class msgbox:
        def alert(text=None, title=None, button=None):
            return pyautogui.alert(text=text, title=title, button=button)

        def confirm(text=None, title=None, *buttons):
            return pyautogui.confirm(text=text, title=title, buttons=buttons)

        def prompt(text=None, title=None, default=None):
            return pyautogui.prompt(text=text, title=title, default=default)

        def password(text=None, title=None, default=None):
            return pyautogui.password(text=text, title=title, default=default, mask="*")

    class locate_image:
        # grayscale=True speeds up locate functions by 30%, but can cause false matches
        def on_screen(image, confidence=None, region=None, grayscale=False):
            return pyautogui.locateOnScreen(
                image=image,
                confidence=confidence,
                region=region,
                grayscale=grayscale,
            )

        def on_all_screen(image, confidence=None, region=None, grayscale=False):
            return pyautogui.locateAllOnScreen(
                image=image,
                confidence=confidence,
                region=region,
                grayscale=grayscale,
            )

        def center_on_screen(image, confidence=None, region=None, grayscale=False):
            return pyautogui.locateCenterOnScreen(
                image=image,
                confidence=confidence,
                region=region,
                grayscale=grayscale,
            )


if __name__ == "__main__":
    main()
