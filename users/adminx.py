import xadmin
from .models import User

class UserAdmin(object):
    list_display = ['username', 'email', 'date_joined','nickname','is_active']
    search_fields = ['username', 'email', 'date_joined']
    list_filter = ['username', 'email', 'date_joined']

# admin.site.unregister(User)
xadmin.site.unregister(User)
xadmin.site.register(User, UserAdmin)


