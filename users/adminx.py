import xadmin
from .models import User, Banner
from xadmin import views

class GlobalSettings(object):
    # 修改title
    site_title = '航天创客后台管理'
    # 修改footer
    site_footer = '航天创客'
    # 收起菜单
    menu_style = 'accordion'

# 将title和footer信息进行注册
class UserAdmin(object):
    list_display = ['username', 'email', 'date_joined','nickname','is_admin','is_active','mobile','image']
    search_fields = ['username', 'email', 'date_joined','mobile']
    list_filter = ['username', 'email', 'date_joined','mobile']

class BannerAdmin(object):
    list_display = ['title', 'image','index', 'add_time']
    search_fields = ['title', 'image','index']
    list_filter = ['title', 'image', 'index', 'add_time']


# admin.site.unregister(User)
xadmin.site.unregister(User)
xadmin.site.register(User, UserAdmin)
xadmin.site.register(views.CommAdminView,GlobalSettings)
xadmin.site.register(Banner,BannerAdmin)