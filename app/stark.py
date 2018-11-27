from app import models
from stark.service.stark import site, StarkConfig


class DerpartMentConfig(StarkConfig):
    """docstring for DerpartMentConfig"""
    list_display = [
        # StarkConfig.display_checkbox,
        'title',
        'intro',
        # StarkConfig.display_edit_del,
    ]


site.register(models.Department, DerpartMentConfig)


class DoctorConfig(StarkConfig):
    """docstring for DerpartMentConfig"""
    list_display = [
        # StarkConfig.display_checkbox,
        'name',
        'level',
        'price',
        'gender',
        'depart',
        'intro',
        # StarkConfig.display_edit_del,
    ]


site.register(models.Doctor, DoctorConfig)


class CustomerConfig(StarkConfig):
    """docstring for DerpartMentConfig"""
    list_display = [
        # StarkConfig.display_checkbox,
        'name',
        'phone',
        'gender',
        'disease',
        'count',
        'intro',
        # StarkConfig.display_edit_del,
    ]


site.register(models.Customer, CustomerConfig)

# class MenuConfig(StarkConfig):
#     """docstring for DerpartMentConfig"""
#     list_display = [
#         # StarkConfig.display_checkbox,
#         'title',
#         'icon',
#         StarkConfig.display_edit_del,
#     ]


# site.register(models.Menu, MenuConfig)


# class PermissionConfig(StarkConfig):
#     """docstring for DerpartMentConfig"""
#     list_display = [
#         # StarkConfig.display_checkbox,
#         'title',
#         'url',
#         'name',
#         'pid',
#         'menu',
#         StarkConfig.display_edit_del,
#     ]


# site.register(models.Permission, PermissionConfig)


# class RoleConfig(StarkConfig):
#     """docstring for DerpartMentConfig"""
#     list_display = [
#         # StarkConfig.display_checkbox,
#         'title',
#         'permissions',
#         'gender',
#         'depart',
#         StarkConfig.display_edit_del,
#     ]


# site.register(models.Role, RoleConfig)


class UserInfoConfig(StarkConfig):
    """docstring for DerpartMentConfig"""
    list_display = [
        # StarkConfig.display_checkbox,
        'name',
        'phone',
        'gender',
        'depart',
        StarkConfig.display_edit_del,
    ]


site.register(models.UserInfo, UserInfoConfig)
