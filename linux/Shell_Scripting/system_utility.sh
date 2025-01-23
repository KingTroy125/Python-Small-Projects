#!/bin/bash

# Function to display a menu
show_menu() {
    echo "============================="
    echo "  Shell Scripting Utility"
    echo "============================="
    echo "1. Backup Files"
    echo "2. Update System"
    echo "3. Backup and Update"
    echo "4. Exit"
    echo -n "Choose an option [1-4]: "
}

# Function to perform a backup
backup_files() {
    echo "Starting backup..."
    BACKUP_DIR="$HOME/backup_$(date +%Y%m%d_%H%M%S)"
    mkdir -p "$BACKUP_DIR"
    cp -r $HOME/Documents $HOME/Pictures $HOME/Videos "$BACKUP_DIR"
    echo "Backup completed. Files saved to $BACKUP_DIR"
}

# Function to update the system
update_system() {
    echo "Updating system..."
    sudo apt update && sudo apt upgrade -y
    echo "System update completed."
}

# Main program loop
while true; do
    show_menu
    read -r choice
    case $choice in
        1)
            backup_files
            ;;
        2)
            update_system
            ;;
        3)
            backup_files
            update_system
            ;;
        4)
            echo "Exiting. Goodbye!"
            break
            ;;
        *)
            echo "Invalid choice, please try again."
            ;;
    esac
done