import sys , time

def points(massage):
    sys.stdout.write(massage)
    for x in range(15):
        
        sys.stdout.write(".") 
          
        sys.stdout.flush()
        time.sleep(0.3)

def counter(m):
    sys.stdout.write('\n')
    for y in range(10):
        sys.stdout.write(f"\r{y}")
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write(m)     
points("Waiting ")
points("\nAlmost Finishing ")
counter("\nDone")