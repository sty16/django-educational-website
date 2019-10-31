# coding/adminx.py
import xadmin
from .models import Code

# Code的admin管理器
class CodeAdmin(object):
    '''课程'''

    list_display = [ 'codename','desc','userinfo','fav_nums','download_nums','add_time','syntax_check','manual_check','codefile']   #显示的字段
    search_fields =[ 'codename','desc','userinfo','fav_nums','download_nums','add_time','syntax_check','manual_check','codefile']  #搜索          #搜索
    list_filter =[ 'codename','desc','userinfo','fav_nums','download_nums','add_time','syntax_check','manual_check','codefile']   #过滤

# 将管理器与model进行注册关联
xadmin.site.register(Code, CodeAdmin)