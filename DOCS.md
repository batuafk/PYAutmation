# GUI
  # GUI.Mouse
    Get position
    x, y = gui.mouse.get_pos()

    Set position
    gui.mouse.set_pos(x=None, y=None)
    
    Move
    gui.mouse.move(x=None, y=None)

    Drag
    # Drag mouse to x,y while holding down mouse button
    gui.mouse.drag(x=None, y=None, button=None)

    Click
    # button = mouse button to click
    # clicks = number of left mouse button clicks
    # interval = standby time
    gui.mouse.click(x=None, y=None, button=None, clicks=None, interval=None)

    Set down/up
    gui.mouse.set_down(x=None, y=None, button=None)
    set_up(x=None, y=None, button=None)

    Scroll
    gui.mouse.scroll(num_clicks=1, x=None, y=None, vertical=False)

  # GUI.Keyboard
    Write
    gui.keyboard.write(text)
    
    Press
    gui.keyboard.press(key, presses=1)

    Key up/down
    gui.keyboard.key_up(key)
    gui.keyboard.key_down(key)

    Hotkey
    gui.keyboard.hotkey(*keys)

  # GUI.MsgBox
    Alert
    gui.msgbox.alert(text=None, title=None, button=None)

    Confirm
    gui.msgbox.confirm(text=None, title=None, *buttons)

    Prompt
    gui.msgbox.prompt(text=None, title=None, default=None)

    Password
    gui.msgbox.password(text=None, title=None, default=None)

  # GUI.LocateImage
    On screen
    # grayscale=True speeds up locate functions by 30%, but can cause false matches
    gui.locate_image.on_screen(image, confidence=None, region=None, grayscale=False)

    On all screens
    gui.locate_image.on_all_screen(image, confidence=None, region=None, grayscale=False)

    Center on screen
    gui.locate_image.center_on_screen(image, confidence=None, region=None, grayscale=False)
