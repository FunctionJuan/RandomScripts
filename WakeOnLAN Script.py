from wakeonlan import send_magic_packet

def wakeup(mac, selection):
    """Processes the input of selected option."""
    print(f"\n✅ Sending selection '{selection}' to processor.")
    # Sending Packet
    send_magic_packet(mac)
    return f"Sent Packet to chosen PC"

def exit_program(selection):
    """Handles the exit option."""
    print(f"\n👋 Exiting program as requested by selection '{selection}'.")
    return "Program terminated successfully."


def get_user_choice_():
    """
    Presents the user with four options and uses a nested ternary operator 
    to call the correct function or handle the exit.
    """
    print("--- Wake Up A Computer  ---")
    print("Please select one of the computers to wake up:")
    print("1: Option for (PC Livingroom)")
    print("2: Option for (PC Office)")
    print("3: Option for (PC Garage)")
    print("4: Exit Program")
    
    # Get user input and strip whitespace
    choice = input("Enter your choice (1, 2, 3, or 4): ").strip()

    # Input validation (simple check for four options)
    if choice not in ('1', '2', '3', '4'):
        print("\n❌ Invalid choice. Please enter 1, 2, 3, or 4.")
        return # Exit the function if input is invalid
    
    # --- The Core Nested Ternary Operator Logic ---
    # We now nest three conditional expressions to check for choices '1', '2', '3',
    # with the final 'else' implicitly handling '4' (Exit).
    
    result = (
        wakeup('00:00:00:00:00:00', choice) if choice == '1' else 
        wakeup('00:00:00:00:00:00', choice) if choice == '2' else 
        wakeup('00:00:00:00:00:00', choice) if choice == '3' else
        exit_program(choice) # Handles choice '4'
    )
    
    # Print the result returned by the called function
    print("\n--- Processing Complete ---")
    print(f"Final output: {result}")
    print("---------------------------\n")

# Run the program
if __name__ == "__main__":
    get_user_choice_()