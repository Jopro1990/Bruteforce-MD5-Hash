import time
import itertools
import string
import hashlib
import sys
import signal
import threading

# ANSI escape codes for colors
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
RESET = "\033[0m"

done = False

def signal_handler(signal, frame):
    print(f'{YELLOW}You pressed Ctrl+C!{RESET}')
    global done
    done = True
    sys.exit(0)

def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write(f'\r{YELLOW}loading{RESET} {c}')
        sys.stdout.flush()
        time.sleep(0.1)

def display_menu():
    print(f"\n{MAGENTA}=== Menu ==={RESET}")
    print(f"{CYAN}1.{RESET} Run MD5 Brute-force")
    print(f"{CYAN}2.{RESET} Exit")

def get_menu_choice():
    while True:
        choice = input(f"{YELLOW}Select an option (1-2): {RESET}")
        if choice.isdigit() and 1 <= int(choice) <= 2:
            return int(choice)
        else:
            print(f"{YELLOW}Invalid choice. Please enter a number between 1 and 2.{RESET}")

def main():
    print(f"{GREEN}Welcome to MD5 Brute-force Tool!{RESET}")
    while True:
        display_menu()
        option = get_menu_choice()

        if option == 1:
            print("\nEnter the MD5 hash:")
            inp_usr = input(f"{YELLOW}> {RESET}")
            chrs = string.printable.replace(' \t\n\r\x0b\x0c', '')
            print(f"{CYAN}Characters to be used:{RESET} {chrs}")
            signal.signal(signal.SIGINT, signal_handler)
            _attack(chrs, inp_usr)
        elif option == 2:
            print(f"\n{YELLOW}Exiting. Thank you!{RESET}")
            sys.exit(0)

def _attack(chrs, inputt):
        print(f"\n{GREEN}[+] Start Time:{RESET} {time.strftime('%H:%M:%S')}")
        start_time = time.time()
        t = threading.Thread(target=animate)
        t.start()
        total_pass_try = 0

        for n in range(1, 31 + 1):
            character_start_time = time.time()
            print(f"\n{YELLOW}[!]{RESET} I'm at {n}-characters")

            for xs in itertools.product(chrs, repeat=n):
                saved = ''.join(xs)
                stringg = saved
                m = hashlib.md5()
                m.update(saved.encode('utf-8'))
                total_pass_try += 1

                if m.hexdigest() == inputt:
                    time.sleep(1)
                    global done
                    done = True

                    print(f"\n{YELLOW}[!]{RESET} Found: {stringg}")
                    print(f"{YELLOW}[-]{RESET} End Time: {time.strftime('%H:%M:%S')}")
                    print(f"{YELLOW}[-]{RESET} Total Keyword Attempted: {total_pass_try}")
                    print(f"\n{GREEN}---Md5 cracked at {time.time() - start_time} seconds ---{RESET}")
                    input(f"{YELLOW}Press Enter to exit.{RESET}")
                    sys.exit("Thank You !")

            print(f"{YELLOW}[!]{RESET} {n}-character finished in {time.time() - character_start_time} seconds ---")

if __name__ == "__main__":
    main()
