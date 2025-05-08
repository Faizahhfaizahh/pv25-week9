import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QDialog,
    QPushButton, QLineEdit, QVBoxLayout, QFontDialog, QFileDialog, QMessageBox
)
from PyQt5.uic import loadUi

class DialogNama(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Input Nama")

        # Membuat input nama dan tombol OK/Cancel
        self.input = QLineEdit(self)
        self.input.setPlaceholderText("Masukkan nama anda")
        self.ok_button = QPushButton("OK", self)
        self.cancel_button = QPushButton("Cancel", self)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.ok_button)
        layout.addWidget(self.cancel_button)
        self.setLayout(layout)

        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)

    def get_nama(self):
        return self.input.text()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("week9.ui", self)

        # Menghubungkan tombol input nama ke fungsi buka dialog
        self.pushButton_inputNama.clicked.connect(self.bukaDialogNama)

        #  Menghubungkan tombol pilih font ke fungsi pilih font
        self.pushButton_pilihFont.clicked.connect(self.bukaFontDialog)

        #  Menghubungkan tombol buka file ke fungsi buka file
        self.pushButton_bukaFile.clicked.connect(self.bukaFile)

        # Menu bar actions (Fitur) dan Keluar (File)
        self.actionInput_Nama.triggered.connect(lambda: self.tabWidget.setCurrentIndex(0))
        self.actionPilih_Font.triggered.connect(lambda: self.tabWidget.setCurrentIndex(1))
        self.actionBuka_File.triggered.connect(lambda: self.tabWidget.setCurrentIndex(2))
        self.actionKeluar.triggered.connect(self.keluarAplikasi)

    def bukaDialogNama(self):
        self.tabWidget.setCurrentIndex(0) 
        dialog = DialogNama()
        if dialog.exec_() == QDialog.Accepted:
            nama = dialog.get_nama()
            self.label_nama.setText(f"Nama: {nama}")
            self.label_pilihFont.setText(f"Nama: {nama}")

    def bukaFontDialog(self):
        self.tabWidget.setCurrentIndex(1) 
        font, ok = QFontDialog.getFont()
        if ok:
            self.label_nama.setFont(font)
            self.label_pilihFont.setFont(font)

    def bukaFile(self):
        self.tabWidget.setCurrentIndex(2) 
        file_name, _ = QFileDialog.getOpenFileName(self, "Buka File", "", "Text Files (*.txt);;All Files (*)")
        if file_name:
            try:
                # Membaca isi file .txt
                with open(file_name, "r") as file:
                    content = file.read()
                    # Menampilkan isi file ke label_bukaFile
                    self.label_bukaFile.setText(content)
            except Exception as e:
                self.label_bukaFile.setText(f"Error membuka file: {str(e)}")

    def keluarAplikasi(self):
        reply = QMessageBox.question(self, "Konfirmasi", "Yakin ingin keluar?", 
        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            QApplication.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
