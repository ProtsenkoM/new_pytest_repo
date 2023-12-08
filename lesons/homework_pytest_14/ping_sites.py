import subprocess
import platform


def ping_websites(websites, count=3):
    for website in websites:
        if platform.system().lower() == "windows":
            command = ["ping", "-n", str(count), website]
        else:
            command = ["ping", "-c", str(count), website]

        try:
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Failed to ping {website}. Error: {e}")


if __name__ == '__main__':
    websites_to_ping = ["www.google.com", "www.ithillel.ua"]
    ping_websites(websites_to_ping, count=3)
