import fire

class Ships():

    def sail(self):
        Ships_name = "your ship"
        print(f"{Ships_name} is setting sail")

    def list(self):
        ships = ['john b', 'pequod']
        print(f"ships: {','.join(ships)}")


def sailors(greeting , name):
    message = f'{greeting} {name}'
    print(message)


class Cli():

    def __init__(self):
        self.sailors = sailors
        self.ships = Ships()


if __name__ == '__main__':
    fire.Fire(Cli)