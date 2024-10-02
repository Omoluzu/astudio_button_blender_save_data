import os
import bpy
import requests
from datetime import datetime

USERNAME = "Aleksey Volkov"
BASE_PATH_SAVE_PROJECT = r"D:\Python\AlgousStudio\BlenderButton\SaveProject"
URL = "http://127.0.0.1:8000"

URL_POST_REQUEST_SAVE_DATA_PROJECT = "{}/api/blender/save_path/".format(URL)


def get_path_project() -> str:
    """
    Get project path save
    :return: path
    """
    blend_file_path = bpy.data.filepath
    project_name = os.path.splitext(
        os.path.basename(blend_file_path)
    )[0].split('__')[0]

    return os.path.join(
        BASE_PATH_SAVE_PROJECT,
        "{}__{}.blend".format(
            project_name or 'project',
            datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        )
    )


def send_request(file_path: str) -> None:
    """
    Submit a request to save project data
    :param file_path: Path project save
    """
    data = {
        "author": USERNAME,
        "time_save_project": datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ'),
        "path_save_project": file_path
    }
    
    requests.post(
        URL_POST_REQUEST_SAVE_DATA_PROJECT,
        json=data,
        headers={"Content-Type": "application/json"}
    )


class SimpleOperator(bpy.types.Operator):
    bl_idname = "wm.send_request"
    bl_label = "Отправить запрос"

    def execute(self, context):
        file_path = get_path_project()

        bpy.ops.wm.save_as_mainfile(filepath=file_path)
        send_request(file_path)
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
