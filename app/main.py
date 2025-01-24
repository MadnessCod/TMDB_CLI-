import argparse

import httpx


class TMDB:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='TMDB CLI')
        self.add_argument()

    def add_argument(self):
        self.parser.add_argument('-t', '--type', choices=['playing', 'popular', 'top', 'upcoming'],
                                 required=True, help='Type of TMDB')


if __name__ == '__main__':
    tmdb = TMDB()
