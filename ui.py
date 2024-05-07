# coding=utf-8
# @FileName      :test
# @Time          :2023/7/22 20:37
# @Author        :AhrIlI
# @Contact       :906629272@qq.com

import sys

import maya.cmds as cmds
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from driveF import *
from uiTool import *


# class MasterWindow(QWidget):
#     def __init__(self, parent = None):
#         super(MasterWindow, self).__init__(parent)
#         self.setWindowFlags(self.windowFlags() | Qt.Window)
#         self.setWindowTitle(u"匹配ADV的骨骼驱动")
#         self.resize(500, 950)
#         self.setMinimumSize(500, 900)
#         self.setObjectName("UVDMainWin")
#
#         self.main_layout = QVBoxLayout()
#         self.main_layout.setContentsMargins(0, 0, 0, 0)
#         self.setLayout(self.main_layout)
#
#         self.left_tag = uiWidget.TadWidget()
#         with open(__file__ + "/../uiTool/res/qss/TadWidgetQSS.qss", "r") as f:
#             self.tag_lqss = f.read()
#         self.tag_rqss = "QStackedWidget {background: rgb(47, 56, 69);}"
#         self.left_tag.setStyleSheetLR(lqss = self.tag_lqss, rqss = self.tag_rqss)
#         self.widget1 = DriveMWindow(self)
#         self.widget2 = uiWidget.Splitter(text = u"这也是一个测试，看看怎么样", w = self.width(), h = 10)
#         self.icon_p = QIcon(__file__ + "/../uiTool/res/images/Gear.png")
#         self.left_tag.addInsertItem(
#             [self.icon_p, self.icon_p],
#             [self.widget1, self.widget2]
#         )
#         self.main_layout.addWidget(self.left_tag)


