import sys, os
from PySide2.QtWidgets import QApplication, QWidget
from widget import Widget

def main(argv):
    app = QApplication(argv)

    w = Widget()
    w.show()

    return app.exec_()

if __name__ == '__main__':

    if not 'QT_QPA_PLATFORM_PLUGING_PATH' in os.environ:
        os.environ['QT_QPA_PLATFORM_PLUGING_PATH'] = './platforms'

    exit_status = main(sys.argv)
    sys.exit(exit_status)