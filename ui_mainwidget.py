# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwidget.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

from QLabel_2 import clickable_Qlabel
from QLineEdit_2 import doubleClickable_QLineEdit
import resources_rc

class Ui_MainWidget(object):
    def setupUi(self, MainWidget):
        if not MainWidget.objectName():
            MainWidget.setObjectName(u"MainWidget")
        MainWidget.resize(650, 670)
        MainWidget.setMinimumSize(QSize(650, 670))
        MainWidget.setMaximumSize(QSize(1080, 670))
        MainWidget.setCursor(QCursor(Qt.ArrowCursor))
        MainWidget.setMouseTracking(False)
        icon = QIcon()
        icon.addFile(u":/img_resources/new_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWidget.setWindowIcon(icon)
        MainWidget.setWindowOpacity(1.000000000000000)
        MainWidget.setAutoFillBackground(False)
        self.layoutWidget = QWidget(MainWidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(21, 2, 603, 658))
        self.verticalLayout_8 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.banner = QLabel(self.layoutWidget)
        self.banner.setObjectName(u"banner")
        self.banner.setPixmap(QPixmap(u":/img_resources/new_banner.png"))

        self.verticalLayout_8.addWidget(self.banner)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.time_comp = QLabel(self.layoutWidget)
        self.time_comp.setObjectName(u"time_comp")
        font = QFont()
        font.setFamilies([u"OCR A Extended"])
        font.setPointSize(16)
        self.time_comp.setFont(font)
        self.time_comp.setCursor(QCursor(Qt.ArrowCursor))
        self.time_comp.setLayoutDirection(Qt.LeftToRight)
        self.time_comp.setMargin(5)
        self.time_comp.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.horizontalLayout.addWidget(self.time_comp)

        self.date_comp = QLabel(self.layoutWidget)
        self.date_comp.setObjectName(u"date_comp")
        self.date_comp.setFont(font)
        self.date_comp.setLayoutDirection(Qt.LeftToRight)
        self.date_comp.setAlignment(Qt.AlignCenter)
        self.date_comp.setMargin(5)

        self.horizontalLayout.addWidget(self.date_comp)

        self.day_comp = QLabel(self.layoutWidget)
        self.day_comp.setObjectName(u"day_comp")
        self.day_comp.setFont(font)
        self.day_comp.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.day_comp.setMargin(5)

        self.horizontalLayout.addWidget(self.day_comp)


        self.verticalLayout_8.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.selector_0 = QLabel(self.layoutWidget)
        self.selector_0.setObjectName(u"selector_0")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selector_0.sizePolicy().hasHeightForWidth())
        self.selector_0.setSizePolicy(sizePolicy)
        self.selector_0.setMaximumSize(QSize(240, 5))
        self.selector_0.setStyleSheet(u"background-color : green;")

        self.verticalLayout.addWidget(self.selector_0)

        self.video_frame_0 = clickable_Qlabel(self.layoutWidget)
        self.video_frame_0.setObjectName(u"video_frame_0")
        self.video_frame_0.setMinimumSize(QSize(240, 180))
        self.video_frame_0.setMaximumSize(QSize(240, 180))
        font1 = QFont()
        font1.setPointSize(7)
        self.video_frame_0.setFont(font1)
        self.video_frame_0.setCursor(QCursor(Qt.PointingHandCursor))
        self.video_frame_0.setStyleSheet(u"border: 2px solid black;")
        self.video_frame_0.setFrameShape(QFrame.NoFrame)
        self.video_frame_0.setFrameShadow(QFrame.Plain)
        self.video_frame_0.setLineWidth(1)
        self.video_frame_0.setMidLineWidth(0)
        self.video_frame_0.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.video_frame_0)

        self.loc_0 = doubleClickable_QLineEdit(self.layoutWidget)
        self.loc_0.setObjectName(u"loc_0")
        self.loc_0.setMaxLength(36)
        self.loc_0.setReadOnly(False)
        self.loc_0.setClearButtonEnabled(False)

        self.verticalLayout.addWidget(self.loc_0)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.selector_1 = QLabel(self.layoutWidget)
        self.selector_1.setObjectName(u"selector_1")
        sizePolicy.setHeightForWidth(self.selector_1.sizePolicy().hasHeightForWidth())
        self.selector_1.setSizePolicy(sizePolicy)
        self.selector_1.setMaximumSize(QSize(240, 5))
        self.selector_1.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.selector_1)

        self.video_frame_1 = clickable_Qlabel(self.layoutWidget)
        self.video_frame_1.setObjectName(u"video_frame_1")
        self.video_frame_1.setMinimumSize(QSize(240, 180))
        self.video_frame_1.setMaximumSize(QSize(240, 180))
        self.video_frame_1.setFont(font1)
        self.video_frame_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.video_frame_1.setStyleSheet(u"border: 2px solid black;")
        self.video_frame_1.setFrameShape(QFrame.NoFrame)
        self.video_frame_1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.video_frame_1)

        self.loc_1 = doubleClickable_QLineEdit(self.layoutWidget)
        self.loc_1.setObjectName(u"loc_1")
        self.loc_1.setMaxLength(36)

        self.verticalLayout_2.addWidget(self.loc_1)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.selector_2 = QLabel(self.layoutWidget)
        self.selector_2.setObjectName(u"selector_2")
        sizePolicy.setHeightForWidth(self.selector_2.sizePolicy().hasHeightForWidth())
        self.selector_2.setSizePolicy(sizePolicy)
        self.selector_2.setMaximumSize(QSize(240, 5))
        self.selector_2.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.selector_2)

        self.video_frame_2 = clickable_Qlabel(self.layoutWidget)
        self.video_frame_2.setObjectName(u"video_frame_2")
        self.video_frame_2.setMinimumSize(QSize(240, 180))
        self.video_frame_2.setMaximumSize(QSize(240, 180))
        self.video_frame_2.setFont(font1)
        self.video_frame_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.video_frame_2.setStyleSheet(u"border: 2px solid black;")
        self.video_frame_2.setFrameShape(QFrame.NoFrame)
        self.video_frame_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.video_frame_2)

        self.loc_2 = doubleClickable_QLineEdit(self.layoutWidget)
        self.loc_2.setObjectName(u"loc_2")
        self.loc_2.setMaxLength(36)

        self.verticalLayout_3.addWidget(self.loc_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.selector_3 = QLabel(self.layoutWidget)
        self.selector_3.setObjectName(u"selector_3")
        sizePolicy.setHeightForWidth(self.selector_3.sizePolicy().hasHeightForWidth())
        self.selector_3.setSizePolicy(sizePolicy)
        self.selector_3.setMaximumSize(QSize(240, 5))
        self.selector_3.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.selector_3)

        self.video_frame_3 = clickable_Qlabel(self.layoutWidget)
        self.video_frame_3.setObjectName(u"video_frame_3")
        self.video_frame_3.setMinimumSize(QSize(240, 180))
        self.video_frame_3.setMaximumSize(QSize(240, 180))
        self.video_frame_3.setFont(font1)
        self.video_frame_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.video_frame_3.setStyleSheet(u"border: 2px solid black;")
        self.video_frame_3.setFrameShape(QFrame.NoFrame)
        self.video_frame_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.video_frame_3)

        self.loc_3 = doubleClickable_QLineEdit(self.layoutWidget)
        self.loc_3.setObjectName(u"loc_3")
        self.loc_3.setMaxLength(36)

        self.verticalLayout_4.addWidget(self.loc_3)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_4.addLayout(self.verticalLayout_6)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.video_file_button = QPushButton(self.layoutWidget)
        self.video_file_button.setObjectName(u"video_file_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.video_file_button.sizePolicy().hasHeightForWidth())
        self.video_file_button.setSizePolicy(sizePolicy1)

        self.verticalLayout_5.addWidget(self.video_file_button)

        self.add_ip_cam = QPushButton(self.layoutWidget)
        self.add_ip_cam.setObjectName(u"add_ip_cam")
        sizePolicy1.setHeightForWidth(self.add_ip_cam.sizePolicy().hasHeightForWidth())
        self.add_ip_cam.setSizePolicy(sizePolicy1)

        self.verticalLayout_5.addWidget(self.add_ip_cam)

        self.open_camera_button = QPushButton(self.layoutWidget)
        self.open_camera_button.setObjectName(u"open_camera_button")
        sizePolicy1.setHeightForWidth(self.open_camera_button.sizePolicy().hasHeightForWidth())
        self.open_camera_button.setSizePolicy(sizePolicy1)

        self.verticalLayout_5.addWidget(self.open_camera_button)

        self.start_button = QPushButton(self.layoutWidget)
        self.start_button.setObjectName(u"start_button")
        sizePolicy1.setHeightForWidth(self.start_button.sizePolicy().hasHeightForWidth())
        self.start_button.setSizePolicy(sizePolicy1)

        self.verticalLayout_5.addWidget(self.start_button)

        self.stop_button = QPushButton(self.layoutWidget)
        self.stop_button.setObjectName(u"stop_button")
        sizePolicy1.setHeightForWidth(self.stop_button.sizePolicy().hasHeightForWidth())
        self.stop_button.setSizePolicy(sizePolicy1)
        self.stop_button.setCheckable(False)
        self.stop_button.setChecked(False)

        self.verticalLayout_5.addWidget(self.stop_button)


        self.horizontalLayout_4.addLayout(self.verticalLayout_5)


        self.verticalLayout_8.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.prediction_label = QLabel(self.layoutWidget)
        self.prediction_label.setObjectName(u"prediction_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.prediction_label.sizePolicy().hasHeightForWidth())
        self.prediction_label.setSizePolicy(sizePolicy2)
        self.prediction_label.setMinimumSize(QSize(260, 0))
        font2 = QFont()
        font2.setPointSize(16)
        self.prediction_label.setFont(font2)

        self.horizontalLayout_5.addWidget(self.prediction_label)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, -1, -1, -1)
        self.res_label1 = QLabel(self.layoutWidget)
        self.res_label1.setObjectName(u"res_label1")
        sizePolicy.setHeightForWidth(self.res_label1.sizePolicy().hasHeightForWidth())
        self.res_label1.setSizePolicy(sizePolicy)

        self.verticalLayout_7.addWidget(self.res_label1, 0, Qt.AlignHCenter)

        self.res_cnum0 = doubleClickable_QLineEdit(self.layoutWidget)
        self.res_cnum0.setObjectName(u"res_cnum0")
        self.res_cnum0.setMinimumSize(QSize(160, 0))
        self.res_cnum0.setStyleSheet(u"")
        self.res_cnum0.setMaxLength(10)

        self.verticalLayout_7.addWidget(self.res_cnum0, 0, Qt.AlignHCenter)

        self.res_label2 = QLabel(self.layoutWidget)
        self.res_label2.setObjectName(u"res_label2")
        sizePolicy.setHeightForWidth(self.res_label2.sizePolicy().hasHeightForWidth())
        self.res_label2.setSizePolicy(sizePolicy)

        self.verticalLayout_7.addWidget(self.res_label2, 0, Qt.AlignHCenter)

        self.res_cnum1 = doubleClickable_QLineEdit(self.layoutWidget)
        self.res_cnum1.setObjectName(u"res_cnum1")
        self.res_cnum1.setMinimumSize(QSize(160, 0))
        self.res_cnum1.setMaxLength(10)

        self.verticalLayout_7.addWidget(self.res_cnum1, 0, Qt.AlignHCenter)


        self.horizontalLayout_5.addLayout(self.verticalLayout_7)

        self.clear_predictions = QPushButton(self.layoutWidget)
        self.clear_predictions.setObjectName(u"clear_predictions")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.clear_predictions.sizePolicy().hasHeightForWidth())
        self.clear_predictions.setSizePolicy(sizePolicy3)
        self.clear_predictions.setMinimumSize(QSize(150, 50))
        self.clear_predictions.setMaximumSize(QSize(150, 70))
        font3 = QFont()
        font3.setPointSize(10)
        self.clear_predictions.setFont(font3)

        self.horizontalLayout_5.addWidget(self.clear_predictions)


        self.verticalLayout_8.addLayout(self.horizontalLayout_5)


        self.retranslateUi(MainWidget)

        self.stop_button.setDefault(False)


        QMetaObject.connectSlotsByName(MainWidget)
    # setupUi

    def retranslateUi(self, MainWidget):
        MainWidget.setWindowTitle(QCoreApplication.translate("MainWidget", u"HawkAI", None))
        self.banner.setText("")
        self.time_comp.setText(QCoreApplication.translate("MainWidget", u"00:00:00 AM/PM", None))
        self.date_comp.setText(QCoreApplication.translate("MainWidget", u"MM/DD/YY", None))
        self.day_comp.setText(QCoreApplication.translate("MainWidget", u"DAY", None))
        self.selector_0.setText("")
        self.video_frame_0.setText(QCoreApplication.translate("MainWidget", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">Stream # 1</span></p><p><span style=\" font-size:10pt;\">Load a video stream by clicking </span></p><p><span style=\" font-size:10pt;\">&quot;Select Video File&quot;,</span></p><p><span style=\" font-size:10pt;\">&quot;Add IP Feed&quot;,</span></p><p><span style=\" font-size:10pt;\">or &quot;Open Camera&quot;.</span></p></body></html>", None))
        self.loc_0.setPlaceholderText(QCoreApplication.translate("MainWidget", u"Enter Location 1", None))
        self.selector_1.setText("")
        self.video_frame_1.setText(QCoreApplication.translate("MainWidget", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">Stream # 2</span></p><p><span style=\" font-size:10pt;\">Load a video stream by clicking </span></p><p><span style=\" font-size:10pt;\">&quot;Select Video File&quot;,</span></p><p><span style=\" font-size:10pt;\">&quot;Add IP Feed&quot;,</span></p><p><span style=\" font-size:10pt;\">or &quot;Open Camera&quot;.</span></p></body></html>", None))
        self.loc_1.setPlaceholderText(QCoreApplication.translate("MainWidget", u"Enter Location 2", None))
        self.selector_2.setText("")
        self.video_frame_2.setText(QCoreApplication.translate("MainWidget", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">Stream # 3</span></p><p><span style=\" font-size:10pt;\">Load a video stream by clicking </span></p><p><span style=\" font-size:10pt;\">&quot;Select Video File&quot;,</span></p><p><span style=\" font-size:10pt;\">&quot;Add IP Feed&quot;,</span></p><p><span style=\" font-size:10pt;\">or &quot;Open Camera&quot;.</span></p></body></html>", None))
        self.loc_2.setPlaceholderText(QCoreApplication.translate("MainWidget", u"Enter Location 3", None))
        self.selector_3.setText("")
        self.video_frame_3.setText(QCoreApplication.translate("MainWidget", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">Stream # 4</span></p><p><span style=\" font-size:10pt;\">Load a video stream by clicking </span></p><p><span style=\" font-size:10pt;\">&quot;Select Video File&quot;,</span></p><p><span style=\" font-size:10pt;\">&quot;Add IP Feed&quot;,</span></p><p><span style=\" font-size:10pt;\">or &quot;Open Camera&quot;.</span></p></body></html>", None))
        self.loc_3.setPlaceholderText(QCoreApplication.translate("MainWidget", u"Enter Location 4", None))
        self.video_file_button.setText(QCoreApplication.translate("MainWidget", u"Select Video File", None))
        self.add_ip_cam.setText(QCoreApplication.translate("MainWidget", u"Add IP Feed", None))
        self.open_camera_button.setText(QCoreApplication.translate("MainWidget", u"Open Camera", None))
        self.start_button.setText(QCoreApplication.translate("MainWidget", u"Start", None))
        self.stop_button.setText(QCoreApplication.translate("MainWidget", u"Stop", None))
        self.prediction_label.setText(QCoreApplication.translate("MainWidget", u"PREDICTIONS", None))
        self.res_label1.setText(QCoreApplication.translate("MainWidget", u"Enter Responder 1 Number:", None))
        self.res_cnum0.setPlaceholderText(QCoreApplication.translate("MainWidget", u"e.g. 9*********", None))
        self.res_label2.setText(QCoreApplication.translate("MainWidget", u"Enter Responder 2 Number:", None))
        self.res_cnum1.setText("")
        self.res_cnum1.setPlaceholderText(QCoreApplication.translate("MainWidget", u"e.g. 9*********", None))
        self.clear_predictions.setText(QCoreApplication.translate("MainWidget", u"Clear Predictions / \n"
"Stop Alarm", None))
    # retranslateUi

