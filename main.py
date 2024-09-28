import bpy
import requests

log_messages = []


def send_request():
    url = "http://example.com/api"
    data = {"key": "value"}
    # response = requests.post(url, json=data)
    log_messages.append(url)


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

        for message in log_messages:
            layout.label(text=message)


def register():
    bpy.utils.register_class(SimpleOperator)
    bpy.utils.register_class(SimplePanel)


def unregister():
    bpy.utils.unregister_class(SimplePanel)
    bpy.utils.unregister_class(SimpleOperator)


if __name__ == "__main__":
    register()
