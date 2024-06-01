import re
import os

def get_container_id():
    try:
        with open("/proc/self/cgroup", "r") as file:
            for line in file:
                match = re.search(r'/docker/([0-9a-f]+)', line)
                if match:
                    container_id = match.group(1)
                    print(f"Container ID: {container_id}")
                    return container_id
    except Exception as e:
        print(f"Failed to get container ID: {e}")


def write_container_id_to_file():
    container_id = get_container_id()
    with open('container_id.txt', 'w') as file:
        file.write(container_id)
    print(f"Container ID written to file.")


def read_container_id_from_file(filename='container_id.txt'):
    print(os.getcwd())
    try:
        with open(filename, 'r') as file:
            container_id = file.read().strip()
            print(f"Container ID read from file: {container_id}")
            return container_id
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


if __name__ == '__main__':
    write_container_id_to_file()
