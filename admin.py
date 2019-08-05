from models import *
from flask_admin.contrib.sqla import ModelView
from flask_admin.actions import action
import requests


# 定义模型ProgramInfo的admin后台
class ProgramInfoAdmin(ModelView):
    # 将字段设置中文内容
    column_labels = dict(clientIP='IP地址', name='名称', introduce='描述', statusLock='状态锁')
    page_size = 30
    # 新增任务请求功能
    @action('执行任务', '执行任务', '确定执行任务？')
    def action_task(self, ids):
        for id in ids:
            info = ProgramInfo.query.filter_by(id=id).first()
            if not info.statusLock:
                ip = info.clientIP
                name = info.name
                # 写入任务记录表
                data = TaskRecord(clientIP=ip, name=name)
                db.session.add(data)
                # 获取刚写入数据的主键
                db.session.flush()
                taskId = str(data.id)
                url = ip+'?name='+name+"&taskId="+taskId
                print(url)
                # 向client端发送任务请求
                try:
                    r = requests.get(url)
                    if r.status_code == 200:
                        info.statusLock = 'Lock'
                except:
                    pass
                db.session.commit()


# 在admin界面注册视图
admin.add_view(ProgramInfoAdmin(ProgramInfo, db.session, name='程序信息表'))


# 定义模型TaskRecord的Admin后台
class TaskRecordAdmin(ModelView):
    column_labels = dict(clientIP='IP地址', name='名称', createTime='创建时间')


# 在admin界面注册视图
admin.add_view(TaskRecordAdmin(TaskRecord, db.session, name='任务记录表'))

