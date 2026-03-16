# 우분투 (리눅스 환경)에서 실행되도록

import pyatspi


def extract_ui_elements():

    desktop = pyatspi.Registry.getDesktop(0)

    elements = []

    for app in desktop:
        try:
            for window in app:
                traverse(window, elements)
        except:
            pass

    return elements


def traverse(node, elements):

    try:
        name = node.name if node.name else ""
        role = node.getRoleName()

        parent_name = ""
        try:
            parent = node.parent
            if parent:
                parent_name = parent.name
        except:
            pass

        bbox = None
        center = None

        try:
            component = node.queryComponent()
            x, y, w, h = component.getExtents(pyatspi.DESKTOP_COORDS)

            bbox = (x, y, x + w, y + h)
            center = (x + w // 2, y + h // 2)

        except:
            pass

        elements.append({
            "name": name,
            "control_type": role,
            "parent_name": parent_name,
            "bbox": bbox,
            "center": center
        })

    except:
        pass

    for i in range(node.childCount):
        try:
            child = node.getChildAtIndex(i)
            traverse(child, elements)
        except:
            pass