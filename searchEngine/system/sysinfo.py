import platform

def get_os_hardware_information():
    print("HARDWARE:")
    print("")
    print('uname:', platform.uname())
    print('system   :', platform.system())
    print('node     :', platform.node())
    print('release  :', platform.release())
    print('version  :', platform.version())
    print('machine  :', platform.machine())
    print('processor:', platform.processor())
    print('interpreter:', platform.architecture())
    print("")
    hardware_dict={}
    hardware_dict["uname"]=platform.uname()
    hardware_dict["system"] = platform.system()
    hardware_dict["node"] = platform.node()
    hardware_dict["release"] = platform.release()
    hardware_dict["version"] = platform.version()
    hardware_dict["machine"] = platform.machine()
    hardware_dict["processor"] = platform.processor()
    hardware_dict["interpreter"] = platform.architecture()
    return hardware_dict

def get_interpreter_information():
    print("PYTHON:")
    print("")
    print('Version      :', platform.python_version())
    print('Version tuple:', platform.python_version_tuple())
    print('Compiler     :', platform.python_compiler())
    print('Build        :', platform.python_build())
    print("")
    interpretor_dict={}
    interpretor_dict["Version"]= platform.python_version()
    interpretor_dict["Version tuple"] = platform.python_version_tuple()
    interpretor_dict["Compiler"] = platform.python_compiler()
    interpretor_dict["Build"] = platform.python_build()
    return interpretor_dict

def get_platform_information():
    print("OS PLATFORM:")
    print("")
    print('Platform :', platform.platform())
    print("")
    platform_dict={}
    platform_dict["Platform"]= platform.platform()
    return platform_dict