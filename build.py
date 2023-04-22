import os

from common.config import VERSION, AUTHOR

app_name = 'MyApp'
build_command = "nuitka --standalone --mingw64 --plugin-enable=pyqt5 "
build_command += "--windows-disable-console "
build_command += "--windows-icon-from-ico=resource/images/logo.png --output-dir=out "
build_command += f"--windows-company-name={AUTHOR}  --windows-product-name={app_name} "
build_command += f"--windows-product-version={VERSION} "
build_command += "--nofollow-import-to=tkinter --follow-import-to=common,components,view entry.py"
# ========
os.system("python -m PyQt5.pyrcc_main resource/resource.qrc -o resource_rc.py")  # 编译资源文件
os.system("python -m PyQt5.uic.pyuic view/login_window.ui -o view/ui_login_window.py")  # 编译ui文件
os.system("python -m PyQt5.uic.pyuic view/main_window.ui -o view/ui_main_window.py")  # 编译ui文件
print(build_command)
os.system(build_command)  # 打包
