import ansible_runner
import requests
import os

if __name__ == '__main__':
    # Sets ANSIBLE_CONFIG via os.environ
    os.environ["ANSIBLE_CONFIG"] = f"{os.getcwd()}/ansible.cfg"

    ansible_runner.interface.run_command(executable_cmd="ansible-playbook hello.yml")
    print("\n\033[21mTesting connections\033[0m\n")
    for i in range(1, 4):
        try:
            resp = requests.get("http://0.0.0.0:80/").content.decode("utf-8")
            print(f"Got \033[96m{resp}\033[0m from request {i}")
            print(f" >>> Successful? \033[92m{resp == f'Hello World from managedhost-app-{i} !'}\033[0m")

        except (Exception,) as e:
            print(f"\033[31m{e}\033[0m")
            exit(-1)

        finally:
            print("")

