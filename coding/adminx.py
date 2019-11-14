# coding/adminx.py
import xadmin
from .models import Code, LikeRecord

# Code的admin管理器
class CodeAdmin(object):
    '''课程'''

    list_display = [ 'codename','desc','userinfo','fav_nums','download_nums','add_time','syntax_check','manual_check','result_check','star_check', 'codefile']   #显示的字段
    search_fields =[ 'codename','desc','userinfo','fav_nums','download_nums','add_time','syntax_check','manual_check','result_check','star_check','codefile']  #搜索          #搜索
    list_filter =[ 'codename','desc','userinfo','fav_nums','download_nums','add_time','syntax_check','result_check','star_check','manual_check','codefile']   #过滤

# 将管理器与model进行注册关联
class LikeAdmin(object):
    list_display = ['Like_user','Like_time','Like_codefile']
    search_fields = ['Like_user','Like_time','Like_codefile']
    list_filter = ['Like_user','Like_time','Like_codefile']
xadmin.site.register(Code, CodeAdmin)
xadmin.site.register(LikeRecord,LikeAdmin)