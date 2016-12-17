import platform
import os
if platform.architecture()[0] == '32bit':
    os.environ["PYSDL2_DLL_PATH"] = "./DLL/x86"
else:
    os.environ["PYSDL2_DLL_PATH"] = "./DLL/x64"


import game_framework
import Logo.Logo


game_framework.run(Logo.Logo)


