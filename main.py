import os
import bpy
import requests
from datetime import datetime


def send_request():
    file_path = os.path.join(
        r"D:\Python\AlgousStudio\BlenderButton\SaveProject",
        f"project_{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}.blend"
    )
    bpy.ops.wm.save_as_mainfile(filepath=file_path)

    data = {
#        "time": str(datetime.now()),
        "author": "Aleksey",
        "time_save_project": "2024-09-30T12:00:00Z",
        "path_save_project": file_path
    }
    response = requests.post(
        "http://127.0.0.1:8000/api/blender/save_path/", 
        json=data,
        headers={"Content-Type": "application/json"}
    )


class SimpleOperator(bpy.types.Operator):
    bl_idname = "wm.send_request"
    bl_label = "Отправить запрос"

    def execute(self, context):
        send_request()
        return {'FINISHED'}


class SimplePanel(bpy.types.Panel):
    bl_label = "Кнопка REST API"
    bl_idname = "PT_RestApiButton"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "scene"

    def draw(self, context):
        layout = self.layout
        layout.operator(SimpleOperator.bl_idname)


def register():
    bpy.utils.register_class(SimpleOperator)
    bpy.utils.register_class(SimplePanel)


def unregister():
    bpy.utils.unregister_class(SimplePanel)
    bpy.utils.unregister_class(SimpleOperator)


if __name__ == "__main__":
    register()
