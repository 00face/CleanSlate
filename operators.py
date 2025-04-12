import bpy

class OBJECT_OT_clean_slate(bpy.types.Operator):
    bl_idname = "object.clean_slate"
    bl_label = "Clean Slate"
    bl_description = "Clear the entire scene"

    def execute(self, context):
        print("Clean Slate: Starting scene cleanup.")

        bpy.ops.object.select_all(action='DESELECT')
        print("Clean Slate: Deselected all objects.")

        bpy.ops.object.select_by_type(type='MESH')
        bpy.ops.object.select_by_type(type='CAMERA', extend=True)
        bpy.ops.object.select_by_type(type='LIGHT', extend=True)
        bpy.ops.object.select_by_type(type='EMPTY', extend=True)
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete()
        print("Clean Slate: Deleted all objects, including default ones.")

        # Clear the collection hierarchy
        for collection in bpy.data.collections:
            if collection.name != 'Master Collection':
                bpy.data.collections.remove(collection)
        print("Clean Slate: Cleared collection hierarchy.")

        bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=True)
        print("Clean Slate: Purged orphaned data blocks.")

        bpy.context.scene.world = None
        for material in bpy.data.materials:
            if not material.users:
                bpy.data.materials.remove(material)
        print("Clean Slate: Additional cleanup completed.")

        print("Clean Slate: Scene cleanup completed.")
        return {'FINISHED'}

def register():
    bpy.utils.register_class(OBJECT_OT_clean_slate)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_clean_slate)
