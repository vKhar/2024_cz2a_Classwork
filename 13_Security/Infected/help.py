import os
for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.py'):
                  f = open(os.path.join(root, file))
                  contents = f.read()
                  if 'key logger installed!' in contents:
                        print(os.path.join(root, file))