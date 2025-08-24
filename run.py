import os
from app import create_app, db
from app.models import User, Post  # 根据你的模型导入

# 从环境变量读取配置，默认为 'default'
config_name = os.environ.get('FLASK_CONFIG') or 'default'

# 创建应用实例
app = create_app(config_name)

# 如果需要在应用上下文中执行的操作可以放在这里
@app.shell_context_processor
def make_shell_context():
    """为Flask shell添加上下文"""
    return {
        'db': db,
        'User': User,
        'Post': Post
        # 添加其他需要在shell中直接访问的模型
    }

if __name__ == '__main__':
    # 启动开发服务器
    # host='0.0.0.0' 允许外部访问，debug=True 开启调试模式
    app.run(host='0.0.0.0', port=5000, debug=True)