import os

files = os.listdir('Mini Projects/ClutteredFolder')
i = 1
for file in files:
    # print(file)
    if file.endswith('.png'):
        os.rename(f'Mini Projects/ClutteredFolder/{file}', f'Mini Projects/ClutteredFolder/{i}.png')
        i = i + 1
