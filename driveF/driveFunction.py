# coding=utf-8
# @FileName      :driveFunction
# @Time          :2023/10/18 21:49
# @Author        :AhrIlI
# @Contact       :906629272@qq.com

import maya.cmds as cmds
from PySide2.QtWidgets import *
from maya.OpenMaya import *

crv_points = [(-0.5, 0.0, 5.551115123125783e-17),
              (-0.5000000000000002, -0.13060193748187082, 1.764511734992259e-17),
              (-0.3918058124456122, -0.39180581244561224, 9.770372818361252e-18),
              (-0.13060193748187082, -0.5000000000000001, 1.975851338064811e-17),
              (0.0, -0.5, 5.551115123125783e-17),
              (0.13060193748187063, -0.5000000000000002, 3.575263785060967e-17),
              (0.39180581244561213, -0.3918058124456124, 5.775274622824593e-17),
              (0.5000000000000001, -0.1306019374818706, 7.887745730729024e-17),
              (0.5, 0.0, 5.551115123125783e-17),
              (0.5000000000000001, 0.13060193748187107, 9.337718511259307e-17),
              (0.39180581244561213, 0.39180581244561247, 1.0125192964415441e-16),
              (0.1306019374818707, 0.5000000000000002, 9.126378908186754e-17),
              (-2.7755575615628914e-17, 0.4999999999999998, 8.326672684688677e-17),
              (-0.13060193748187077, 0.5000000000000001, 7.526966461190597e-17),
              (-0.39180581244561224, 0.39180581244561213, 5.32695562342697e-17),
              (-0.5000000000000002, 0.13060193748187066, 3.214484515522541e-17),
              (-0.5000000000000002, -8.326672684688674e-17, 0.0),
              (-0.5, 7.997062234980793e-18, -0.1306019374818708),
              (-0.39180581244561213, 2.3991186704942356e-17, -0.3918058124456121),
              (-0.1306019374818708, 3.061616997868383e-17, -0.49999999999999994),
              (0.0, 0.0, -0.49999999999999994),
              (0.1306019374818708, 3.0616169978683824e-17, -0.4999999999999999),
              (0.3918058124456125, 2.399118670494234e-17, -0.39180581244561186),
              (0.5000000000000002, 7.997062234980767e-18, -0.13060193748187038),
              (0.5000000000000001, -1.617781153285278e-32, 3.0531133177191805e-16),
              (0.49999999999999994, -7.9970622349808e-18, 0.130601937481871),
              (0.3918058124456119, -2.3991186704942363e-17, 0.39180581244561224),
              (0.13060193748187052, -3.0616169978683836e-17, 0.5000000000000002),
              (0.0, 0.0, 0.5),
              (-5.961562558928949e-17, 0.13060193748187088, 0.5),
              (-1.1098955353675924e-16, 0.39180581244561224, 0.3918058124456121),
              (-1.1901936469749647e-16, 0.5000000000000001, 0.1306019374818706),
              (-1.1102230246251565e-16, 0.5, -9.71445146547012e-17),
              (-1.0302524022753486e-16, 0.5, -0.1306019374818708),
              (-6.30071801268745e-17, 0.39180581244561213, -0.3918058124456121),
              (1.6167143680782006e-18, 0.1306019374818708, -0.49999999999999994),
              (3.0616169978683836e-17, 1.3877787807814457e-17, -0.49999999999999994),
              (5.961562558928947e-17, -0.1306019374818708, -0.4999999999999999),
              (1.1098955353675929e-16, -0.3918058124456125, -0.39180581244561186),
              (1.1901936469749647e-16, -0.5000000000000002, -0.13060193748187038),
              (1.1102230246251565e-16, -0.5000000000000001, 3.0531133177191805e-16),
              (1.0302524022753484e-16, -0.49999999999999994, 0.130601937481871),
              (6.300718012687445e-17, -0.3918058124456119, 0.39180581244561224),
              (-1.6167143680782592e-18, -0.13060193748187052, 0.5000000000000002),
              (-3.0616169978683873e-17, 1.8041124150158794e-16, 0.5),
              (-0.13060193748187088, -3.061616997868383e-17, 0.5),
              (-0.39180581244561224, -2.3991186704942347e-17, 0.3918058124456121),
              (-0.5000000000000001, -7.997062234980776e-18, 0.1306019374818706),
              (-0.5, 8.474091755303838e-33, -9.71445146547012e-17)]
crv_knots = [2.0, 2.0, 2.0, 3.0, 4.0, 4.0, 4.0, 5.0, 6.0, 6.0, 6.0, 7.0, 8.0, 8.0, 8.0, 9.0, 10.0, 10.0, 10.0, 11.0,
             12.0, 12.0, 12.0, 13.0, 14.0, 14.0, 14.0, 15.0, 16.0, 16.0, 16.0, 17.0, 18.0, 18.0, 18.0, 19.0, 20.0, 20.0,
             20.0, 21.0, 22.0, 22.0, 22.0, 23.0, 24.0, 24.0, 24.0, 25.0, 26.0, 26.0, 26.0]
crv_form = 0
crv_degree = 3
crv_color = 22


def setColour(shape, color):
    """
    设置曲线颜色
    :param shape: 曲线的shape
    :param color: overrideColor
    :return:
    """
    cmds.setAttr(shape + ".overrideEnabled", 1)
    cmds.setAttr(shape + ".overrideColor", color)
    return 0


def setShape(crv):
    """
    设置曲线形状
    :param crv: 需要设置的曲线的transform名称
    :return:
    """
    crv_shapes = cmds.listRelatives(crv, s = True)
    if crv_shapes is not None:
        cmds.delete(crv_shapes)
    tmp_crv = cmds.curve(p = crv_points, k = crv_knots, d = crv_degree, per = bool(crv_form))
    new_shape = cmds.listRelatives(tmp_crv, s = 1)[0]
    cmds.parent(new_shape, crv, r = 1, s = 1)
    cmds.delete(tmp_crv)
    new_shape = cmds.rename(new_shape, crv + "Shape")
    setColour(new_shape, crv_color)
    return 0


def softSelectRadius(direction, matrix):
    """
    根据软选择范围的大小确定Loc位置
    :param direction: 朝向
    :param matrix: 骨骼世界矩阵
    :return: 位置坐标
    """
    diameter = cmds.softSelect(q = True, ssd = True) * 2
    direction_point = MPoint(direction[0] * diameter, direction[1] * diameter, direction[2] * diameter) * matrix
    return [direction_point.x, direction_point.y, direction_point.z]


def getPointToMeshClosestPos(mesh, direction, matrix):
    """
    获取射线与模型的交点,MFnMesh.closestIntersection的发射方向向量需为单位向量
    :param mesh: 模型
    :param direction: 发射方向
    :param matrix: 骨骼世界矩阵
    :return: 交点坐标
    """
    dag_path = MDagPath()
    selection = MSelectionList()
    selection.add(mesh)
    selection.getDagPath(0, dag_path)
    mesh_fn = MFnMesh(dag_path)
    msource_ray = MPoint(0.0, 0.0, 0.0) * matrix
    inverse_matrix_list = [1.0, 0.0, 0.0, 0.0,
                           0.0, 1.0, 0.0, 0.0,
                           0.0, 0.0, 1.0, 0.0,
                           -msource_ray.x, -msource_ray.y, -msource_ray.z, 1.0]
    inverse_matrix = MMatrix()
    MScriptUtil.createMatrixFromList(inverse_matrix_list, inverse_matrix)
    mdirection_ray = MPoint(*direction) * matrix * inverse_matrix
    source_ray = MFloatPoint(*msource_ray)
    direction_ray = MFloatVector(mdirection_ray.x, mdirection_ray.y, mdirection_ray.z)
    point_hit = MFloatPoint()
    result = mesh_fn.closestIntersection(source_ray, direction_ray, None, None, None, MSpace.kWorld,
                                         99999, None, None, point_hit, None, None, None, None,
                                         None)
    if result:
        return [point_hit[0], point_hit[1], point_hit[2]]
    else:
        return [source_ray.x, source_ray.y, source_ray.z]


