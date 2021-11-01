import yagmail
a = yagmail.SMTP(
    user='1772597917@qq.com',
    password='ntspggekzcggdggd',
    host='smtp.qq.com'
)
a.send(
    to=['1772597917@qq.com','813513353@qq.com'],
    subject='标题',
    contents='测试日志及报告',
    attachments=[r'D:\untitled2\zuoye1029\common\r.html',r'D:\untitled2\zuoye1029\common\rizhi.log']
)