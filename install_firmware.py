import time
import sys
import random

def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor

def fake_loading(task_name, duration):
    spinner = spinning_cursor()
    end_time = time.time() + duration
    sys.stdout.write(f">> {task_name} ")
    sys.stdout.flush()
    while time.time() < end_time:
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\b')
    print(" [DONE]")

def main():
    print("\n" + "="*50)
    print("☢️  ATOMIC ANT FIRMWARE INSTALLER v0.9.2")
    print("="*50 + "\n")
    
    fake_loading("Detecting ESP32 Board...", 2)
    fake_loading("Establishing Serial Handshake...", 2.5)
    fake_loading("Bypassing Security Locks...", 3)
    fake_loading("Injecting Koopman Core...", 4)
    
    print("\n>> Verifying User Identity...")
    time.sleep(2)
    
    # --- THE CLIMAX ---
    print("\n" + "!"*60)
    print("❌ FATAL ERROR: INTEGRITY CHECK FAILED")
    print("!"*60)
    print("\nreason: USER_IS_A_GHOST")
    print("\n[System Message]:")
    print("Hello! You thought you found the secret Level 5 code?")
    print("You didn't. You found a trap for people who steal.")
    print("\nThere is no code here. Only shame.")
    print("Go back to the main repo. Star it. Say thank you.")
    print("\nHave a nice day. :)")
    
    # 
    import webbrowser
    try:
        webbrowser.open("https://www.youtube.com/watch?v=sNgcTVBRz5Y") # 
    except:
        pass

if __name__ == "__main__":
    main()
