from flask import render_template, session, current_app

from info.models import User
from info.modules.news import news_blu


@news_blu.route('/<int:news_id>')
def news_detail(news_id):
    # 查询用户登录信息
    user_id = session.get("user_id", None)
    user = None
    if user_id:
        # 尝试查询用户的模型
        try:
            user = User.query.get(user_id)
        except Exception as e:
            current_app.logger.error(e)
    data = {
        "user": user.to_dict() if user else None,
    }
    return render_template('news/detail.html', data=data)
