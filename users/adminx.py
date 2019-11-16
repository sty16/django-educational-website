import xadmin
from .models import User

class UserAdmin(object):
    list_display = ['username', 'email', 'date_joined','nickname','is_admin','is_active','mobile','image']
    search_fields = ['username', 'email', 'date_joined','mobile']
    list_filter = ['username', 'email', 'date_joined','mobile']

# admin.site.unregister(User)
xadmin.site.unregister(User)
xadmin.site.register(User, UserAdmin)


