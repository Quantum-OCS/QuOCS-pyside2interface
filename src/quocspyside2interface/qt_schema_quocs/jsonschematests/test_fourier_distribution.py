""" Test for Fourier and uniform distribution together """
from qtpy import QtWidgets

from quocspyside2interface.qt_schema_quocs.fourierbasis import FourierBasis


def main():
    import sys
    app = QtWidgets.QApplication()
    Form = QtWidgets.QWidget(parent=None)

    # Load Fourier Widget
    fourier_basis = FourierBasis(parent=Form)
    Form.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