def mirrorLocator(matrix_list):
    """
    获取YZ平面镜像的矩阵数据
    :param matrix_list: 矩阵列表
    :return: 镜像后矩阵列表
    """
    matrix_list[1] = matrix_list[1] * -1.0
    matrix_list[2] = matrix_list[2] * -1.0
    matrix_list[5] = matrix_list[5] * -1.0
    matrix_list[6] = matrix_list[6] * -1.0
    matrix_list[9] = matrix_list[9] * -1.0
    matrix_list[10] = matrix_list[10] * -1.0
    matrix_list[12] = matrix_list[12] * -1.0
    return matrix_list


def createMirrorLocatorFn(locator, locator_grp):
    """
    镜像左边的locator
    :param locator: 需要镜像的locator
    :param locator_grp: 需要添加locator的组
    :return: locator
    """
    matrix = MMatrix()
    MScriptUtil.createMatrixFromList(mirrorLocator(cmds.getAttr(locator + ".worldMatrix[0]")), matrix)
    rot = MTransformationMatrix(matrix).rotation()
    pos = MTransformationMatrix(matrix).translation(MSpace.kWorld)
    left_locator = cmds.spaceLocator(n = locator.replace("_R_", "_L_"))[0]
    get_left_locator_shape = cmds.listRelatives(left_locator, s = True)[0]
    setColour(get_left_locator_shape, 13)
    dag_path = MDagPath()
    selection = MSelectionList()
    selection.add(left_locator)
    selection.getDagPath(0, dag_path)
    transform_fn = MFnTransform(dag_path)
    transform_fn.setTranslation(pos, MSpace.kWorld)
    transform_fn.setRotation(rot, MSpace.kWorld)
    cmds.parent(left_locator, locator_grp)
    if cmds.objExists(locator + ".one"):
        cmds.addAttr(left_locator, ln = "one", at = "bool")
        cmds.setAttr(left_locator + ".one", e = True, cb = True)
        v = cmds.getAttr(locator + ".one")
        cmds.setAttr(left_locator + ".one", v)
    return left_locator


def matrixToList(matrix):
    """
    将MMatrix对象转成4*4的列表
    :param matrix: MMatrix
    :return: matrix_list
    """
    matrix_list = list()
    for i in range(4):
        for o in range(4):
            matrix_list.append(matrix(i, o))
    return matrix_list


def matrixConFun(parent, children, ctype, offset):
    """
    矩阵约束
    :param parent: 约束者(父级)列表
    :param children: 被约束者(子级)列表
    :param ctype: 是否为多对一，True是，False不是
    :param offset: 是否偏移
    :return: 所有的节点
    """
    cmds.undoInfo(ock = True)
    node_name = children[0]
    children_type = cmds.objectType(children[0])
    if ctype:
        offset_v = 1.0 / len(parent)
        pma_matrix = cmds.createNode("plusMinusAverage", n = "{0}_{1}".format(node_name, "PMAmatrix"))
        wt_matrix = cmds.createNode("wtAddMatrix", n = "{0}_{1}".format(node_name, "WTmatrix"))
        dp_matrix = cmds.createNode("decomposeMatrix", n = "{0}_{1}".format(node_name, "DPmatrix"))
        cmds.connectAttr(wt_matrix + ".matrixSum", dp_matrix + ".inputMatrix", f = True)
    for i, par in enumerate(parent):
        if not ctype:
            node_name = children[i]
            children_type = cmds.objectType(children[i])
        m_matrix = cmds.createNode("multMatrix", n = "{0}_{1}_{2}".format(node_name, "Mmatrix", i))
        if not ctype:
            dp_matrix = cmds.createNode("decomposeMatrix", n = "{0}_{1}_{2}".format(node_name, "DPmatrix", i))
            cmds.connectAttr(m_matrix + ".matrixSum", dp_matrix + ".inputMatrix", f = True)
        if ctype:
            attr_name = children[0] + "." + par + "_W"
            cmds.addAttr(children[0], ln = par + "_W", at = "double", min = 0, dv = offset_v)
            cmds.setAttr(attr_name, e = True, k = True)
            cmds.connectAttr(m_matrix + ".matrixSum", wt_matrix + ".wtMatrix[{0}].matrixIn".format(i), f = True)
            cmds.connectAttr(attr_name, pma_matrix + ".input1D[{0}]".format(i), f = True)
            md_matrix = cmds.createNode("multiplyDivide", n = "{0}_{1}_{2}".format(node_name, "MDmatrix", i))
            cmds.setAttr(md_matrix + ".operation", 2)
            cmds.connectAttr(attr_name, md_matrix + ".input1X", f = True)
            cmds.connectAttr(pma_matrix + ".output1D", md_matrix + ".input2X", f = True)
            cmds.connectAttr(md_matrix + ".outputX", wt_matrix + ".wtMatrix[{0}].weightIn".format(i), f = True)
        if offset:
            wmatrix = MMatrix()
            wimatrix = MMatrix()
            MScriptUtil.createMatrixFromList(
                cmds.getAttr(children[0] + ".worldMatrix[0]") if ctype else cmds.getAttr(
                    children[i] + ".worldMatrix[0]"),
                wmatrix)
            MScriptUtil.createMatrixFromList(cmds.getAttr(par + ".worldInverseMatrix[0]"), wimatrix)
            offset_matrix = wmatrix * wimatrix
            offset_matrix = matrixToList(offset_matrix)
            cmds.setAttr(m_matrix + ".matrixIn[0]", offset_matrix, type = "matrix")
        cmds.connectAttr(par + ".worldMatrix[0]", m_matrix + ".matrixIn[1]", f = True)
        if ctype:
            cmds.connectAttr(children[0] + ".parentInverseMatrix[0]", m_matrix + ".matrixIn[2]", f = True)
        else:
            cmds.connectAttr(children[i] + ".parentInverseMatrix[0]", m_matrix + ".matrixIn[2]", f = True)
        if not ctype:
            if children_type == "joint":
                etq_node = cmds.createNode('eulerToQuat', n = '{0}_{1}'.format(node_name, 'ETQ'))
                cmds.connectAttr(children[i] + ".rotateOrder", etq_node + ".inputRotateOrder", f = True)
                cmds.connectAttr(children[i] + ".jointOrient", etq_node + ".inputRotate", f = True)
                qi_node = cmds.createNode('quatInvert', n = '{0}_{1}'.format(node_name, 'QI'))
                cmds.connectAttr(etq_node + ".outputQuat", qi_node + ".inputQuat", f = True)
                qp_node = cmds.createNode('quatProd', n = '{0}_{1}'.format(node_name, 'QP'))
                cmds.connectAttr(qi_node + ".outputQuat", qp_node + ".input2Quat", f = True)
                cmds.connectAttr(dp_matrix + ".outputQuat", qp_node + ".input1Quat", f = True)
                qte_node = cmds.createNode('quatToEuler', n = '{0}_{1}'.format(node_name, 'QTE'))
                cmds.connectAttr(qp_node + ".outputQuat", qte_node + ".inputQuat", f = True)
                cmds.connectAttr(qte_node + ".outputRotate", children[i] + ".rotate", f = True)
                cmds.connectAttr(dp_matrix + ".outputTranslate", children[i] + ".translate", f = True)
                cmds.connectAttr(dp_matrix + ".outputScale", children[i] + ".scale", f = True)
                cmds.connectAttr(children[i] + ".rotateOrder", dp_matrix + ".inputRotateOrder", f = True)
            else:
                cmds.connectAttr(children[i] + ".rotateOrder", dp_matrix + ".inputRotateOrder", f = True)
                cmds.connectAttr(dp_matrix + ".outputTranslate", children[i] + ".translate", f = True)
                cmds.connectAttr(dp_matrix + ".outputRotate", children[i] + ".rotate", f = True)
                cmds.connectAttr(dp_matrix + ".outputScale", children[i] + ".scale", f = True)
    if ctype:
        if children_type == "joint":
            etq_node = cmds.createNode('eulerToQuat', n = '{0}_{1}'.format(node_name, 'ETQ'))
            cmds.connectAttr(children[0] + ".rotateOrder", etq_node + ".inputRotateOrder", f = True)
            cmds.connectAttr(children[0] + ".jointOrient", etq_node + ".inputRotate", f = True)
            qi_node = cmds.createNode('quatInvert', n = '{0}_{1}'.format(node_name, 'QI'))
            cmds.connectAttr(etq_node + ".outputQuat", qi_node + ".inputQuat", f = True)
            qp_node = cmds.createNode('quatProd', n = '{0}_{1}'.format(node_name, 'QP'))
            cmds.connectAttr(qi_node + ".outputQuat", qp_node + ".input2Quat", f = True)
            cmds.connectAttr(dp_matrix + ".outputQuat", qp_node + ".input1Quat", f = True)
            qte_node = cmds.createNode('quatToEuler', n = '{0}_{1}'.format(node_name, 'QTE'))
            cmds.connectAttr(qp_node + ".outputQuat", qte_node + ".inputQuat", f = True)
            cmds.connectAttr(qte_node + ".outputRotate", children[0] + ".rotate", f = True)
            cmds.connectAttr(dp_matrix + ".outputTranslate", children[0] + ".translate", f = True)
            cmds.connectAttr(dp_matrix + ".outputScale", children[0] + ".scale", f = True)
            cmds.connectAttr(children[0] + ".rotateOrder", dp_matrix + ".inputRotateOrder", f = True)
        else:
            cmds.connectAttr(children[0] + ".rotateOrder", dp_matrix + ".inputRotateOrder", f = True)
            cmds.connectAttr(dp_matrix + ".outputTranslate", children[0] + ".translate", f = True)
            cmds.connectAttr(dp_matrix + ".outputRotate", children[0] + ".rotate", f = True)
            cmds.connectAttr(dp_matrix + ".outputScale", children[0] + ".scale", f = True)
    cmds.undoInfo(cck = True)
    if ctype:
        return [dp_matrix]
    else:
        return [m_matrix, dp_matrix]


