import platform
import psutil
import os
import sys

def clean_screen():
    if psutil.POSIX:
        os.system('clear')
    else:
        os.system('cls')

def secs2hours(secs):
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
    return "%d:%02d:%02d" % (hh, mm, ss)

def cpustats():
    clean_screen()
    print("-------- PLATFORM INFORMATION --------")
    print("OS: ",platform.platform())
    print("Version: ",platform.version())
    print("Processor: ",platform.processor())
    print("-------- CPU INFORMATION ---------")
    print("CPU Count: ", psutil.cpu_count())
    total = psutil.cpu_count()
    cpus_percent = psutil.cpu_percent(percpu=True)
    for i in range(total):
        print("CPU %-6i" % i, end="")
    print()
    for percent in cpus_percent:
        print("%-10s" % percent, end="")
    print()
    print("------- BATTERY INFORMATION -------")
    batt = psutil.sensors_battery()
    if batt is None:
        return sys.exit("no battery is installed")

    print("charge:     %s%%" % round(batt.percent, 2))
    if batt.power_plugged:
        print("status:     %s" % (
            "charging" if batt.percent < 100 else "fully charged"))
        print("plugged in: yes")
    else:
        print("left:       %s" % secs2hours(batt.secsleft))
        print("status:     %s" % "discharging")
        print("plugged in: no")

    print("--------- MEMORY INFORMATION (in MB)--------")
    virt = psutil.virtual_memory()
    templ = "%10s %10s %10s %10s %10s %10s"
    print(templ % ('total', 'used', 'free', 'shared', 'buffers', 'cache'))
    print(templ % (
        int(virt.total / 1024),
        int(virt.used / 1024),
        int(virt.free / 1024),
        int(getattr(virt, 'shared', 0) / 1024),
        int(getattr(virt, 'buffers', 0) / 1024),
        int(getattr(virt, 'cached', 0) / 1024)))
    print()
    print("percent: ",virt.percent,"%")

cpustats()

