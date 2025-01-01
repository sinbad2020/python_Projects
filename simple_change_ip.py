import os
import random
interface = "Wi-Fi"  #"Ethernet"
print("""▀▄▀▄▀▄   🎀  ❝𝓉𝒽𝒾𝓈 𝓅𝓇❁𝑔𝓇𝒶𝓂 𝒻💍𝓇 𝓌𝒾𝓃𝒹🍬𝓌𝓈 ❀𝓃𝓁𝓎❞  🎀   ▄▀▄▀▄▀
░"░t░h░i░s░ ░p░r░o░g░r░a░m░ ░f░o░r░ ░w░i░n░d░o░w░s░ ░o░n░l░y░"░\n""")

#function to return input
def userInput():
    while True:
        try:
            num_router = int(input("Complete the IP router: 192.168.__.1: "))
            if 0 < num_router < 255:
                return num_router
            else:
                print("Please inter number between 0 and 255")
        except ValueError:
            print("Invalid input. Please enter a valid number.")         
            
     
#function to return random number from(30, 150)
def randomNumber():
    return random.randint(30, 150)

#function to execute commnad with given variables
def starting(router , r_ip):
    command = os.system(f"netsh interface ipv4 set address wi-fi static 192.168.{router}.{r_ip} 255.255.255.0 192.168.{router}.1")
    #checking command output
    if command == 0 :
        print(f"the new ip is: 192.168.{router}.{r_ip}")
    else:
         print("An error occurred while executing the command. Please check your input and try again.")
def main():
    router = userInput()
    r_ip = randomNumber()
    starting(router , r_ip)
#for starting when excute the program directly not when you import it    
if __name__ == "__main__":
    main()

    
