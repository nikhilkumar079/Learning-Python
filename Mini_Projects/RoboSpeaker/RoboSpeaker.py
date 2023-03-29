import os

if __name__ == '__main__':
  
    print('Welcome to RoboSpeaker. Created by Nikhil')
    while True:
        x = input('Enter the Text: ')
        if x == 'q':
            os.system("say 'bye bye'")
            break
        command = f"say {x}"
        os.system(command)
