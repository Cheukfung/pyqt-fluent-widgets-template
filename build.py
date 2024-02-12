import os

from common.config import VERSION, AUTHOR

app_name = 'MyApp'
build_command = "nuitka --standalone --mingw64 --enable-plugin=pyside6 "
build_command += "--windows-disable-console "
build_command += "--windows-icon-from-ico=resource/images/logo.png --output-dir=out "
build_command += f"--windows-company-name={AUTHOR}  --windows-product-name={app_name} "
build_command += f"--windows-product-version={VERSION} "
build_command += "--follow-import-to=common,components,view entry.py"
# ========
# 运行pack_resources.py
# ========
os.system("python pack_resources.py")
print(build_command)
os.system(build_command)  # 打包
