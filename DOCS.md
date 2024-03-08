# GUI
  ### GUI.Mouse
  Get position
  ```python
  x, y = gui.mouse.get_pos()
  ```

  Set position
  ```python
  gui.mouse.set_pos(x=None, y=None)
  ```
    
  Move
  ```python
  gui.mouse.move(x=None, y=None)
  ```

  Drag
  ```python
  # Drag mouse to x,y while holding down mouse button
  gui.mouse.drag(x=None, y=None, button=None)
  ```

  Click
  ```python
  # button = mouse button to click
  # clicks = number of left mouse button clicks
  # interval = standby time
  gui.mouse.click(x=None, y=None, button=None, clicks=None, interval=None)
  ```

  Set down/up
  ```python
  gui.mouse.set_down(x=None, y=None, button=None)
  set_up(x=None, y=None, button=None)
  ```

  Scroll
  ```python
  gui.mouse.scroll(num_clicks=1, x=None, y=None, vertical=False)
  ```

  ### GUI.Keyboard
  Write
  ```python
  gui.keyboard.write(text)
  ```
    
  Press
  ```python
  gui.keyboard.press(key, presses=1)
  ```

  Key up/down
  ```python
  gui.keyboard.key_up(key)
  gui.keyboard.key_down(key)
  ```

  Hotkey
  ```python
  gui.keyboard.hotkey(*keys)
  ```

  ### GUI.MsgBox
  Alert
  ```python
  gui.msgbox.alert(text=None, title=None, button=None)
  ```

  Confirm
  ```python
  gui.msgbox.confirm(text=None, title=None, *buttons)
  ```

  Prompt
  ```python
  gui.msgbox.prompt(text=None, title=None, default=None)
  ```

  Password
  ```python
  gui.msgbox.password(text=None, title=None, default=None)
  ```

  ### GUI.LocateImage
  On screen
  ```python
  # grayscale=True speeds up locate functions by 30%, but can cause false matches
  gui.locate_image.on_screen(image, confidence=None, region=None, grayscale=False)
  ```

  On all screens
  ```python
  gui.locate_image.on_all_screen(image, confidence=None, region=None, grayscale=False)
  ```

  Center on screen
  ```python
  gui.locate_image.center_on_screen(image, confidence=None, region=None, grayscale=False)
  ```


# BackGUI
  Connect
  ```python
  app = connect(file_name, file_path, window_name)
  ```

  Send key
  ```python
  send_key(app, key)
  ```


# Proxy
  ### Tor
  Configure/start/stop
  ```python 
  tor.configure()
  tor.start()
  tor.stop()
  ```

  ### Set proxies
  ```python
  # Tor
  tor_proxies = {
    'http': 'socks5://127.0.0.1:9050',
    'https': 'socks5://127.0.0.1:9050'
  }
    
  # SOCKS5
  socks_proxies = {
    'http': 'socks5://proxy_url:port',
    'https': 'socks5://proxy_url:port'
  }

  # HTTP(S)
  http_proxies = {
    'https': 'https://proxy_url:port',
    'http': 'http://proxy_url:port'
  }
  ```


# Discord
  Send message to webhook
  ```python
  discord.send_message_webhook(url, content, username=None, proxy=None)
  ```

  Send message to channel using user token
  ```python
  send_message_client(token, channel_id, message, proxy=None)
  ```


# General
  Get mac addresses
  ```python
  mac_addresses = get_mac_addresses()

  wifi_mac =  mac_addresses["Wi-Fi"]
  ethernet_mac = mac_addresses["Ethernet"]
  ```

  Is process running
  ```py
  running = is_process_running(process_name)
  ```

  Run process
  ```python
  run_process(path)
  ```

  Terminate process
  ```python
  terminate_process(process_name)
  ```

  Is running as admin
  ```python
  admin = is_admin()
  ```

  Get PID by process name
  ```python
  pid = get_pid_by_process_name(process_name)
  ```

  Screenshot
  ```python
  screenshot(file_name, region=None)
  ```

  Image to text
  ```python
  text = image_to_text(image)
  ```

  Get a windows position
  ```python
  get_window_pos(window)
  ```

  Activate window
  ```python
  activate_window(window)
  ```
