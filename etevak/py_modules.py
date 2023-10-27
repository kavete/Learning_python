import platform

my_system = platform.system()

print(my_system)

print(platform.processor())

print(platform.architecture())

print(platform.python_compiler())

print(platform.freedesktop_os_release())

print(platform.java_ver())

print(platform.machine())

print(platform.python_revision())


function_names = dir(platform)

print(function_names)