class DriveMWindow(QWidget):
    u"""
    创建驱动主界面
    """

    def __init__(self, parent = None):
        """

        :param parent:
        """
        super(DriveMWindow, self).__init__(parent)
        self.setWindowFlags(self.windowFlags() | Qt.Window)
        self.setWindowTitle(u"匹配ADV的骨骼驱动")
        self.resize(600, 1100)
        self.setMinimumSize(500, 1100)
        self.setStyleSheet("background: rgb(60, 69, 82);")

        self.setObjectName("UVDriveTool")
        self.drive_fun = driveFunction.DriveFunC(parent)
        self.drive_fun.upDate()
        self.script_job_id = 0

        self._createLineEditPBtn()
        self._createSplitter()
        self._createSliderBtn()
        self._createLabel()
        self._createPushBtn()
        self._createCollapsibleBox()
        self._createLayouts()
        self._createConnect()

        self._updateInfoUI()

        if self.script_job_id != 0:
            if cmds.scriptJob(ex = self.script_job_id):
                self.script_job_id = 0
        elif self.script_job_id == 0:
            self.script_job_id = cmds.scriptJob(runOnce = True, e = [u"SceneOpened", self.sceneOpened])

    def update(self):
        super(DriveMWindow, self).update()
        if cmds.objExists("ALL_UVDrive_Control_Grp"):
            self.create_loc_label.setText(u"重建驱动")
            self.build_btn.setVisible(False)
            self.rebuild_btn.setVisible(True)
            self.toggle_btn.setVisible(True)
        else:
            self.create_loc_label.setText(u"构建驱动")
            self.build_btn.setVisible(True)
            self.rebuild_btn.setVisible(False)
            self.toggle_btn.setVisible(False)

    def sceneOpened(self):
        """
        当maya开新的场景时，更新DriveFunC的数据，同时刷新界面状态
        :return:
        """
        self.script_job_id = cmds.scriptJob(runOnce = True, e = [u"SceneOpened", self.sceneOpened])
        self._updateInfoUI()
        self.drive_fun.upDate()

    def _updateInfoUI(self):
        """
        更新界面状态
        :return:
        """
        if cmds.objExists("ALL_UVDrive_Control_Grp"):
            self.create_loc_label.setText(u"重建驱动")
            self.build_btn.setVisible(False)
            self.rebuild_btn.setVisible(True)
            self.toggle_btn.setVisible(True)
        else:
            self.create_loc_label.setText(u"构建驱动")
            self.build_btn.setVisible(True)
            self.rebuild_btn.setVisible(False)
            self.toggle_btn.setVisible(False)

    def _createLayouts(self):
        """
        布局
        :return:
        """
        self.main_layout = QVBoxLayout()
        # self.main_layout.setAlignment(Qt.AlignHCenter)
        self.main_layout.setContentsMargins(10, 0, 10, 0)
        self.setLayout(self.main_layout)
        self.main_layout.addWidget(self.line_edit_pbtn)
        self.main_layout.addWidget(self.create_joint_splitter)
        self.main_layout.addSpacing(10)
        self.main_layout.addWidget(self.all_sbtn)
        self.main_layout.setAlignment(self.all_sbtn, Qt.AlignHCenter)
        self.grid_joint_layout = QGridLayout()
        self.main_layout.addLayout(self.grid_joint_layout)
        self.grid_joint_layout.addWidget(self.wrist_sbtn, 0, 0, Qt.AlignHCenter)
        self.grid_joint_layout.addWidget(self.elbow_sbtn, 0, 1, Qt.AlignHCenter)
        self.grid_joint_layout.addWidget(self.shoulder_sbtn, 0, 2, Qt.AlignHCenter)
        self.grid_joint_layout.addWidget(self.ankle_sbtn, 0, 3, Qt.AlignHCenter)
        self.grid_joint_layout.addWidget(self.knee_sbtn, 1, 0, Qt.AlignHCenter)
        self.grid_joint_layout.addWidget(self.hip_sbtn, 1, 1, Qt.AlignHCenter)
        self.grid_joint_layout.addWidget(self.finger_sbtn, 1, 2, Qt.AlignHCenter)
        self.main_layout.addSpacing(10)
        self.main_layout.addWidget(self.create_loc)
        self.main_layout.addSpacing(5)
        self.main_layout.addWidget(self.c_box)
        self.main_layout.addWidget(self.mirror_loc)
        self.main_layout.addSpacing(5)
        self.main_layout.addWidget(self.build_drive_splitter)
        self.main_layout.addSpacing(5)
        self.main_layout.addWidget(self.create_loc_label)
        self.main_layout.setAlignment(self.create_loc_label, Qt.AlignHCenter)
        self.main_layout.addWidget(self.build_btn)
        self.build_layout = QHBoxLayout()
        self.main_layout.addLayout(self.build_layout)
        self.build_layout.addWidget(self.toggle_btn)
        self.build_layout.addWidget(self.rebuild_btn)
        self.main_layout.addSpacing(25)
        self.main_layout.addWidget(self.other_joint_splitter)
        self.main_layout.addSpacing(5)
        self.main_layout.addWidget(self.add_drv_label)
        self.main_layout.setAlignment(self.add_drv_label, Qt.AlignHCenter)
        self.add_drv_layout = QHBoxLayout()
        self.main_layout.addLayout(self.add_drv_layout)
        self.add_drv_layout.addWidget(self.add_drv_joint)
        self.add_drv_layout.addWidget(self.remove_drv_joint)
        self.main_layout.addSpacing(5)
        self.main_layout.addWidget(self.mirror_sdk_label)
        self.main_layout.setAlignment(self.mirror_sdk_label, Qt.AlignHCenter)
        self.main_layout.addSpacing(5)
        self.main_layout.addWidget(self.select_add_driven_attr)
        self.edit_sdk_layout = QGridLayout()
        self.main_layout.addLayout(self.edit_sdk_layout)
        self.edit_sdk_layout.addWidget(self.edit_sdk_btn, 0, 0)
        self.edit_sdk_layout.addWidget(self.remove_sdk_btn, 0, 1)
        self.edit_sdk_layout.addWidget(self.mirror_sdk_rtl, 1, 0)
        self.edit_sdk_layout.addWidget(self.mirror_sdk_ltr, 1, 1)

        self.main_layout.addSpacing(10)
        self.main_layout.addWidget(self.select_joint_btn)

        self.main_layout.addSpacerItem(QSpacerItem(1, 1, QSizePolicy.Fixed, QSizePolicy.Expanding))

    def _createLineEditPBtn(self):
        """
        创建加载模型工具
        :return:
        """
        self.line_edit_pbtn = uiWidget.LineEditPBtn(label = u"模型：", stype = u"mesh")
        self.select_drv_joint_pbtn = uiWidget.LineEditPBtn(label = u"驱动骨：", stype = u"joint")
        self.select_add_driven_attr = LineEditPBtnFix(label = u"属性:", stype = u"joint")

    def _createSplitter(self):
        """
        创建分割线
        :return:
        """
        self.create_joint_splitter = uiWidget.Splitter(text = u"需要创建的骨骼", w = self.width(), h = 20)
        self.build_drive_splitter = uiWidget.Splitter(rgb = (143, 178, 201), w = self.width(), h = 20)
        self.other_joint_splitter = uiWidget.Splitter(text = u"其他功能", w = self.width(), h = 20)

    def _createPushBtn(self):
        """
        按钮
        :return:
        """
        with open(__file__ + "/../uiTool/res/qss/PushBtnQSS.qss", "r") as f:
            qss = f.read()
        self.create_loc = QPushButton(u"创建定位的Locator")
        self.select_joint_locator = QPushButton(u"选择骨骼点击创建")
        self.locator_one_constrain = QPushButton(u"单个骨骼约束")
        self.mirror_loc = QPushButton(u"镜像Locator R>>>L")
        self.build_btn = QPushButton(u"构建驱动系统")
        self.rebuild_btn = QPushButton(u"重构驱动系统")
        self.toggle_btn = QPushButton(u"返回Locator设置")
        self.select_joint_btn = QPushButton(u"选择驱动的骨骼")
        self.add_drv_joint = QPushButton(u"添加")
        self.remove_drv_joint = QPushButton(u"移除")
        self.edit_sdk_btn = QPushButton(u"选择控制器点击调整SDK")
        self.remove_sdk_btn = QPushButton(u"选择控制器点击移除SDK")
        self.mirror_sdk_rtl = QPushButton(u"镜像SDK R>>>L")
        self.mirror_sdk_ltr = QPushButton(u"镜像SDK L>>>R")

        self.rebuild_btn.setVisible(False)
        self.toggle_btn.setVisible(False)

        self.create_loc.setStyleSheet(qss)
        self.select_joint_locator.setStyleSheet(qss)
        self.locator_one_constrain.setStyleSheet(qss)
        self.mirror_loc.setStyleSheet(qss)
        self.build_btn.setStyleSheet(qss)
        self.rebuild_btn.setStyleSheet(qss)
        self.toggle_btn.setStyleSheet(qss)
        self.select_joint_btn.setStyleSheet(qss)
        self.add_drv_joint.setStyleSheet(qss)
        self.remove_drv_joint.setStyleSheet(qss)
        self.edit_sdk_btn.setStyleSheet(qss)
        self.remove_sdk_btn.setStyleSheet(qss)
        self.mirror_sdk_rtl.setStyleSheet(qss)
        self.mirror_sdk_ltr.setStyleSheet(qss)

    def _createLabel(self):
        """
        提示标签
        :return:
        """
        qss = "color: rgb(248, 244, 237); font: bold 10pt Microsoft YaHei;"
        self.select_joint_add_label = QLabel(u"加载驱动骨骼后，开启需要创建的方向")
        self.locator_one_constrain_label = QLabel(
            u"选择Locator点击按钮添加属性\n当Locator存在该属性时，只会被单个骨骼约束")
        self.create_loc_label = QLabel(u"构建驱动")
        self.add_drv_label = QLabel(u"单个关节添加驱动属性")
        self.mirror_sdk_label = QLabel(u"加载驱动属性调整SDK")

        self.select_joint_add_label.setStyleSheet(qss)
        self.locator_one_constrain_label.setStyleSheet(qss)
        self.create_loc_label.setStyleSheet(qss)
        self.add_drv_label.setStyleSheet(qss)
        self.mirror_sdk_label.setStyleSheet(qss)

    def _createSliderBtn(self):
        """
        创建滑动按钮
        :return:
        """
        self.all_sbtn = uiWidget.TextSliderBtn(w = 40, h = 20, text = u"ALL", grcon = (140, 162, 196),
                                               grcoff = (82, 91, 104))
        self.wrist_sbtn = uiWidget.TextSliderBtn(w = 40, h = 20, text = u"Wrist", grcon = (140, 162, 196),
                                                 grcoff = (82, 91, 104))
        self.elbow_sbtn = uiWidget.TextSliderBtn(w = 40, h = 20, text = u"Elbow", grcon = (140, 162, 196),
                                                 grcoff = (82, 91, 104))
        self.shoulder_sbtn = uiWidget.TextSliderBtn(w = 40, h = 20, text = u"Shoulder", grcon = (140, 162, 196),
                                                    grcoff = (82, 91, 104))
        self.ankle_sbtn = uiWidget.TextSliderBtn(w = 40, h = 20, text = u"Ankle", grcon = (140, 162, 196),
                                                 grcoff = (82, 91, 104))
        self.knee_sbtn = uiWidget.TextSliderBtn(w = 40, h = 20, text = u"Knee", grcon = (140, 162, 196),
                                                grcoff = (82, 91, 104))
        self.hip_sbtn = uiWidget.TextSliderBtn(w = 40, h = 20, text = u"Hip", grcon = (140, 162, 196),
                                               grcoff = (82, 91, 104))
        self.finger_sbtn = uiWidget.TextSliderBtn(w = 40, h = 20, text = u"Finger", grcon = (140, 162, 196),
                                                  grcoff = (82, 91, 104))
        self.all_list_sbtn = [self.wrist_sbtn, self.elbow_sbtn, self.shoulder_sbtn, self.ankle_sbtn, self.knee_sbtn,
                              self.hip_sbtn, self.finger_sbtn]

    def _createCollapsibleBox(self):
        """
        折叠控件，手动添加locator和驱动骨骼放入此下
        :return:
        """
        self.c_box = uiWidget.CollapsibleBox(u"添加额外的locator")
        self.cbox_add_layout = QVBoxLayout()
        self.cbox_grid_layout = QGridLayout()
        self.cbox_add_layout.addWidget(self.select_drv_joint_pbtn)
        self.fy_sbtn = uiWidget.TextSliderBtn(w = 40, h = 20, text = u"+Y", grcon = (140, 162, 196),
                                              grcoff = (82, 91, 104))
        self.by_sbtn = uiWidget.TextSliderBtn(w = 40, h = 20, text = u"-Y", grcon = (140, 162, 196),
                                              grcoff = (82, 91, 104))
        self.fz_sbtn = uiWidget.TextSliderBtn(w = 40, h = 20, text = u"+Z", grcon = (140, 162, 196),
                                              grcoff = (82, 91, 104))
        self.bz_sbtn = uiWidget.TextSliderBtn(w = 40, h = 20, text = u"-Z", grcon = (140, 162, 196),
                                              grcoff = (82, 91, 104))
        self.all_selected_dri_sbtn = [self.fy_sbtn, self.by_sbtn, self.fz_sbtn, self.bz_sbtn]
        self.cbox_add_layout.addWidget(self.select_joint_add_label)
        self.cbox_add_layout.setAlignment(self.select_joint_add_label, Qt.AlignHCenter)
        self.cbox_add_layout.addSpacing(5)
        self.cbox_add_layout.addLayout(self.cbox_grid_layout)
        self.cbox_grid_layout.addWidget(self.fy_sbtn, 0, 0, Qt.AlignHCenter)
        self.cbox_grid_layout.addWidget(self.by_sbtn, 0, 1, Qt.AlignHCenter)
        self.cbox_grid_layout.addWidget(self.fz_sbtn, 0, 2, Qt.AlignHCenter)
        self.cbox_grid_layout.addWidget(self.bz_sbtn, 0, 3, Qt.AlignHCenter)
        self.cbox_add_layout.addWidget(self.select_joint_locator)
        self.cbox_add_layout.addSpacing(5)
        self.cbox_add_layout.addWidget(self.locator_one_constrain_label)
        self.cbox_add_layout.setAlignment(self.locator_one_constrain_label, Qt.AlignHCenter)
        self.cbox_add_layout.addWidget(self.locator_one_constrain)
        self.c_box.setContentLayout(self.cbox_add_layout)

    def _createConnect(self):
        """
        连接信号
        :return:
        """
        self.all_sbtn.btn.toggled.connect(self._allSbtnSlot)
        self.line_edit_pbtn.textChanged.connect(self._setDriveFMesh)
        self.create_loc.clicked.connect(self._driveFCreateTransform)
        self.select_joint_locator.clicked.connect(self._createSelectedJointLoc)
        self.mirror_loc.clicked.connect(self._commandMirrorLocator)
        self.build_btn.clicked.connect(self._createDriveS)
        self.locator_one_constrain.clicked.connect(self._addLocatorAttr)
        self.toggle_btn.clicked.connect(self._reSetLocatorPos)
        self.select_joint_btn.clicked.connect(self._selectJoint)
        self.rebuild_btn.clicked.connect(self._reBuildConnect)
        self.add_drv_joint.clicked.connect(self._addDrivenBySelect)
        self.remove_drv_joint.clicked.connect(self._deleteDrivenBySelect)
        self.edit_sdk_btn.clicked.connect(self._setSDK)
        self.remove_sdk_btn.clicked.connect(self._removeSDK)
        # self.select_joint_btn.clicked.connect(self._selectJoint)

    def _selectJoint(self):
        """
        选择驱动骨骼
        :return:
        """
        select_list = self.drive_fun.getJoint()
        cmds.select(select_list)

    def _reBuildConnect(self):
        """
        重建
        :return:
        """
        self.drive_fun.reBuild()
        return cmds.warning(u"+++++重建完成+++++\n")

    def _createDriveS(self):
        """
        构建驱动
        :return:
        """
        self.drive_fun.createDriveSystem()
        cmds.select(cl = True)
        self.update()
        return cmds.warning(u"+++++构建完成+++++\n")

    def _reSetLocatorPos(self):
        """
        修改locator位置
        :return:
        """
        tf = cmds.getAttr("ALL_UVDrive_Control_Grp.visibility")
        if tf:
            cmds.setAttr("ALL_UVDrive_Control_Grp.visibility", 0)
            cmds.setAttr("Pos_Locator_Grp.visibility", 1)
        else:
            cmds.setAttr("ALL_UVDrive_Control_Grp.visibility", 1)
            cmds.setAttr("Pos_Locator_Grp.visibility", 0)

    def _addLocatorAttr(self):
        """
        为Locator添加属性
        :return:
        """
        loc_list = cmds.ls(sl = True)
        add_list = list()
        for loc in loc_list:
            shape = cmds.listRelatives(loc, s = True)
            if shape is not None:
                if cmds.objectType(shape[0]) == "locator":
                    add_list.append(loc)
        if len(add_list) > 0:
            for loc in loc_list:
                self.drive_fun.addLocatorAttr(loc)
        else:
            cmds.warning(u"选择locator再点击！")

    def _commandMirrorLocator(self):
        """
        镜像Locator
        :return:
        """
        self.drive_fun.createMirrorLocator()

    def _setDriveFMesh(self, text):
        """
        更新drive_fun.mesh
        :param text:
        :return:
        """
        if text:
            self.drive_fun.mesh = text
        else:
            self.drive_fun.mesh = None

    def _driveFCreateTransform(self):
        """
        drive_fun._createTransform 创建必要的组与Locator
        :return:
        """
        joint_list = list()
        for jnt in self.all_list_sbtn:
            if jnt.btn.getChecked():
                joint_list.append(jnt.text + "_R")
        self.drive_fun.createTransform(joint_list)

    def _createSelectedJointLoc(self):
        """
        选择骨骼点击创建
        :return:
        """
        joint = cmds.ls(sl = True)
        drive_jnt = self.select_drv_joint_pbtn.obj
        direction_tf = list()
        re_locator = list()
        for tf in self.all_selected_dri_sbtn:
            direction_tf.append(tf.btn.getChecked())
        for j in joint:
            if cmds.objectType(j) != u"joint":
                return cmds.warning(j + u"不是骨骼！")
            else:
                self.drive_fun.createSelectJointLocator(j, drive_jnt, direction_tf, re_locator)
        if len(re_locator) != 0:
            cmds.warning(re_locator)

    def _addDrivenBySelect(self):
        """
        选择骨骼添加驱动
        :return:
        """
        joint = cmds.ls(sl = True, type = "joint")[0]
        if len(joint) != 0:
            self.drive_fun.addDriveFn(joint)
        else:
            cmds.warning(u"请选择骨骼!")

    def _deleteDrivenBySelect(self):
        """
        删除所选骨骼的驱动
        :return:
        """
        joint = cmds.ls(sl = True, type = "joint")[0]
        if len(joint) != 0:
            self.drive_fun.deleteDrivenFn(joint)
        else:
            cmds.warning(u"请选择骨骼!")

    def _setSDK(self):
        """
        选择控制器调整SDK
        :return:
        """
        control = cmds.ls(sl = True)
        attr = self.select_add_driven_attr.obj
        self.drive_fun.setDrivenKeyByCon(control, attr)

    def _removeSDK(self):
        """
        移除SDK
        :return:
        """
        control = cmds.ls(sl = True)
        for c in control:
            p = cmds.listRelatives(c, p = True)[0]
            driveFunction.deleSDKNode(p)

    def _getAllDrivenJoint(self):
        """
        选择所有创建出来的骨骼
        :return:
        """
        cmds.undoInfo(ock = 1)
        select_list = []
        for j in cmds.ls(type = "joint"):
            if cmds.objExists("{0}.uvt".format(j)):
                select_list.append(j)
        cmds.select(select_list)
        cmds.undoInfo(cck = 1)

    def testF(self):
        print(self.drive_fun.mesh)

    def _allSbtnSlot(self, torf):
        """
        self.all_sbtn按钮连接的槽函数
        :return:
        """
        self.wrist_sbtn.btn.setChecked(torf)
        self.elbow_sbtn.btn.setChecked(torf)
        self.shoulder_sbtn.btn.setChecked(torf)
        self.ankle_sbtn.btn.setChecked(torf)
        self.knee_sbtn.btn.setChecked(torf)
        self.hip_sbtn.btn.setChecked(torf)
        self.finger_sbtn.btn.setChecked(torf)

        inv = not torf
        self.wrist_sbtn.btn.setEnabled(inv)
        self.elbow_sbtn.btn.setEnabled(inv)
        self.shoulder_sbtn.btn.setEnabled(inv)
        self.ankle_sbtn.btn.setEnabled(inv)
        self.knee_sbtn.btn.setEnabled(inv)
        self.hip_sbtn.btn.setEnabled(inv)
        self.finger_sbtn.btn.setEnabled(inv)


class LineEditPBtnFix(uiWidget.LineEditPBtn):
    def loadSelected(self):
        """

        :return:
        """
        selected = cmds.ls(sl = True, o = True)
        attr = cmds.channelBox("mainChannelBox", q = True, sma = True)[0]
        if len(selected) == 1:
            get_shapes = cmds.listRelatives(selected[0], s = True)
            try:
                for s in get_shapes:
                    if not cmds.getAttr(s + ".intermediateObject"):
                        shape = s
                selected_type = cmds.objectType(shape)
            except:
                selected_type = cmds.objectType(selected[0])
            if selected_type != self.stype:
                return cmds.warning(u"请选择{0}加载".format(self.stype))
            self.setLineText(selected[0] + "." + attr)
            self.textChanged.emit(self.line.text())
        else:
            self.obj = None
            self.line.clear()
            self.textChanged.emit(self.line.text())
            return cmds.warning(u"请选择一个{0}加载".format(self.stype))


# def main():
#     app = QApplication(sys.argv)
#
#     main_wnd = MasterWindow()
#     main_wnd.show()
#
#     sys.exit(app.exec_())


# if __name__ == '__main__':
#     main()
