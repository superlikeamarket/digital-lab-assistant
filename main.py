from lab_assistant.menu import show_menu
from lab_assistant.dilution import run_dilution_cli
from lab_assistant.media_prep import run_media_prep_cli
from lab_assistant.cfu import run_cfu_cli
from lab_assistant.timer import run_timer_cli


def main():
    while True:
        choice = show_menu()

        if choice == "1":
            run_dilution_cli()
        elif choice == "2":
            run_media_prep_cli()
        elif choice == "3":
            run_cfu_cli()
        elif choice == "4":
            run_timer_cli()
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()