def disObjConnectAttr(attr):
    """
    断开对象的属性连接
    :param attr: 属性名称
    :return:
    """
    cmds.undoInfo(ock = True)
    destination = cmds.connectionInfo(attr, ged = True)
    if len(destination) == 0:
        attr_list = cmds.listAttr(attr, m = True)
        for at in attr_list:
            destination = cmds.connectionInfo(attr.split(".")[0] + ".{0}".format(at), ged = True)
            src = cmds.connectionInfo(destination, sfd = True)
            cmds.disconnectAttr(src, destination)
    else:
        src = cmds.connectionInfo(destination, sfd = True)
        cmds.disconnectAttr(src, destination)
    cmds.undoInfo(cck = True)


def getTypeObj(pobj, otype):
    """
    获取父级下的所有type的对象
    :param pobj: 父级(列表)
    :param otype: 对象类型
    :return: 
    """
    list_obj = []
    get_listiterator = pobj.__iter__()
    while get_listiterator:
        try:
            obj = get_listiterator.next()
            get_shape = cmds.listRelatives(obj, s = True)
            if get_shape is not None:
                if cmds.objectType(get_shape[0]) == otype:
                    list_obj.append(obj)
            else:
                get_c = cmds.listRelatives(obj, c = True)
                if get_c:
                    for i in getTypeObj(get_c, otype):
                        list_obj.append(i)
        except StopIteration:
            break
    return list_obj


def getSDKNode(obj):
    """
    获取obj的驱动节点
    :param obj: 需要获取的对象
    :return: {属性名:驱动属性}, {属性名:对应的节点}
    """
    get_driven = cmds.setDrivenKeyframe(obj, q = True, dn = True)
    get_driver = {}
    get_node = {}
    for drn in get_driven:
        v = cmds.setDrivenKeyframe(drn, q = True, dr = True)
        get_driver[drn] = v
    for attr in get_driven:
        node = cmds.listConnections(attr)
        get_node[attr] = node[0]
    return [get_driver, get_node]


def deleSDKNode(obj):
    """
    删除SDK相关节点
    :param obj:
    :return:
    """
    cmds.undoInfo(ock = True)
    if cmds.setDrivenKeyframe(obj, q = True, dr = True)[0] != "No drivers.":
        sdk_node = getSDKNode(obj)
        for nr in sdk_node[1]:
            node = sdk_node[1].get(nr)
            if cmds.objectType(node) == "blendWeighted":
                cmds.delete(node)
            elif cmds.objectType(node) == "unitConversion":
                nodes = cmds.listConnections(node + ".input", s = True)
                if cmds.objectType(nodes[0]) == "blendWeighted":
                    cmds.delete(nodes)
                else:
                    dels = cmds.listConnections(nodes + ".input", s = True)
                    cmds.delete(dels)
                    cmds.delete(node)
            else:
                cmds.delete(node)
    cmds.undoInfo(cck = True)


def replaceSkinByJoint(cobj, pocj):
    """
    替换骨骼权重
    :param cobj: 被替换骨骼
    :param pocj: 需要替换骨骼
    :return:
    """
    skin_clusters = []
    skin_clusters_nodes = cmds.ls(type = "skinCluster")
    for node in skin_clusters_nodes:
        influences = cmds.skinCluster(node, query = True, influence = True)
        if cobj in influences:
            skin_clusters.append(node)
    for s in skin_clusters:
        cmds.skinCluster(s, e = True, lw = True, wt = 0, ai = pocj)
        influences = cmds.skinCluster(s, query = True, influence = True)
        for jnt in influences:
            if jnt == cobj or jnt == pocj:
                cmds.setAttr(jnt + ".liw", 0)
            else:
                cmds.setAttr(jnt + ".liw", 1)
        skin_shape = cmds.skinCluster(s, q = True, g = True)[0]
        cmds.skinPercent(s, skin_shape, t = cobj, tv = [(pocj, 1)])
        cmds.skinCluster(s, e = True, ri = cobj)


