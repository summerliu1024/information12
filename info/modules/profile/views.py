from flask import render_template, g, request, jsonify, current_app
from werkzeug.utils import redirect

from info import constants
from info.libs.image_storage import storage
from info.modules.profile import profile_blu
from info.utils.common import user_login_data
from info.utils.response_code import RET


@profile_blu.route('/pass_info', methods=["GET", "POST"])
@user_login_data
def pass_info():
    if request.method == "GET":
        return render_template('news/user_pass_info.html')

    # 1. 获取参数
    old_password = request.json.get("old_password")
    news_password = request.json.get("new_password")

    # 2. 校验参数
    if not all([old_password, news_password]):
        return jsonify(errno=RET.PARAMERR, errmsg="参数错误")

    # 3. 判断旧密码是否正确
    user = g.user
    if not user.check_passowrd(old_password):
        return jsonify(errno=RET.PWDERR, errmsg="原密码错误")

    # 4. 设置新密码
    user.password = news_password

    return jsonify(errno=RET.OK, errmsg="保存成功")


@profile_blu.route('/pic_info', methods=["GET", "POST"])
@user_login_data
def pic_info():
    user = g.user
    if request.method == "GET":
        return render_template('news/user_pic_info.html', data={"user": user.to_dict()})

    # 如果是POST表示修改头像
    # 1. 取到上传的图片
    try:
        avatar = request.files.get("avatar").read()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.PARAMERR, errmsg="参数错误")

    # 2. 上传头像
    try:
        # 使用自已封装的storage方法去进行图片上传
        key = storage(avatar)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.THIRDERR, errmsg="上传头像失败")

    # 3. 保存头像地址
    user.avatar_url = key
    return jsonify(errno=RET.OK, errmsg="OK", data={"avatar_url": constants.QINIU_DOMIN_PREFIX + key})


@profile_blu.route('/base_info', methods=["GET", "POST"])
@user_login_data
def base_info():
    # 不同的请求方式，做不同的事情
    if request.method == "GET":
        return render_template('news/user_base_info.html', data={"user": g.user.to_dict()})

    # 代表是修改用户数据
    # 1. 取到传入的参数
    nick_name = request.json.get("nick_name")
    signature = request.json.get("signature")
    gender = request.json.get("gender")

    # 2. 校验参数
    if not all([nick_name, signature, gender]):
        return jsonify(errno=RET.PARAMERR, errmsg="参数错误")
    if gender not in ("WOMAN", "MAN"):
        return jsonify(errno=RET.PARAMERR, errmsg="参数错误")

    user = g.user
    user.signature = signature
    user.nick_name = nick_name
    user.gender = gender

    return jsonify(errno=RET.OK, errmsg="OK")


@profile_blu.route('/info')
@user_login_data
def user_info():
    user = g.user
    if not user:
        # 代表没有登录，重定向到首页
        return redirect("/")
    data = {"user": user.to_dict()}
    return render_template('news/user.html', data=data)
