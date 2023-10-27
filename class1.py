class Hello:
    def __init__(self, name):
        self.name = name


class Hi(Hello):
    def __init__(self, name):
        super().__init__(name=name)

    def __str__(self):
        return f'Hi, {self.name}'
