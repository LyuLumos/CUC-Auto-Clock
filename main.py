import argparse
import datetime
import json
import re
import time

import requests

from ljy import info

true = True
false = False


def get_jdy_info(sno, pwd):
    data = json.loads(requests.get(
        f"https://service-h8hlja8f-1304133342.bj.apigw.tencentcs.com/release/{sno}/{pwd}/cookies/jdy").text)
    return data["cookies"]["JDY_SID"], data["cookies"]["_csrf"]


def get_jdy_csrf(JDY_SID, _csrf, UA):
    cookies = {
        'help_btn_visible': 'true',
        'JDY_SID': JDY_SID,
        '_csrf': _csrf,
        'fx-lang': 'zh_cn',
        'Hm_lvt_48ee90f250328e7eaea0c743a4c3a339': '1652244024',
        'Hm_lpvt_48ee90f250328e7eaea0c743a4c3a339': '1652244287',
    }

    headers = {
        'Host': 'www.jiandaoyun.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': UA,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }
    data = requests.get('https://www.jiandaoyun.com/dashboard',
                        cookies=cookies, headers=headers).text
    return re.findall(r'window.jdy_csrf_token = "(.*)"', data)[0]


def post_jdy_data(JDY_SID, _csrf, X_Csrf_Token, UA, sno, college, dept, class_, pno, sname, curplace, province, city,
                  district, latitude, longitude, detail, dorm):
    cookies = {
        'help_btn_visible': 'true',
        'JDY_SID': JDY_SID,
        '_csrf': _csrf,
        'fx-lang': 'zh_cn',
        'Hm_lvt_48ee90f250328e7eaea0c743a4c3a339': '1652244024',
        'Hm_lpvt_48ee90f250328e7eaea0c743a4c3a339': '1652244287',
    }
    headers = {
        'Host': 'www.jiandaoyun.com',
        'Sec-Ch-Ua': '"(Not(A:Brand";v="8", "Chromium";v="101"',
        'X-Csrf-Token': X_Csrf_Token,
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': UA,
        'Content-Type': 'application/json;charset=UTF-8',
        'Accept': 'application/json, text/plain, */*',
        'X-Jdy-Ver': '4.8.0',
        'Origin': 'https://www.jiandaoyun.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.jiandaoyun.com/dashboard',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }
    URL = "https://www.jiandaoyun.com/_/data/create"
    data = {
        "values": {
            "_widget_1581259263912": {
                # 发起者， "62f4a3af1fd85000082d703c" for ljy
                "data": "62f4a3af1fd85000082d703c",
                "visible": true
            },
            "_widget_1581325409790": {
                # 学号
                "data": sno,
                "visible": true
            },
            "_widget_1581259263913": {
                # 个人信息 "日期-学院-学号-姓名"
                "data": '-'.join(
                    [str(int(i)) for i in datetime.date.today().strftime('%Y-%m-%d').split('-')] + [college, sno,
                                                                                                    sname]),
                "visible": true
            },
            "_widget_1581259263911": {
                # 学院
                "data": college,
                "visible": true
            },
            "_widget_1597408997541": {
                # 系
                "data": dept,
                "visible": true
            },
            "_widget_1648264291941": {
                # 班级，非必选
                "data": class_,
                "visible": true
            },
            "_widget_1582001600375": {
                # 学号
                "data": pno,
                "visible": true
            },
            "_widget_1581259263910": {
                # 日期
                "data": int(time.mktime(datetime.date.today().timetuple())) * 1000,
                "visible": true
            },
            "_widget_1594972479663": {
                # "北京"、"其他省市" or "境外"
                "data": curplace,
                "visible": true
            },
            "_widget_1594972480348": {
                # 定位目前所在地
                "data": {
                    "province": province,
                    "city": city,
                    "district": district,
                    "detail": detail,
                    "lnglatXY": [longitude, latitude]
                },
                "visible": true
            },
            "_widget_1661251622829": {
                # 该区域是否出现本地疫情
                "data": "否",
                "visible": true
            },
            "_widget_1597408997159": {
                # 该区域是否为中高风险
                "data": "否",
                "visible": true
            },
            "_widget_1595580335402": {
                # 所在地是否变化
                "data": "否",
                "visible": true
            },
            "_widget_1595602792466": {
                # 有变化才需要写的，变动信息
                "visible": false
            },
            "_widget_1598020946197": {
                # 有变化才需要写的，变动地址
                "visible": false
            },
            "_widget_1596350939077": {
                # 公寓
                "data": dorm,
                "visible": true
            },
            "_widget_1597486309838": {
                "data": [{
                    "_widget_1646814426533": {
                        # 记录日期
                        "data": int(time.mktime(datetime.date.today().timetuple())) * 1000
                    },
                    "_widget_1646815571409": {
                        # 日期-学号
                        "data": '-'.join(
                            [str(int(i)) for i in datetime.date.today().strftime('%Y-%m-%d').split('-')] + [sno])
                    },
                    "_widget_1597486309854": {
                        "data": "36"
                    },
                    "_widget_1597486309914": {
                        "data": "36"
                    },
                    "_widget_1597486309943": {
                        "data": "36"
                    }
                }],
                "visible": true
            },
            "_widget_1661251622874": {
                # 今日是否核酸 是，否
                "data": "是",
                "visible": true
            },
            "_widget_1661251622908": {
                # 24小时核酸报告情况，未出结果、已出结果，阴性or阳性
                "data": "已出结果，阴性",
                "visible": true
            },
            "_widget_1661251623043": {
                # 🐏才用填的截图
                "data": [],
                "visible": false
            },
            "_widget_1594974441946": {
                # 是否密接或确诊
                "data": "否",
                "visible": true
            },
            "_widget_1640358284019": {
                # 密接才需要，核酸报告
                "visible": false
            },
            "_widget_1640358284045": {
                # 密接才需要，7天行程
                "visible": false
            },
            "_widget_1640358284032": {
                # 密接才需要，最近接触人员名单
                "visible": false
            },
            "_widget_1611412944997": {
                # 隔离状态
                "data": "未隔离",
                "visible": true
            },
            "_widget_1611412945031": {
                # 隔离才需要，隔离地点
                "visible": false
            },
            "_widget_1647852158272": {
                # 共同居住人密接
                "data": "否",
                "visible": true
            },
            "_widget_1647852158338": {
                # 某个不可见的玩意
                "visible": false
            },
            "_widget_1599385089556": {
                "data": ["594ce5de3726b7321e0a6252"],
                "visible": false
            },
            "_widget_1599385089589": {
                "data": ["5b8df24ee6e30a158b2a97d9"],
                "visible": false
            },
            "_widget_1643251849715": {
                "data": "", "visible": false
            }
        },
        "appId": "5f36523524018e0006723761",
        "entryId": "5f1039fca2c60000075671b0",
        "formId": "5f1039fca2c60000075671b0",
        "hasResult": true,
        "dataOpId": "12bd2c21-e3a8-4c1a-9972-742658af2e25",  # 每天变化
        "authGroupId": -1
    }
    # print(data)
    response = requests.post(
        url=URL,
        data=json.dumps(data),
        headers=headers,
        cookies=cookies,
    )
    print(response.text)


def arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--studentNumber", help="校园卡账号")
    parser.add_argument("--userAgent", help="User Agent")
    parser.add_argument("-p", "--password", help="校园网密码")
    parser.add_argument("--college", default="计算机与网络空间安全学院", help="学院")
    parser.add_argument("--department", help="专业")
    parser.add_argument("--class_", help="班级", required=False)
    parser.add_argument("--phoneNumber", type=str)
    parser.add_argument("--studentName", help="姓名")
    parser.add_argument("--curplace", choices=["北京", "其他省市", "境外"])
    parser.add_argument("--province", default="北京市")
    parser.add_argument("--city", default="北京市")
    parser.add_argument("--district", default="朝阳区")
    parser.add_argument("--detailAddress", default="中国传媒大学48号教学楼")
    parser.add_argument("--position", nargs=2, default=[116.55629, 39.91295], type=float, help="经度和维度")
    parser.add_argument("--dorm", help="宿舍")
    return parser.parse_args()


def clock():
    args = arguments()
    sno = info.studentNumber if info.studentNumber else args.studentNumber
    pwd = info.pwd if info.pwd else args.password
    UA = info.userAgent if info.userAgent else args.userAgent
    college = info.college if info.college else info.college
    dept = info.department if info.department else info.department
    class_ = info.class_ if info.class_ else args.class_
    pno = info.phoneNumber if info.phoneNumber else args.phoneNumber
    sname = info.studentName if info.studentName else args.studentName
    curplace = info.curplace if info.curplace else args.curplace
    province = info.province if info.province else args.province
    city = info.city if info.city else args.city
    district = info.district if info.district else args.district
    detail = info.detailAddress if info.detailAddress else args.detailAddress
    latitude = info.latitude if info.latitude else args.latitude
    longitude = info.longitude if info.longitude else args.longitude
    dorm = info.dorm if info.dorm else args.dorm

    JDY_SID, _csrf = get_jdy_info(sno, pwd)
    X_Csrf_Token = get_jdy_csrf(JDY_SID, _csrf, UA)
    post_jdy_data(JDY_SID, _csrf, X_Csrf_Token, UA, sno, college, dept, class_, pno,
                  sname, curplace, province, city, district, latitude, longitude, detail, dorm)


if __name__ == '__main__':
    clock()