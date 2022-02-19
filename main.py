from MenuUI.LoginAndRegisterUI import login_register_ui

# from com.qa.system.Menu import *

# menu_service()
if login_register_ui():
    print("Access allowed")
    from MenuUI.MenuSelectionUI.MenuSelectionWindow import menu_select_option_window
else:
    print("No access allowed")

