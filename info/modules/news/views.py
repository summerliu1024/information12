from flask import render_template, session, current_app, g

from info.models import User
from info.modules.news import news_blu
from info.utils.common import user_login_data


@news_blu.route('/<int:news_id>')
@user_login_data
def news_detail(news_id):
    # 查询用户登录信息
    user=g.user
    data = {
        "user": user.to_dict() if user else None,
    }
    return render_template('news/detail.html', data=data)
