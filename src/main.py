import sys, pyperclip, json, requests
from typing import TypedDict
from pathlib import Path
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QCheckBox, QLineEdit,
    QTableWidgetItem, QFileDialog, QMessageBox
)
from PySide6.QtGui import QDesktopServices
from PySide6.QtCore import QTimer, QUrl

from ui.main_window import Ui_MainWindow
from ui import resources_rc
from text_cleaner import TextCleaner


CURRENT_SETTINGS_PATH = Path("settings/current_settings.json")
CURRENT_VERSION = "v1.1.0"

class Settings(TypedDict):
    update_check_at_startup: bool
    trim: bool
    remove_blank_lines: bool
    linebreak_to_space: bool
    multiple_spaces_to_single: bool
    numbered_list_to_plain: bool
    groupbox_case: bool
    upper_case: bool
    lower_case: bool
    capitalize_case: bool
    sentence_case: bool
    groupbox_wrap: bool
    parentheses: bool
    curly_brackets: bool
    square_brackets: bool
    single_quotes: bool
    double_quotes: bool
    single_quotes: bool
    find_and_replace: list[list[str, str]]


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.debounce_timer = QTimer()
        self.debounce_timer.setSingleShot(True)
        self.ignore_next_clipboard_signal = False
        self.init_ui()
        self.init_signals_slots()
        self.show()
        if self.action_update_check_at_startup.isChecked():
            self.check_for_updates()

    def init_ui(self) -> None:
        self.setWindowTitle(f"Auto Clipboard Cheaner {CURRENT_VERSION}")
        self.load_settings()

    def init_signals_slots(self) -> None:
        self.action_check_for_updates.triggered.connect(self.check_for_updates)
        self.action_load.triggered.connect(self.load_settings)
        self.action_export.triggered.connect(self.export_settings)
        self.action_documentation.triggered.connect(
            lambda: QDesktopServices.openUrl(QUrl("https://github.com/riteshkarmakar/auto-clipboard-cleaner/blob/main/README.md"))
        )

        self.action_start.triggered.connect(self.start)
        self.action_stop.triggered.connect(self.stop)
        self.action_reset.triggered.connect(self.reset)

        self.btn_add.clicked.connect(self.add_table_row)
        self.btn_remove.clicked.connect(self.remove_table_row)
        self.tableWidget.currentItemChanged.connect(
            lambda: self.btn_remove.setEnabled(True) if self.tableWidget.currentRow() != -1
            else self.btn_remove.setDisabled(True)
        )
        self.debounce_timer.timeout.connect(self.process_clipboard)

    def check_for_updates(self) -> None:
        url = f"https://api.github.com/repos/riteshkarmakar/auto-clipboard-cleaner/releases/latest"

        try:
            response = None
            response = requests.get(url)
            response.raise_for_status()
        except:
            if self.sender() != self.action_check_for_updates:
                return
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setWindowTitle("Update Check Failed!")
            msg.setText("Unable to fetch update information.")
            msg.setInformativeText("Please check your internet connection or try again later.")
            msg.setDetailedText(f"Error code: {response.status_code if response != None else "None"}\nURL: {url}")
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.exec()
            return
        
        release_data = response.json()
        latest_version = release_data['tag_name']
        release_page_url = release_data['html_url']
        download_url = release_data['assets'][0]['browser_download_url']
        
        if latest_version > CURRENT_VERSION:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setWindowTitle("Update Available")
            msg.setText(
                f"<h3>A New Version ({latest_version}) is Available!</h3>"
                f"To learn more about what's new, click 'View Details' below.</p>"
            )
            msg.setInformativeText("Would you like to update now?")
            msg.setStandardButtons(
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Help | QMessageBox.StandardButton.Cancel
            )
            msg.button(QMessageBox.StandardButton.Help).setText("View Details")
            
            # Open the download URL or View Details
            result = msg.exec()
            if result == QMessageBox.StandardButton.Yes:
                QDesktopServices.openUrl(QUrl(download_url))
            elif result == QMessageBox.StandardButton.Help:
                QDesktopServices.openUrl(QUrl(release_page_url))

        else:
            if self.sender() == self.action_check_for_updates:
                QMessageBox.information(
                    self, "No Update Available", f"You are currently using the latest version ({CURRENT_VERSION})"
                )

    def reset(self) -> None:
        for check_box in self.centralwidget.findChildren(QCheckBox):
            check_box.setChecked(False)
        for line_edit in self.centralwidget.findChildren(QLineEdit):
            line_edit.clear()
        self.tableWidget.setRowCount(0)
        self.groupBox_change_case.setChecked(False)
        self.groupBox_wrap_text.setChecked(False)

    def add_table_row(self) -> None:
        find_text = self.lineEdit_find.text()
        if not find_text:
            return
        replace_with = self.lineEdit_replace.text()

        new_row = self.tableWidget.rowCount()
        self.tableWidget.insertRow(new_row)
        self.tableWidget.setItem(new_row, 0, QTableWidgetItem(find_text))
        self.tableWidget.setItem(new_row, 1, QTableWidgetItem(replace_with))

        for line_edit in self.groupBox_find_replace.findChildren(QLineEdit):
            line_edit.clear()

    def remove_table_row(self) -> None:
        current_row = self.tableWidget.currentRow()
        if current_row != -1:
            self.tableWidget.removeRow(current_row)

    def save_settings(self, path: Path) -> None:
        find_and_replace: list[tuple[str, str]] = []
        for row in range(self.tableWidget.rowCount()):
            find_text = self.tableWidget.item(row, 0).text()
            replace_with = self.tableWidget.item(row, 1).text()
            find_and_replace.append([find_text, replace_with])

        settings: Settings = {
            "update_check_at_startup": self.action_update_check_at_startup.isChecked(),
            "trim": self.checkBox_trim.isChecked(),
            "remove_blank_lines": self.checkBox_remove_blank_lines.isChecked(),
            "linebreak_to_space": self.checkBox_linebreak_to_space.isChecked(),
            "multiple_spaces_to_single": self.checkBox_multiple_spaces_to_single.isChecked(),
            "numbered_list_to_plain": self.checkBox_numbered_list_to_plain.isChecked(),
            "groupbox_case": self.groupBox_change_case.isChecked(),
            "upper_case": self.radioButton_upper.isChecked(),
            "lower_case": self.radioButton_lower.isChecked(),
            "capitalize_case": self.radioButton_capitalize.isChecked(),
            "sentence_case": self.radioButton_sentence.isChecked(),
            "groupbox_wrap": self.groupBox_wrap_text.isChecked(),
            "parentheses": self.radioButton_parenthesis.isChecked(),
            "curly_brackets": self.radioButton_curly_brackets.isChecked(),
            "square_brackets": self.radioButton_square_brackets.isChecked(),
            "single_quotes": self.radioButton_single_quotes.isChecked(),
            "double_quotes": self.radioButton_double_quotes.isChecked(),
            "find_and_replace": find_and_replace
        }

        data = json.dumps(settings, indent="\t")
        path.parent.mkdir(exist_ok=True)
        path.write_text(data)

    def closeEvent(self, event) -> None:
        self.save_settings(CURRENT_SETTINGS_PATH)
        event.accept()

    def load_settings(self) -> None:
        if self.sender() != self.action_load:
            path = CURRENT_SETTINGS_PATH
            if not Path(path).exists(): return
        else:
            path, _ = QFileDialog.getOpenFileName(self, "Load Settings", str(CURRENT_SETTINGS_PATH.parent), filter="JSON (*.json)")
            if not path: return

        with open(path, "r") as file:
            data = file.read()
        settings: Settings = json.loads(data)

        self.action_update_check_at_startup.setChecked(settings.get("update_check_at_startup", True))
        self.checkBox_trim.setChecked(settings.get("trim", False))
        self.checkBox_remove_blank_lines.setChecked(settings.get("remove_blank_lines", False))
        self.checkBox_linebreak_to_space.setChecked(settings.get("linebreak_to_space", False))
        self.checkBox_multiple_spaces_to_single.setChecked(settings.get("multiple_spaces_to_single", False))
        self.checkBox_numbered_list_to_plain.setChecked(settings.get("numbered_list_to_plain", False))
        self.groupBox_change_case.setChecked(settings.get("groupbox_case", False))
        self.radioButton_upper.setChecked(settings.get("upper_case", False))
        self.radioButton_lower.setChecked(settings.get("lower_case", False))
        self.radioButton_capitalize.setChecked(settings.get("capitalize_case", False))
        self.radioButton_sentence.setChecked(settings.get("sentence_case", False))
        self.groupBox_wrap_text.setChecked(settings.get("groupbox_wrap", False))
        self.radioButton_parenthesis.setChecked(settings.get("parentheses", False))
        self.radioButton_curly_brackets.setChecked(settings.get("curly_brackets", False))
        self.radioButton_square_brackets.setChecked(settings.get("square_brackets", False))
        self.radioButton_single_quotes.setChecked(settings.get("single_quotes", False))
        self.radioButton_double_quotes.setChecked(settings.get("double_quotes", False))

        find_and_replace = settings.get("find_and_replace", [])
        self.tableWidget.setRowCount(len(find_and_replace))
        for row, item in enumerate(find_and_replace):
            self.tableWidget.setItem(row, 0, QTableWidgetItem(item[0]))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(item[1]))

    def export_settings(self) -> None:
        path, _ = QFileDialog.getSaveFileName(self, "Save Settings", str(CURRENT_SETTINGS_PATH.parent), filter="JSON (*.json)")
        if path:
            self.save_settings(Path(path))

    def start(self) -> None:
        QApplication.clipboard().dataChanged.connect(self.clipboard_changed)
        self.action_start.setDisabled(True)
        self.action_stop.setEnabled(True)
        self.action_reset.setDisabled(True)

    def stop(self) -> None:
        QApplication.clipboard().dataChanged.disconnect(self.clipboard_changed)
        self.action_stop.setDisabled(True)
        self.action_start.setEnabled(True)
        self.action_reset.setEnabled(True)

    def clipboard_changed(self) -> None:
        # Reset and start the timer on each signal
        self.debounce_timer.start(500)

    def process_clipboard(self) -> None:
        # Avoid processing self-generated signals
        if self.ignore_next_clipboard_signal:
            self.ignore_next_clipboard_signal = False
            return
        
        text = pyperclip.paste()
        text_cleaner = TextCleaner(text)

        # Apply text cleaning operations based on checkboxes
        if self.checkBox_trim.isChecked():
            text_cleaner.trim()
        if self.checkBox_remove_blank_lines.isChecked():
            text_cleaner.remove_blank_lines()
        if self.checkBox_linebreak_to_space.isChecked():
            text_cleaner.replace_linebreak_with_space()
        if self.checkBox_multiple_spaces_to_single.isChecked():
            text_cleaner.multiple_spaces_to_single()
        if self.checkBox_numbered_list_to_plain.isChecked():
            text_cleaner.numbered_list_to_plain()

        # Handle change of case
        if self.groupBox_change_case.isChecked():
            if self.radioButton_upper.isChecked():
                text_cleaner.to_uppercase()
            elif self.radioButton_lower.isChecked():
                text_cleaner.to_lowercase()
            elif self.radioButton_capitalize.isChecked():
                text_cleaner.to_capitalize_case()
            elif self.radioButton_sentence.isChecked():
                text_cleaner.to_sentence_case()

        # Handle wrapping of text
        if self.groupBox_wrap_text.isChecked():
            if self.radioButton_parenthesis.isChecked():
                text_cleaner.wrap_text("Parentheses")
            elif self.radioButton_curly_brackets.isChecked():
                text_cleaner.wrap_text("Curly Brackets")
            elif self.radioButton_square_brackets.isChecked():
                text_cleaner.wrap_text("Square Brackets")
            elif self.radioButton_single_quotes.isChecked():
                text_cleaner.wrap_text("Single Quotes")
            elif self.radioButton_double_quotes.isChecked():
                text_cleaner.wrap_text("Double Quotes")

        # Handle Find & Replace
        for row in range(self.tableWidget.rowCount()):
            find_text = self.tableWidget.item(row, 0).text()
            replace_with = self.tableWidget.item(row, 1).text()
            text_cleaner.find_and_replace(find_text, replace_with)

        # Mark that the next signal for this change is to be ignored
        self.ignore_next_clipboard_signal = True

        # Get the cleaned text and update the clipboard
        cleaned_text = text_cleaner.get_cleaned_text()
        pyperclip.copy(cleaned_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("WindowsVista")
    window = MainWindow()
    sys.exit(app.exec())
