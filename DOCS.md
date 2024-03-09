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
  x, y = gui.locate_image.on_screen(image, confidence=None, region=None, grayscale=False)
  ```

  On all screens
  ```python
  gui.locate_image.on_all_screen(image, confidence=None, region=None, grayscale=False)
  ```

  Center on screen
  ```python
  x, y = gui.locate_image.center_on_screen(image, confidence=None, region=None, grayscale=False)
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
  Add 9000-9999 ports
  ```python
  tor.configure()
  ```

  start/stop
  ```python
  tor.start()
  tor.stop()
  ```

  Use Tor as system-wide proxy
  
  If Tor is configured, you can use ports 9000-9999
  ```python
  tor.enable_system_wide(port)
  tor.disable_system_wide()
  ```

  Use tor proxies not system-wide
  ```py
  socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9050)
  socket.socket = socks.socksocket

  response = requests.get("https://api.ipify.org")
  print(response.text)
  ```

  Set proxies
  ```python
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
  discord.send_message_client(token, channel_id, message, proxy=None)
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

# Growtopia
  ``growtopia.path`` ``growtopia.exe_path`` ``growtopia.save_path`` ``growtopia.file_name`` ``growtopia.window_name``
  
  Get game detail
  ```python
  game_detail = growtopia.get_game_detail()

  online_users = game_detail['Online_User']
  gt_date = game_detail['GTDate']
  gt_time = game_detail['GTTime']
  ```

  Get server data
  ```python
  server_data = growtopia.get_server_data(version=version, protocol=205)

  server = server_data["server"]
  port = int(server_data["port"])
  type = int(server_data["type"])

  maint = server_data["#maint"]

  beta_server = server_data["beta_server"]
  beta_port = int(server_data["beta_port"])
  beta_type = server_data["beta_type"]

  beta2_server = server_data["beta2_server"]
  beta2_port = int(server_data["beta2_port"])
  beta2_type = server_data["beta2_type"]

  beta3_server = server_data["beta3_server"]
  beta3_port = int(server_data["beta3_port"])
  beta3_type = server_data["beta3_type"]

  type2 = int(server_data["type2"])
  meta = server_data["meta"]
  ```

  Get game information
  ```python
  game_info = growtopia.get_game_info()

  game_version = float(game_info['version'])
  game_installs = game_info['realInstalls']
  ```

  Get GrowID, encrypted password, last world
  ```python
  usr, pass, world = growtopia.get_save()
  ```

  Connect
  ```python
  app = growtopia.connect()
  ```

  Send key
  ```python
  growtopia.send_key(app, key)
  ```

  Screenshot
  ```python
  growtopia.screenshot()
  ```

  Image to text
  ```python
  text = growtopia.image_to_text()
  ```

  Login
  ```python
  app = growtopia.login()
  ```


  
