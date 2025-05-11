class TestClass:
    def __init__(self):
        from colorama import init, Fore, Style
        from tqdm import tqdm
        import time

        # Initialize colorama for Windows compatibility
        init()

        self.Fore = Fore
        self.Style = Style
        self.tqdm = tqdm
        self.time = time

    def mc(self):
        print("Something from mc")
        self.mp()

    def mp(self):
        print("Something from mp")

    def test_loading_bar(self):
        for i in self.tqdm(range(100), desc="🚀 Loading", unit="🌟 step"):
            self.time.sleep(0.05)  # Simulate work by sleeping for 50ms

    def colorful_loading_bar(self):
        for i in self.tqdm(
            range(100),
            desc="🦄 Loading",
            unit="✨ step",
            colour="cyan",
            bar_format="{l_bar}{bar} 🦄 {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}{postfix}]",
            ascii="⭐ "
        ):
            self.time.sleep(0.05)  # Simulate work by sleeping for 50ms

def main():
    test_instance = TestClass()
    test_instance.mp()
    test_instance.test_loading_bar()
    test_instance.colorful_loading_bar()

if __name__ == "__main__":
    main()