class DriveFunC:
    """
    具体功能
    """
    suffix = ["_ty_plus", "_ty_minus", "_tz_plus", "_tz_minus"]
    directions = [[0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]
    finger_name = ["ThumbFinger1", "ThumbFinger2", "ThumbFinger3",
                   "IndexFinger1", "IndexFinger2", "IndexFinger3",
                   "MiddleFinger1", "MiddleFinger2", "MiddleFinger3",
                   "RingFinger1", "RingFinger2", "RingFinger3",
                   "PinkyFinger1", "PinkyFinger2", "PinkyFinger3"
                   ]
    con_two_joint = ["Wrist", "Elbow", "Shoulder", "Ankle", "Knee", "Hip"]

    def __init__(self, win_self):
        """

        :param win_self: 窗口
        """
        self.get_win = win_self.findChild(QWidget, "UVDriveTool")
        self.mesh = None
        self.upDate()
        self.re_locator_list = list()
        self.radius = 0.5

    def upDate(self):
        """
        更新，当maya打开新的场景或打开其他文件时更新相关属性
        :return:
        """
        if cmds.objExists("Pos_Locator_Right_Grp"):
            self.all_grp = "ALL_UVDrive_Grp"
            self.pos_locator_grp = "Pos_Locator_Grp"
            self.locator_right_grp = "Pos_Locator_Right_Grp"
            self.locator_right_wrist = "Pos_Locator_Right_Wrist"
            self.locator_right_elbow = "Pos_Locator_Right_Elbow"
            self.locator_right_shoulder = "Pos_Locator_Right_Shoulder"
            self.locator_right_ankle = "Pos_Locator_Right_Ankle"
            self.locator_right_knee = "Pos_Locator_Right_Knee"
            self.locator_right_hip = "Pos_Locator_Right_Hip"
            self.locator_right_finger = "Pos_Locator_Right_Finger"
            self.locator_left_grp = "Pos_Locator_Left_Grp"
            self.locator_left_wrist = "Pos_Locator_Left_Wrist"
            self.locator_left_elbow = "Pos_Locator_Left_Elbow"
            self.locator_left_shoulder = "Pos_Locator_Left_Shoulder"
            self.locator_left_ankle = "Pos_Locator_Left_Ankle"
            self.locator_left_knee = "Pos_Locator_Left_Knee"
            self.locator_left_hip = "Pos_Locator_Left_Hip"
            self.locator_left_finger = "Pos_Locator_Left_Finger"
            self.all_right_locator_grp = [self.locator_right_wrist, self.locator_right_elbow,
                                          self.locator_right_shoulder,
                                          self.locator_right_ankle, self.locator_right_knee, self.locator_right_hip,
                                          self.locator_right_finger]
            self.all_left_locator_grp = [self.locator_left_wrist, self.locator_left_elbow, self.locator_left_shoulder,
                                         self.locator_left_ankle, self.locator_left_knee, self.locator_left_hip,
                                         self.locator_left_finger]
        if cmds.objExists("ALL_UVDrive_Control_Grp"):
            self.control_right_wrist = "UVDrive_Control_Right_Wrist"
            self.control_right_elbow = "UVDrive_Control_Right_Elbow"
            self.control_right_shoulder = "UVDrive_Control_Right_Shoulder"
            self.control_right_ankle = "UVDrive_Control_Right_Ankle"
            self.control_right_knee = "UVDrive_Control_Right_Knee"
            self.control_right_hip = "UVDrive_Control_Right_Hip"
            self.control_right_finger = "UVDrive_Control_Right_Finger"
            self.all_right_control_grp = [self.control_right_wrist, self.control_right_elbow,
                                          self.control_right_shoulder,
                                          self.control_right_ankle, self.control_right_knee, self.control_right_hip,
                                          self.control_right_finger]
            self.control_left_wrist = "UVDrive_Control_Left_Wrist"
            self.control_left_elbow = "UVDrive_Control_Left_Elbow"
            self.control_left_shoulder = "UVDrive_Control_Left_Shoulder"
            self.control_left_ankle = "UVDrive_Control_Left_Ankle"
            self.control_left_knee = "UVDrive_Control_Left_Knee"
            self.control_left_hip = "UVDrive_Control_Left_Hip"
            self.control_left_finger = "UVDrive_Control_Left_Finger"
            self.all_left_control_grp = [self.control_left_wrist, self.control_left_elbow,
                                         self.control_left_shoulder,
                                         self.control_left_ankle, self.control_left_knee, self.control_left_hip,
                                         self.control_left_finger]
            self.drive_all = "ALL_UVDrive_DriveSy_Grp"
            self.drive_right = "ALL_UVDrive_DriveSy_Right_Grp"
            self.drive_left = "ALL_UVDrive_DriveSy_Left_Grp"
            self.drive_other = "ALL_UVDrive_DriveSy_Other_Grp"

    def reDelete(self):
        """
        删除除用于重建的对象
        :return: 驱动关键帧
        """
        cmds.undoInfo(ock = True)
        sdk = []
        for r, l in zip(self.all_right_control_grp, self.all_left_control_grp):
            get_rc = getTypeObj([r], "nurbsCurve")
            get_lc = getTypeObj([l], "nurbsCurve")
            for rc, lc in zip(get_rc, get_lc):
                sdk_grp_r = cmds.listRelatives(rc, p = True)[0]
                sdk_grp_l = cmds.listRelatives(lc, p = True)[0]
                if cmds.objExists(rc.replace("Control", "PosLoc")):
                    if cmds.setDrivenKeyframe(sdk_grp_r, q = True, dr = True)[0] != "No drivers.":
                        sdk_node_r = getSDKNode(sdk_grp_r)
                        sdk.append(sdk_node_r)
                        for nr in sdk_node_r[1]:
                            disObjConnectAttr(nr)
                else:
                    deleSDKNode(sdk_grp_r)
                if cmds.objExists(lc.replace("Control", "PosLoc")):
                    if cmds.setDrivenKeyframe(sdk_grp_l, q = True, dr = True)[0] != "No drivers.":
                        sdk_node_l = getSDKNode(sdk_grp_l)
                        sdk.append(sdk_node_l)
                        for nl in sdk_node_l[1]:
                            disObjConnectAttr(nl)
                else:
                    deleSDKNode(sdk_grp_l)
                get_rnode = cmds.ls(rc.replace("Control", "Jnt") + "*")[1:]
                cmds.delete(get_rnode)
                get_lnode = cmds.ls(lc.replace("Control", "Jnt") + "*")[1:]
                cmds.delete(get_lnode)
            get_all_node = cmds.ls(r + "*") + cmds.ls(l + "*")
            cmds.delete(get_all_node)
        driver_grp = cmds.listRelatives(self.drive_right, c = True)
        drivel_grp = cmds.listRelatives(self.drive_left, c = True)
        for loc in self.all_right_locator_grp:
            is_none = cmds.listRelatives(loc, c = True)
            if is_none is None:
                jnt = loc.split("_")[-1]
                for grpr, grpl in zip(driver_grp, drivel_grp):
                    if jnt in grpr:
                        sph_r = cmds.listRelatives(grpr, c = True)[0]
                        sph_l = cmds.listRelatives(grpl, c = True)[0]
                        get_rsphnode = cmds.ls(sph_r + "*")
                        get_lsphnode = cmds.ls(sph_l + "*")
                        cmds.delete(get_rsphnode)
                        cmds.delete(get_lsphnode)
                        cmds.deleteAttr(jnt + "_R.dU")
                        cmds.deleteAttr(jnt + "_R.dV")
                        cmds.deleteAttr(jnt + "_L.dU")
                        cmds.deleteAttr(jnt + "_L.dV")
                        cmds.delete(grpr)
                        cmds.delete(grpl)
        cmds.undoInfo(cck = True)
        return sdk

    def addLocatorAttr(self, loc):
        """
        给Locator添加属性“one”(类型为布尔)，用来确定是否使用一个骨骼来进行约束
        :param loc: 需要添加的Locator
        :return:
        """
        if not cmds.objExists(loc + ".one"):
            cmds.addAttr(loc, ln = "one", at = "bool")
            cmds.setAttr(loc + ".one", e = True, cb = True)
            cmds.setAttr(loc + ".one", 1)

    def getJoint(self):
        """
        获取创建出来的骨骼
        :return: 所有骨骼
        """
        # all_joint = []
        # for r, l in zip(self.all_right_control_grp, self.all_left_control_grp):
        #     get_rc = getTypeObj([r], "nurbsCurve")
        #     get_lc = getTypeObj([l], "nurbsCurve")
        #     for rc, lc in zip(get_rc, get_lc):
        #         rjnt = rc.replace("Control", "Jnt")
        #         ljnt = lc.replace("Control", "Jnt")
        #         all_joint.append(rjnt)
        #         all_joint.append(ljnt)
        # return all_joint
        select_list = []
        for j in cmds.ls(type = "joint"):
            if cmds.objExists("{0}.uvt".format(j)):
                select_list.append(j)
        cmds.select(select_list)
        return select_list

    def createTransform(self, create_joint_list):
        """
        创建所需的组和定位器，确定骨骼位置
        :param create_joint_list: 需要创建的骨骼
        :return:
        """
        cmds.undoInfo(ock = True)
        if cmds.objExists("FitSkeleton"):
            pass
        else:
            return cmds.warning(u"找不到FitSkeleton曲线，请检查ADV绑定系统是否完整")
        if not cmds.objExists("ALL_UVDrive_Grp"):
            self.all_grp = cmds.createNode("transform", n = "ALL_UVDrive_Grp")
            self.pos_locator_grp = cmds.createNode("transform", n = "Pos_Locator_Grp")
            self.locator_right_grp = cmds.createNode("transform", n = "Pos_Locator_Right_Grp")
            self.locator_right_wrist = cmds.createNode("transform", n = "Pos_Locator_Right_Wrist")
            self.locator_right_elbow = cmds.createNode("transform", n = "Pos_Locator_Right_Elbow")
            self.locator_right_shoulder = cmds.createNode("transform", n = "Pos_Locator_Right_Shoulder")
            self.locator_right_ankle = cmds.createNode("transform", n = "Pos_Locator_Right_Ankle")
            self.locator_right_knee = cmds.createNode("transform", n = "Pos_Locator_Right_Knee")
            self.locator_right_hip = cmds.createNode("transform", n = "Pos_Locator_Right_Hip")
            self.locator_right_finger = cmds.createNode("transform", n = "Pos_Locator_Right_Finger")
            self.locator_left_grp = cmds.createNode("transform", n = "Pos_Locator_Left_Grp")
            self.locator_left_wrist = cmds.createNode("transform", n = "Pos_Locator_Left_Wrist")
            self.locator_left_elbow = cmds.createNode("transform", n = "Pos_Locator_Left_Elbow")
            self.locator_left_shoulder = cmds.createNode("transform", n = "Pos_Locator_Left_Shoulder")
            self.locator_left_ankle = cmds.createNode("transform", n = "Pos_Locator_Left_Ankle")
            self.locator_left_knee = cmds.createNode("transform", n = "Pos_Locator_Left_Knee")
            self.locator_left_hip = cmds.createNode("transform", n = "Pos_Locator_Left_Hip")
            self.locator_left_finger = cmds.createNode("transform", n = "Pos_Locator_Left_Finger")
            cmds.parent(self.pos_locator_grp, self.all_grp)
            cmds.parent(self.locator_right_grp, self.pos_locator_grp)
            self.all_right_locator_grp = [self.locator_right_wrist, self.locator_right_elbow,
                                          self.locator_right_shoulder,
                                          self.locator_right_ankle, self.locator_right_knee, self.locator_right_hip,
                                          self.locator_right_finger]
            cmds.parent(self.all_right_locator_grp, self.locator_right_grp)
            cmds.parent(self.locator_left_grp, self.pos_locator_grp)
            self.all_left_locator_grp = [self.locator_left_wrist, self.locator_left_elbow, self.locator_left_shoulder,
                                         self.locator_left_ankle, self.locator_left_knee, self.locator_left_hip,
                                         self.locator_left_finger]
            cmds.parent(self.all_left_locator_grp, self.locator_left_grp)
        for jnt in create_joint_list:
            if "Finger" in jnt:
                for f in self.finger_name:
                    f = f + "_R"
                    for direction in self.directions[2:]:
                        loc = self._createPosLocator(f, direction, self.directions.index(direction))
                        if loc:
                            cmds.parent(loc, self.locator_right_finger)
                break
            for i, direction in enumerate(self.directions):
                loc = self._createPosLocator(jnt, direction, i)
                if loc:
                    get_joint_name = jnt.split("_")[0]
                    for index, n in enumerate(self.all_right_locator_grp):
                        if get_joint_name in n:
                            cmds.parent(loc, self.all_right_locator_grp[index])
                if jnt in ["Elbow_R", "Knee_R"] and i == 1:
                    break
        if len(self.re_locator_list) != 0:
            cmds.warning(self.re_locator_list)
            self.re_locator_list = []
        cmds.select(cl = True)
        cmds.undoInfo(cck = True)

    def createSelectJointLocator(self, joint, drive_jnt, direction_tf, re_locator):
        """
        根据所选骨骼创建locator
        :param joint: 所选择的骨骼
        :param drive_jnt: 驱动的骨骼
        :param direction_tf: 确定要创建的方向
        :param re_locator: 重复的locator
        :return: locator名称
        """
        cmds.undoInfo(ock = True)
        joint_list = list()
        for i, direction in enumerate(direction_tf):
            if direction:
                loc = self._createPosLocator(joint, self.directions[i], i)
                if loc:
                    joint_list.append(loc)
        if len(joint_list) != 0:
            get_joint_name = drive_jnt.split("_")[0]
            locator_grp = [grp for grp in self.all_right_locator_grp if get_joint_name in grp][0]
            cmds.parent(joint_list, locator_grp)
        if len(self.re_locator_list) != 0:
            re_locator.extend(self.re_locator_list)
            self.re_locator_list = []
        cmds.undoInfo(cck = True)
        return joint_list

    def _createPosLocator(self, joint, direction, i):
        """
        创建定位器
        :param joint: 需要创建的骨骼
        :param direction: Loc方向
        :return: Locator
        """
        cmds.undoInfo(ock = True)
        joint_name = joint
        if "_M" in joint_name:
            joint_name = joint.replace("_M", "_R")
        if cmds.objExists(joint_name + self.suffix[i] + "_PosLoc"):
            self.re_locator_list.append(u"已经存在" + joint_name + self.suffix[i] + "_PosLoc")
            return 0
        matrix = MMatrix()
        matrix_value = cmds.xform(joint, q = True, ws = True, m = True)
        MScriptUtil.createMatrixFromList(matrix_value, matrix)
        if self.mesh is None:
            post = softSelectRadius(direction, matrix)
        else:
            post = getPointToMeshClosestPos(self.mesh, direction, matrix)
        loc = cmds.spaceLocator(n = "{0}{1}_PosLoc".format(joint_name, self.suffix[i]))[0]
        cmds.xform(loc, ws = True, t = post)
        cmds.matchTransform(loc, joint, rot = True)
        get_shape = cmds.listRelatives(loc, s = True)[0]
        setColour(get_shape, 17)
        cmds.undoInfo(cck = True)
        return loc

    def createMirrorLocator(self):
        """
        镜像左边的locator
        :return:
        """
        cmds.undoInfo(ock = True)
        for left in self.all_left_locator_grp:
            locator_left_list = cmds.listRelatives(left, c = True)
            if locator_left_list is not None:
                cmds.delete(locator_left_list)
        for right in self.all_right_locator_grp:
            locator_right_list = cmds.listRelatives(right, c = True)
            if locator_right_list is not None:
                for loc in locator_right_list:
                    get_shape = cmds.listRelatives(loc, s = True)
                    locator_grp = right.replace("Right", "Left")
                    if cmds.objectType(get_shape[0]) == "locator":
                        createMirrorLocatorFn(loc, locator_grp)
        cmds.undoInfo(cck = True)

    def createDriveSystem(self):
        """
        构建驱动系统(创建控制器与骨骼，创建驱动，设置驱动关键帧)
        :return:
        """
        cmds.undoInfo(ock = True)
        self._createControlHierarchy()
        self._createDriveCommand()
        cmds.setAttr(self.pos_locator_grp + ".visibility", 0)
        cmds.undoInfo(cck = True)

    def _createControlHierarchy(self):
        """
        创建控制器相关的层级，和根据locator创建控制器和骨骼
        :return: 0
        """
        cmds.undoInfo(ock = True)
        re_true = cmds.objExists("ALL_UVDrive_Control_Grp")
        if not re_true:
            self.uvdrive_ctrl_all = cmds.createNode("transform", n = "ALL_UVDrive_Control_Grp")
            right_control = cmds.createNode("transform", n = "UVDrive_Control_Grp_R")
            left_control = cmds.createNode("transform", n = "UVDrive_Control_Grp_L")
            cmds.parent(self.uvdrive_ctrl_all, self.all_grp)
            cmds.parent(right_control, self.uvdrive_ctrl_all)
            cmds.parent(left_control, self.uvdrive_ctrl_all)
        else:
            right_control = "UVDrive_Control_Grp_R"
            left_control = "UVDrive_Control_Grp_L"
        self.control_right_wrist = cmds.createNode("transform", n = "UVDrive_Control_Right_Wrist")
        self.control_right_elbow = cmds.createNode("transform", n = "UVDrive_Control_Right_Elbow")
        self.control_right_shoulder = cmds.createNode("transform", n = "UVDrive_Control_Right_Shoulder")
        self.control_right_ankle = cmds.createNode("transform", n = "UVDrive_Control_Right_Ankle")
        self.control_right_knee = cmds.createNode("transform", n = "UVDrive_Control_Right_Knee")
        self.control_right_hip = cmds.createNode("transform", n = "UVDrive_Control_Right_Hip")
        self.control_right_finger = cmds.createNode("transform", n = "UVDrive_Control_Right_Finger")
        self.all_right_control_grp = [self.control_right_wrist, self.control_right_elbow,
                                      self.control_right_shoulder,
                                      self.control_right_ankle, self.control_right_knee, self.control_right_hip,
                                      self.control_right_finger]
        self.control_left_wrist = cmds.createNode("transform", n = "UVDrive_Control_Left_Wrist")
        self.control_left_elbow = cmds.createNode("transform", n = "UVDrive_Control_Left_Elbow")
        self.control_left_shoulder = cmds.createNode("transform", n = "UVDrive_Control_Left_Shoulder")
        self.control_left_ankle = cmds.createNode("transform", n = "UVDrive_Control_Left_Ankle")
        self.control_left_knee = cmds.createNode("transform", n = "UVDrive_Control_Left_Knee")
        self.control_left_hip = cmds.createNode("transform", n = "UVDrive_Control_Left_Hip")
        self.control_left_finger = cmds.createNode("transform", n = "UVDrive_Control_Left_Finger")
        self.all_left_control_grp = [self.control_left_wrist, self.control_left_elbow,
                                     self.control_left_shoulder,
                                     self.control_left_ankle, self.control_left_knee, self.control_left_hip,
                                     self.control_left_finger]
        cmds.parent(self.all_right_control_grp, right_control)
        cmds.parent(self.all_left_control_grp, left_control)
        if not re_true:
            cmds.connectAttr("MainScaleMultiplyDivide.output", self.uvdrive_ctrl_all + ".scale", f = True)
        for index in range(len(self.all_right_locator_grp)):
            right_loc = cmds.listRelatives(self.all_right_locator_grp[index], c = True)
            left_loc = cmds.listRelatives(self.all_left_locator_grp[index], c = True)
            if right_loc is not None:
                for r, l in zip(right_loc, left_loc):
                    parent_joint = r.split("_")[0]
                    two = True if parent_joint in self.con_two_joint or parent_joint in self.finger_name else False
                    r_two = two
                    l_two = two
                    if cmds.objExists(r + ".one"):
                        if cmds.getAttr(r + ".one"):
                            r_two = False
                    if cmds.objExists(l + ".one"):
                        if cmds.getAttr(l + ".one"):
                            l_two = False
                    right_con_joint = self._createControlAndJoint(r, r_two)
                    left_con_joint = self._createControlAndJoint(l, l_two)
                    get_p_r = cmds.listRelatives(right_con_joint[0], p = True)
                    get_p_l = cmds.listRelatives(left_con_joint[0], p = True)
                    if get_p_r is None:
                        cmds.parent(right_con_joint[0], self.all_right_control_grp[index])
                    if get_p_l is None:
                        cmds.parent(left_con_joint[0], self.all_left_control_grp[index])
                    try:
                        cmds.parent(right_con_joint[1], right_con_joint[2])
                        cmds.parent(left_con_joint[1], left_con_joint[2])
                    except RuntimeError:
                        pass
        cmds.undoInfo(cck = True)
        return 0

    def _createControlAndJoint(self, locator, two):
        """
        创建控制器和骨骼以及被骨骼约束
        :param locator: 需要创建控制器的locator
        :param two: 是否两个骨骼约束offset组
        :return: 控制器,骨骼,约束骨骼,约束节点
        """
        cmds.undoInfo(ock = True)
        cmds.refresh()
        parent_joint = locator.split("_")[0] + "_M"
        if cmds.objExists(parent_joint):
            pass
        else:
            parent_joint = "_".join(locator.split("_")[:2])
        if two:
            second_joint = cmds.listRelatives(parent_joint, p = True)[0]
        name_get = locator.replace("PosLoc", "Control")
        transform_con = cmds.createNode("transform", n = name_get)
        transform_offset = cmds.createNode("transform", n = name_get + "_Offset")
        transform_grp = cmds.createNode("transform", n = name_get + "_Grp")
        cmds.parent(transform_con, transform_offset)
        cmds.parent(transform_offset, transform_grp)
        setShape(transform_con)
        cmds.matchTransform(transform_grp, locator, pos = True, rot = True)
        cmds.select(cl = True)
        joint_name = locator.replace("PosLoc", "Jnt")
        if not cmds.objExists(joint_name):
            skin_joint = cmds.joint(n = joint_name)
            cmds.addAttr(skin_joint, ln = "uvt", at = "message")
            cmds.matchTransform(skin_joint, locator, pos = True, rot = True)
            cmds.makeIdentity(skin_joint, a = True, r = True)
            cmds.setAttr(skin_joint + ".segmentScaleCompensate", 0)
            matrixConFun([transform_con], [skin_joint], False, True)
        else:
            matrixConFun([transform_con], [joint_name], False, True)
        constrain_joint = [second_joint, parent_joint] if two else [parent_joint]
        matrix_con = transform_grp
        if two:
            if cmds.objExists(second_joint.split("_")[0] + parent_joint + "_Constrains_Grp"):
                parent_grp = second_joint.split("_")[0] + parent_joint + "_Constrains_Grp"
                cmds.parent(transform_grp, parent_grp)
                matrix_con = parent_grp
            else:
                parent_grp = cmds.createNode("transform",
                                             n = second_joint.split("_")[0] + parent_joint + "_Constrains_Grp")
                cmds.matchTransform(parent_grp, parent_joint, pos = True, rot = True)
                cmds.parent(transform_grp, parent_grp)
                matrix_con = parent_grp
                node = matrixConFun(constrain_joint, [matrix_con], two, True)
                cmds.disconnectAttr(node[0] + ".outputScale", parent_grp + ".scale")
                md_node1 = cmds.createNode("multiplyDivide", n = "{0}_{1}".format(parent_grp, "MD01"))
                md_node2 = cmds.createNode("multiplyDivide", n = "{0}_{1}".format(parent_grp, "MD02"))
                plus_node = cmds.createNode("plusMinusAverage", n = "{0}_{1}".format(parent_grp, "PMA"))
                cmds.connectAttr(second_joint + ".scale", md_node1 + ".input1", f = True)
                cmds.connectAttr(parent_joint + ".scale", md_node2 + ".input1", f = True)
                cmds.setAttr(md_node1 + ".input2X", 0.5)
                cmds.setAttr(md_node1 + ".input2Y", 0.5)
                cmds.setAttr(md_node1 + ".input2Z", 0.5)
                cmds.setAttr(md_node2 + ".input2X", 0.5)
                cmds.setAttr(md_node2 + ".input2Y", 0.5)
                cmds.setAttr(md_node2 + ".input2Z", 0.5)
                cmds.connectAttr(md_node1 + ".output", plus_node + ".input3D[0]", f = True)
                cmds.connectAttr(md_node2 + ".output", plus_node + ".input3D[1]", f = True)
                cmds.connectAttr(plus_node + ".output3D", parent_grp + ".scale", f = True)

        else:
            matrixConFun(constrain_joint, [matrix_con], two, True)
        cmds.undoInfo(cck = True)
        return [matrix_con, joint_name, parent_joint]

    def _createDriveCommand(self):
        """
        创建驱动
        :return:
        """
        cmds.undoInfo(ock = True)
        if not cmds.objExists("ALL_UVDrive_DriveSy_Grp"):
            self.drive_all = cmds.createNode("transform", n = "ALL_UVDrive_DriveSy_Grp")
            self.drive_right = cmds.createNode("transform", n = "ALL_UVDrive_DriveSy_Right_Grp")
            self.drive_left = cmds.createNode("transform", n = "ALL_UVDrive_DriveSy_Left_Grp")
            self.drive_other = cmds.createNode("transform", n = "ALL_UVDrive_DriveSy_Other_Grp")
            cmds.parent(self.drive_all, self.all_grp)
            cmds.parent(self.drive_right, self.drive_all)
            cmds.parent(self.drive_left, self.drive_all)
            cmds.parent(self.drive_other, self.drive_all)
        right_d_joint = list()
        left_d_joint = list()
        for r, l in zip(self.all_right_control_grp, self.all_left_control_grp):
            right_cons = cmds.listRelatives(r, c = True)
            left_cons = cmds.listRelatives(l, c = True)
            if right_cons is not None:
                right_d_joint.append(r.split("_")[-1])
            if left_cons is not None:
                left_d_joint.append(l.split("_")[-1])
        for rjnt in right_d_joint:
            if "Finger" in rjnt:
                continue
            if cmds.objExists(rjnt + "_R.dU"):
                continue
            if not cmds.objExists("UVDrive_{0}Sphere_Right".format(rjnt)):
                sphere_grp = cmds.createNode("transform", n = "UVDrive_{0}Sphere_Right".format(rjnt))
                spheres = self._createDriveFn(rjnt + "_R")
                cmds.parent(spheres, sphere_grp)
                cmds.parent(sphere_grp, self.drive_right)
        for ljnt in left_d_joint:
            if "Finger" in ljnt:
                continue
            if cmds.objExists(ljnt + "_L.dU"):
                continue
            if not cmds.objExists("UVDrive_{0}Sphere_Left".format(ljnt)):
                sphere_grp = cmds.createNode("transform", n = "UVDrive_{0}Sphere_Left".format(ljnt))
                spheres = self._createDriveFn(ljnt + "_L")
                cmds.parent(spheres, sphere_grp)
                cmds.parent(sphere_grp, self.drive_left)
        cmds.setAttr(self.drive_all + ".visibility", 0)
        cmds.undoInfo(cck = True)

    def _createDriveFn(self, joint):
        """
        根据骨骼构建驱动(不包括手指骨骼)
        :param joint: 骨骼
        :return: 
        """
        cmds.undoInfo(ock = True)
        parent_joint = cmds.listRelatives(joint, p = True)[0]
        cmds.addAttr(joint, ln = "dU", at = "double", dv = 0)
        cmds.addAttr(joint, ln = "dV", at = "double", dv = 0)
        cmds.setAttr(joint + ".dU", k = True)
        cmds.setAttr(joint + ".dV", k = True)
        spheres = cmds.sphere(p = [-1, 0, 0], ax = [0, 1, 0], ssw = -90, esw = 90, r = 1, d = 3, ut = 0, tol = 0.01,
                              s = 10, nsp = 10, ch = 0, n = "UVD_Sphere_{0}".format(joint))[0]
        sphere_shape = cmds.listRelatives(spheres, s = True)[0]
        cmds.matchTransform(spheres, joint, pos = True, rot = True)
        uv_get_node = cmds.createNode("closestPointOnSurface", n = "{0}_CPOSF".format(spheres))
        cm_node = cmds.createNode("composeMatrix", n = "{0}_CMmatrix".format(spheres))
        mm_node = cmds.createNode("multMatrix", n = "{0}_Mmatrix".format(spheres))
        dp_node = cmds.createNode("decomposeMatrix", n = "{0}_DPmatrix".format(spheres))
        set_node = cmds.createNode("setRange", n = "{0}_setR".format(spheres))
        cmds.connectAttr(sphere_shape + ".worldSpace[0]", uv_get_node + ".inputSurface", f = True)
        cmds.connectAttr(cm_node + ".outputMatrix", mm_node + ".matrixIn[0]", f = True)
        cmds.connectAttr(joint + ".worldMatrix[0]", mm_node + ".matrixIn[1]", f = True)
        cmds.connectAttr(mm_node + ".matrixSum", dp_node + ".inputMatrix", f = True)
        cmds.connectAttr(dp_node + ".outputTranslate", uv_get_node + ".inPosition", f = True)
        cmds.setAttr(cm_node + ".inputTranslateX", 1)
        cmds.connectAttr(uv_get_node + ".parameterU", set_node + ".valueX", f = True)
        cmds.connectAttr(uv_get_node + ".parameterV", set_node + ".valueY", f = True)
        cmds.setAttr(set_node + ".minX", -1)
        cmds.setAttr(set_node + ".minY", -1)
        cmds.setAttr(set_node + ".maxX", 1)
        cmds.setAttr(set_node + ".maxY", 1)
        cmds.setAttr(set_node + ".oldMaxX", 10)
        cmds.setAttr(set_node + ".oldMaxY", 10)
        cmds.connectAttr(set_node + ".outValueX", joint + ".dU", f = True)
        cmds.connectAttr(set_node + ".outValueY", joint + ".dV", f = True)
        joint_matrix_node = matrixConFun([joint], [spheres], False, True)
        cmds.disconnectAttr(joint_matrix_node[1] + ".outputTranslate", spheres + ".translate")
        cmds.disconnectAttr(joint_matrix_node[1] + ".outputRotate", spheres + ".rotate")
        cmds.disconnectAttr(joint_matrix_node[1] + ".outputScale", spheres + ".scale")
        parent_matrix_node = matrixConFun([parent_joint], [spheres], False, True)
        cmds.disconnectAttr(parent_matrix_node[1] + ".outputTranslate", spheres + ".translate")
        cmds.disconnectAttr(parent_matrix_node[1] + ".outputScale", spheres + ".scale")
        cmds.connectAttr(joint_matrix_node[1] + ".outputTranslate", spheres + ".translate")
        cmds.connectAttr(joint_matrix_node[1] + ".outputScale", spheres + ".scale")
        cmds.undoInfo(cck = True)
        return spheres

    def reBuild(self):
        """
        重建驱动系统(删除之前的控制系统，保留骨骼权重再重建控制系统替换权重)
        :return:
        """
        cmds.undoInfo(ock = True)
        all_joint = self.getJoint()
        delete_joint = []
        replace_joint = []
        for jnt in all_joint:
            disObjConnectAttr(jnt + ".t")
            disObjConnectAttr(jnt + ".r")
            disObjConnectAttr(jnt + ".s")
            loc = jnt.replace("Jnt", "PosLoc")
            if not cmds.objExists(loc):
                delete_joint.append(jnt)
            else:
                jnt_pos = [round(num, 3) for num in cmds.xform(jnt, q = True, ws = True, t = True)]
                loc_pos = [round(num, 3) for num in cmds.xform(loc, q = True, ws = True, t = True)]
                if jnt_pos != loc_pos:
                    true_name = "prefix_" + jnt
                    replace_joint.append(true_name)
                    cmds.rename(jnt, true_name)
                    delete_joint.append(true_name)
        sdk = self.reDelete()
        self.createDriveSystem()
        for s in sdk:
            for index in range(len(s)):
                if index == 0:
                    continue
                else:
                    for attr in s[index]:
                        node = s[index].get(attr)
                        cmds.connectAttr(node + ".output", attr)
        for j in replace_joint:
            new_j = j.replace("prefix_", "")
            if cmds.objExists(new_j):
                replaceSkinByJoint(j, new_j)
        cmds.delete(delete_joint)
        cmds.setAttr("ALL_UVDrive_Control_Grp.visibility", 1)
        cmds.undoInfo(cck = True)
        return replace_joint

    def addDriveFn(self, joint):
        """
        添加驱动
        :param joint: 需要添加驱动的骨骼
        :return:
        """
        cmds.undoInfo(ock = True)
        sphere_grp = cmds.createNode("transform", n = "UVDrive_{0}Sphere_Other".format(joint))
        sphere = self._createDriveFn(joint)
        cmds.parent(sphere_grp, self.drive_other)
        cmds.parent(sphere, sphere_grp)
        cmds.undoInfo(cck = True)

    def deleteDrivenFn(self, joint):
        """
        删除所选骨骼的驱动
        :param joint: 所选骨骼
        :return:
        """
        cmds.undoInfo(ock = True)
        grp = cmds.listRelatives(self.drive_other, c = True)
        for g in grp:
            if joint in g:
                sph = cmds.listRelatives(g, c = True)[0]
                get_sphnode = cmds.ls(sph + "*")
                cmds.delete(get_sphnode)
                cmds.deleteAttr(joint + ".dU")
                cmds.deleteAttr(joint + ".dV")
                cmds.delete(g)
        cmds.undoInfo(cck = True)

    def setDrivenKeyByCon(self, control, attr):
        """
        选择控制器设置驱动关键帧
        :param control: 控制器
        :param attr: 驱动属性
        :return:
        """
        cmds.undoInfo(ock = True)
        for c in control:
            offset = cmds.listRelatives(c, p = True)[0]
            matrix = MMatrix()
            MScriptUtil.createMatrixFromList(cmds.getAttr(c + ".worldMatrix[0]"), matrix)
            rot = MTransformationMatrix(matrix).rotation()
            pos = MTransformationMatrix(matrix).translation(MSpace.kWorld)
            dag_path = MDagPath()
            selection = MSelectionList()
            selection.add(offset)
            selection.getDagPath(0, dag_path)
            transform_fn = MFnTransform(dag_path)
            transform_fn.setTranslation(pos, MSpace.kWorld)
            transform_fn.setRotation(rot, MSpace.kWorld)
            s = cmds.getAttr(c + ".s")[0]
            cmds.setAttr(offset + ".s", s[0], s[1], s[2])
            cmds.setAttr(c + ".t", 0, 0, 0)
            cmds.setAttr(c + ".r", 0, 0, 0)
            cmds.setAttr(c + ".s", 1, 1, 1)
            cmds.setDrivenKeyframe(offset + ".tx", currentDriver = attr)
            cmds.setDrivenKeyframe(offset + ".ty", currentDriver = attr)
            cmds.setDrivenKeyframe(offset + ".tz", currentDriver = attr)
            cmds.setDrivenKeyframe(offset + ".rx", currentDriver = attr)
            cmds.setDrivenKeyframe(offset + ".ry", currentDriver = attr)
            cmds.setDrivenKeyframe(offset + ".rz", currentDriver = attr)
            cmds.setDrivenKeyframe(offset + ".sx", currentDriver = attr)
            cmds.setDrivenKeyframe(offset + ".sy", currentDriver = attr)
            cmds.setDrivenKeyframe(offset + ".sz", currentDriver = attr)
        cmds.undoInfo(cck = True)

    def mirrorSDK(self, lorr):
        """
        镜像SDK
        :param lorr: True右到左，False左到右
        :return:
        """
        cmds.undoInfo(ock = True)
        if lorr:
            cop = self.locator_right_grp
            # pas = self.locator_left_grp
        else:
            cop = self.locator_left_grp
            # pas = self.locator_right_grp
        for cp in cmds.listRelatives(cop, c = True):
            for l in cmds.listRelatives(cp, c = True):
                offset = l.replace()
                sdk_node = getSDKNode(offset)
        cmds.undoInfo(cck = True)
