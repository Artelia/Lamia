import os, sys

lamiapath = os.path.join(os.path.join(os.path.dirname(__file__)), "..", "..")
sys.path.append(lamiapath)
from test.test_utils import *


def main():
    app = initQGis()

    mainwin, canvas, lamiawidget = getDisplayWidget()
    translator = loadLocale()

    exitQGis()


if __name__ == "__main__":
    main()
