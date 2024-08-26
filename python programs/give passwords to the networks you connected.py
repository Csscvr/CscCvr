import subprocess

def get_all_networks():
    # Get the list of all Wi-Fi networks you have ever connected to
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
    all_networks = [i.split(":")[1].strip() for i in data if "All User Profile" in i]
    return all_networks

def get_network_info(network_name):
    # Get the password and other info of the selected network
    try:
        data = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', network_name, 'key=clear']).decode('utf-8').split('\n')
        password = [i.split(":")[1].strip() for i in data if "Key Content" in i]
        ssid = [i.split(":")[1].strip() for i in data if "SSID name" in i]
        auth = [i.split(":")[1].strip() for i in data if "Authentication" in i]
        cipher = [i.split(":")[1].strip() for i in data if "Cipher" in i]
        connection_type = [i.split(":")[1].strip() for i in data if "Connection type" in i]
        radio_type = [i.split(":")[1].strip() for i in data if "Radio type" in i]
        channel = [i.split(":")[1].strip() for i in data if "Channel" in i]
        signal = [i.split(":")[1].strip() for i in data if "Signal" in i]
        return ssid[0], auth[0], cipher[0], password[0], connection_type[0], radio_type[0], channel[0], signal[0]
    except IndexError:
        return "Cannot read password!", "Cannot read auth!", "Cannot read cipher!", "Cannot read password!", "Cannot read connection type!", "Cannot read radio type!", "Cannot read channel!", "Cannot read signal!"

def main():
    all_networks = get_all_networks()
    print("All Wi-Fi Networks You Have Ever Connected To:")
    for i, network in enumerate(all_networks):
        print(f"{i+1}. {network}")

    while True:
        try:
            choice = int(input("Enter the number of the network to view its password and info: "))
            if 1 <= choice <= len(all_networks):
                network_name = all_networks[choice-1]
                ssid, auth, cipher, password, connection_type, radio_type, channel, signal = get_network_info(network_name)
                print(f"Network Name (SSID): {ssid}")
                print(f"Authentication: {auth}")
                print(f"Encryption: {cipher}")
                print(f"Password: {password}")
                print(f"Connection Type: {connection_type}")
                print(f"Radio Type: {radio_type}")
                print(f"Channel: {channel}")
                print(f"Signal: {signal}")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and", len(all_networks))
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()