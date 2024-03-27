import ansible_runner
import json
import os

if __name__ == "__main__":
    # Sets ANSIBLE_CONFIG via os.environ
    os.environ["ANSIBLE_CONFIG"] = f"{os.getcwd()}/ansible.cfg"

    print("\n\033[21mGetting hosts\033[0m\n")
    inv, warn = ansible_runner.get_inventory(action="list", inventories=["hosts.yml"])
    inv = json.loads(inv)
    for hostname, dets in inv["_meta"]["hostvars"].items():
        print(hostname)
        print(f"  IP: \033[36m{dets['ansible_host']}\033[0m")

        print("  Groups:")
        children = inv["all"]["children"]
        for child in children:
            if hostname in inv[child]["hosts"]:
                print(f"    - \033[36m{child}\033[0m")

        print()

    print("\033[21mPinging\033[0m\n")
    ansible_runner.run_command("ansible all:localhost -m ping")