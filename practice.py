import sys , time

massage = 'i love you'
len_massage = len(massage)
for i in range(len_massage):
    sys.stdout.write(f"\r{i:2}")
    sys.stdout.flush()
    time.sleep(0.1)
   



#function to change case sensitive
def changing(text):
    len_t = len(text)
    for i in range(10):
        for x in range(len_t):
            char = text[x]
            #print(char)
            if char.islower():
                new_char = char.upper()
            else:
                new_char = char.lower()
            new_text = text[:x] + new_char + text[x+1:]
            sys.stdout.write(f'\r{new_text}')
            sys.stdout.flush()
            time.sleep(0.1)
    time.sleep(0.2)
changing("starting metasploit framework")


'''
while True:
    sys.stdout.write(f"\r[0:]")
    sys.stdout.flush()
    time.sleep(0.1)

'''





