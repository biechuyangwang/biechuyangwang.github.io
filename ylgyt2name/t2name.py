import urllib3
import time
import json
from tkinter import *
import certifi

city_id = [ {
    "id": 0,
    "province": "未知",
    "city": "未知"
}, {
    "id": 1,
    "province": "北京",
    "city": "北京"
}, {
    "id": 2,
    "province": "北京",
    "city": "东城"
}, {
    "id": 3,
    "province": "北京",
    "city": "西城"
}, {
    "id": 4,
    "province": "北京",
    "city": "崇文"
}, {
    "id": 5,
    "province": "北京",
    "city": "宣武"
}, {
    "id": 6,
    "province": "北京",
    "city": "朝阳"
}, {
    "id": 7,
    "province": "北京",
    "city": "丰台"
}, {
    "id": 8,
    "province": "北京",
    "city": "石景山"
}, {
    "id": 9,
    "province": "北京",
    "city": "海淀"
}, {
    "id": 10,
    "province": "北京",
    "city": "门头沟"
}, {
    "id": 11,
    "province": "北京",
    "city": "房山"
}, {
    "id": 12,
    "province": "北京",
    "city": "通州"
}, {
    "id": 13,
    "province": "北京",
    "city": "顺义"
}, {
    "id": 14,
    "province": "北京",
    "city": "昌平"
}, {
    "id": 15,
    "province": "北京",
    "city": "大兴"
}, {
    "id": 16,
    "province": "北京",
    "city": "怀柔"
}, {
    "id": 17,
    "province": "北京",
    "city": "平谷"
}, {
    "id": 18,
    "province": "北京",
    "city": "密云"
}, {
    "id": 19,
    "province": "北京",
    "city": "延庆"
}, {
    "id": 20,
    "province": "天津",
    "city": "天津"
}, {
    "id": 21,
    "province": "天津",
    "city": "和平"
}, {
    "id": 22,
    "province": "天津",
    "city": "河东"
}, {
    "id": 23,
    "province": "天津",
    "city": "河西"
}, {
    "id": 24,
    "province": "天津",
    "city": "南开"
}, {
    "id": 25,
    "province": "天津",
    "city": "河北"
}, {
    "id": 26,
    "province": "天津",
    "city": "红桥"
}, {
    "id": 27,
    "province": "天津",
    "city": "塘沽"
}, {
    "id": 28,
    "province": "天津",
    "city": "汉沽"
}, {
    "id": 29,
    "province": "天津",
    "city": "大港"
}, {
    "id": 30,
    "province": "天津",
    "city": "东丽"
}, {
    "id": 31,
    "province": "天津",
    "city": "西青"
}, {
    "id": 32,
    "province": "天津",
    "city": "津南"
}, {
    "id": 33,
    "province": "天津",
    "city": "北辰"
}, {
    "id": 34,
    "province": "天津",
    "city": "武清"
}, {
    "id": 35,
    "province": "天津",
    "city": "宝坻"
}, {
    "id": 36,
    "province": "天津",
    "city": "蓟县"
}, {
    "id": 37,
    "province": "天津",
    "city": "宁河"
}, {
    "id": 38,
    "province": "天津",
    "city": "芦台"
}, {
    "id": 39,
    "province": "天津",
    "city": "静海"
}, {
    "id": 40,
    "province": "上海",
    "city": "上海"
}, {
    "id": 41,
    "province": "上海",
    "city": "黄浦"
}, {
    "id": 42,
    "province": "上海",
    "city": "卢湾"
}, {
    "id": 43,
    "province": "上海",
    "city": "徐汇"
}, {
    "id": 44,
    "province": "上海",
    "city": "长宁"
}, {
    "id": 45,
    "province": "上海",
    "city": "静安"
}, {
    "id": 46,
    "province": "上海",
    "city": "普陀"
}, {
    "id": 47,
    "province": "上海",
    "city": "闸北"
}, {
    "id": 48,
    "province": "上海",
    "city": "虹口"
}, {
    "id": 49,
    "province": "上海",
    "city": "杨浦"
}, {
    "id": 50,
    "province": "上海",
    "city": "闵行"
}, {
    "id": 51,
    "province": "上海",
    "city": "宝山"
}, {
    "id": 52,
    "province": "上海",
    "city": "嘉定"
}, {
    "id": 53,
    "province": "上海",
    "city": "浦东"
}, {
    "id": 54,
    "province": "上海",
    "city": "金山"
}, {
    "id": 55,
    "province": "上海",
    "city": "松江"
}, {
    "id": 56,
    "province": "上海",
    "city": "青浦"
}, {
    "id": 57,
    "province": "上海",
    "city": "南汇"
}, {
    "id": 58,
    "province": "上海",
    "city": "奉贤"
}, {
    "id": 59,
    "province": "上海",
    "city": "崇明"
}, {
    "id": 60,
    "province": "上海",
    "city": "城桥"
}, {
    "id": 61,
    "province": "重庆",
    "city": "重庆"
}, {
    "id": 62,
    "province": "重庆",
    "city": "渝中"
}, {
    "id": 63,
    "province": "重庆",
    "city": "大渡口"
}, {
    "id": 64,
    "province": "重庆",
    "city": "江北"
}, {
    "id": 65,
    "province": "重庆",
    "city": "沙坪坝"
}, {
    "id": 66,
    "province": "重庆",
    "city": "九龙坡"
}, {
    "id": 67,
    "province": "重庆",
    "city": "南岸"
}, {
    "id": 68,
    "province": "重庆",
    "city": "北碚"
}, {
    "id": 69,
    "province": "重庆",
    "city": "万盛"
}, {
    "id": 70,
    "province": "重庆",
    "city": "双桥"
}, {
    "id": 71,
    "province": "重庆",
    "city": "渝北"
}, {
    "id": 72,
    "province": "重庆",
    "city": "巴南"
}, {
    "id": 73,
    "province": "重庆",
    "city": "万州"
}, {
    "id": 74,
    "province": "重庆",
    "city": "涪陵"
}, {
    "id": 75,
    "province": "重庆",
    "city": "黔江"
}, {
    "id": 76,
    "province": "重庆",
    "city": "长寿"
}, {
    "id": 77,
    "province": "重庆",
    "city": "合川"
}, {
    "id": 78,
    "province": "重庆",
    "city": "永川"
}, {
    "id": 79,
    "province": "重庆",
    "city": "江津"
}, {
    "id": 80,
    "province": "重庆",
    "city": "南川"
}, {
    "id": 81,
    "province": "重庆",
    "city": "綦江"
}, {
    "id": 82,
    "province": "重庆",
    "city": "潼南"
}, {
    "id": 83,
    "province": "重庆",
    "city": "铜梁"
}, {
    "id": 84,
    "province": "重庆",
    "city": "大足"
}, {
    "id": 85,
    "province": "重庆",
    "city": "荣昌"
}, {
    "id": 86,
    "province": "重庆",
    "city": "璧山"
}, {
    "id": 87,
    "province": "重庆",
    "city": "垫江"
}, {
    "id": 88,
    "province": "重庆",
    "city": "武隆"
}, {
    "id": 89,
    "province": "重庆",
    "city": "丰都"
}, {
    "id": 90,
    "province": "重庆",
    "city": "城口"
}, {
    "id": 91,
    "province": "重庆",
    "city": "梁平"
}, {
    "id": 92,
    "province": "重庆",
    "city": "开县"
}, {
    "id": 93,
    "province": "重庆",
    "city": "巫溪"
}, {
    "id": 94,
    "province": "重庆",
    "city": "巫山"
}, {
    "id": 95,
    "province": "重庆",
    "city": "奉节"
}, {
    "id": 96,
    "province": "重庆",
    "city": "云阳"
}, {
    "id": 97,
    "province": "重庆",
    "city": "忠县"
}, {
    "id": 98,
    "province": "重庆",
    "city": "石柱"
}, {
    "id": 99,
    "province": "重庆",
    "city": "彭水"
}, {
    "id": 100,
    "province": "重庆",
    "city": "酉阳"
}, {
    "id": 101,
    "province": "重庆",
    "city": "秀山"
}, {
    "id": 102,
    "province": "河北",
    "city": "河北"
}, {
    "id": 103,
    "province": "河北",
    "city": "石家庄"
}, {
    "id": 104,
    "province": "河北",
    "city": "张家口"
}, {
    "id": 105,
    "province": "河北",
    "city": "承德"
}, {
    "id": 106,
    "province": "河北",
    "city": "秦皇岛"
}, {
    "id": 107,
    "province": "河北",
    "city": "唐山"
}, {
    "id": 108,
    "province": "河北",
    "city": "廊坊"
}, {
    "id": 109,
    "province": "河北",
    "city": "保定"
}, {
    "id": 110,
    "province": "河北",
    "city": "衡水"
}, {
    "id": 111,
    "province": "河北",
    "city": "沧州"
}, {
    "id": 112,
    "province": "河北",
    "city": "邢台"
}, {
    "id": 113,
    "province": "河北",
    "city": "邯郸"
}, {
    "id": 114,
    "province": "山西",
    "city": "山西"
}, {
    "id": 115,
    "province": "山西",
    "city": "太原"
}, {
    "id": 116,
    "province": "山西",
    "city": "朔州"
}, {
    "id": 117,
    "province": "山西",
    "city": "大同"
}, {
    "id": 118,
    "province": "山西",
    "city": "阳泉"
}, {
    "id": 119,
    "province": "山西",
    "city": "长治"
}, {
    "id": 120,
    "province": "山西",
    "city": "晋城"
}, {
    "id": 121,
    "province": "山西",
    "city": "忻州"
}, {
    "id": 122,
    "province": "山西",
    "city": "晋中"
}, {
    "id": 123,
    "province": "山西",
    "city": "临汾"
}, {
    "id": 124,
    "province": "山西",
    "city": "吕梁"
}, {
    "id": 125,
    "province": "山西",
    "city": "运城"
}, {
    "id": 126,
    "province": "内蒙古",
    "city": "内蒙古"
}, {
    "id": 127,
    "province": "内蒙古",
    "city": "呼和浩特"
}, {
    "id": 128,
    "province": "内蒙古",
    "city": "包头"
}, {
    "id": 129,
    "province": "内蒙古",
    "city": "乌海"
}, {
    "id": 130,
    "province": "内蒙古",
    "city": "赤峰"
}, {
    "id": 131,
    "province": "内蒙古",
    "city": "通辽"
}, {
    "id": 132,
    "province": "内蒙古",
    "city": "呼伦贝尔"
}, {
    "id": 133,
    "province": "内蒙古",
    "city": "鄂尔多斯"
}, {
    "id": 134,
    "province": "内蒙古",
    "city": "乌兰察布"
}, {
    "id": 135,
    "province": "内蒙古",
    "city": "巴彦淖尔"
}, {
    "id": 136,
    "province": "内蒙古",
    "city": "兴安"
}, {
    "id": 137,
    "province": "内蒙古",
    "city": "锡林郭勒"
}, {
    "id": 138,
    "province": "内蒙古",
    "city": "阿拉善"
}, {
    "id": 139,
    "province": "辽宁",
    "city": "辽宁"
}, {
    "id": 140,
    "province": "辽宁",
    "city": "沈阳"
}, {
    "id": 141,
    "province": "辽宁",
    "city": "朝阳"
}, {
    "id": 142,
    "province": "辽宁",
    "city": "阜新"
}, {
    "id": 143,
    "province": "辽宁",
    "city": "铁岭"
}, {
    "id": 144,
    "province": "辽宁",
    "city": "抚顺"
}, {
    "id": 145,
    "province": "辽宁",
    "city": "本溪"
}, {
    "id": 146,
    "province": "辽宁",
    "city": "辽阳"
}, {
    "id": 147,
    "province": "辽宁",
    "city": "鞍山"
}, {
    "id": 148,
    "province": "辽宁",
    "city": "丹东"
}, {
    "id": 149,
    "province": "辽宁",
    "city": "大连"
}, {
    "id": 150,
    "province": "辽宁",
    "city": "营口"
}, {
    "id": 151,
    "province": "辽宁",
    "city": "盘锦"
}, {
    "id": 152,
    "province": "辽宁",
    "city": "锦州"
}, {
    "id": 153,
    "province": "辽宁",
    "city": "葫芦岛"
}, {
    "id": 154,
    "province": "吉林",
    "city": "吉林"
}, {
    "id": 155,
    "province": "吉林",
    "city": "长春"
}, {
    "id": 156,
    "province": "吉林",
    "city": "白城"
}, {
    "id": 157,
    "province": "吉林",
    "city": "松原"
}, {
    "id": 158,
    "province": "吉林",
    "city": "吉林"
}, {
    "id": 159,
    "province": "吉林",
    "city": "四平"
}, {
    "id": 160,
    "province": "吉林",
    "city": "辽源"
}, {
    "id": 161,
    "province": "吉林",
    "city": "通化"
}, {
    "id": 162,
    "province": "吉林",
    "city": "白山"
}, {
    "id": 163,
    "province": "吉林",
    "city": "延边"
}, {
    "id": 164,
    "province": "黑龙江",
    "city": "黑龙江"
}, {
    "id": 165,
    "province": "黑龙江",
    "city": "哈尔滨"
}, {
    "id": 166,
    "province": "黑龙江",
    "city": "齐齐哈尔"
}, {
    "id": 167,
    "province": "黑龙江",
    "city": "七台河"
}, {
    "id": 168,
    "province": "黑龙江",
    "city": "黑河"
}, {
    "id": 169,
    "province": "黑龙江",
    "city": "大庆"
}, {
    "id": 170,
    "province": "黑龙江",
    "city": "鹤岗"
}, {
    "id": 171,
    "province": "黑龙江",
    "city": "伊春"
}, {
    "id": 172,
    "province": "黑龙江",
    "city": "佳木斯"
}, {
    "id": 173,
    "province": "黑龙江",
    "city": "双鸭山"
}, {
    "id": 174,
    "province": "黑龙江",
    "city": "鸡西"
}, {
    "id": 175,
    "province": "黑龙江",
    "city": "牡丹江"
}, {
    "id": 176,
    "province": "黑龙江",
    "city": "绥化"
}, {
    "id": 177,
    "province": "黑龙江",
    "city": "大兴安岭"
}, {
    "id": 178,
    "province": "江苏",
    "city": "江苏"
}, {
    "id": 179,
    "province": "江苏",
    "city": "南京"
}, {
    "id": 180,
    "province": "江苏",
    "city": "徐州"
}, {
    "id": 181,
    "province": "江苏",
    "city": "连云港"
}, {
    "id": 182,
    "province": "江苏",
    "city": "宿迁"
}, {
    "id": 183,
    "province": "江苏",
    "city": "淮安"
}, {
    "id": 184,
    "province": "江苏",
    "city": "盐城"
}, {
    "id": 185,
    "province": "江苏",
    "city": "扬州"
}, {
    "id": 186,
    "province": "江苏",
    "city": "泰州"
}, {
    "id": 187,
    "province": "江苏",
    "city": "南通"
}, {
    "id": 188,
    "province": "江苏",
    "city": "镇江"
}, {
    "id": 189,
    "province": "江苏",
    "city": "常州"
}, {
    "id": 190,
    "province": "江苏",
    "city": "无锡"
}, {
    "id": 191,
    "province": "江苏",
    "city": "苏州"
}, {
    "id": 192,
    "province": "浙江",
    "city": "浙江"
}, {
    "id": 193,
    "province": "浙江",
    "city": "杭州"
}, {
    "id": 194,
    "province": "浙江",
    "city": "湖州"
}, {
    "id": 195,
    "province": "浙江",
    "city": "嘉兴"
}, {
    "id": 196,
    "province": "浙江",
    "city": "舟山"
}, {
    "id": 197,
    "province": "浙江",
    "city": "宁波"
}, {
    "id": 198,
    "province": "浙江",
    "city": "绍兴"
}, {
    "id": 199,
    "province": "浙江",
    "city": "衢州"
}, {
    "id": 200,
    "province": "浙江",
    "city": "金华"
}, {
    "id": 201,
    "province": "浙江",
    "city": "台州"
}, {
    "id": 202,
    "province": "浙江",
    "city": "温州"
}, {
    "id": 203,
    "province": "浙江",
    "city": "丽水"
}, {
    "id": 204,
    "province": "安徽",
    "city": "安徽"
}, {
    "id": 205,
    "province": "安徽",
    "city": "合肥"
}, {
    "id": 206,
    "province": "安徽",
    "city": "宿州"
}, {
    "id": 207,
    "province": "安徽",
    "city": "淮北"
}, {
    "id": 208,
    "province": "安徽",
    "city": "亳州"
}, {
    "id": 209,
    "province": "安徽",
    "city": "阜阳"
}, {
    "id": 210,
    "province": "安徽",
    "city": "蚌埠"
}, {
    "id": 211,
    "province": "安徽",
    "city": "淮南"
}, {
    "id": 212,
    "province": "安徽",
    "city": "滁州"
}, {
    "id": 213,
    "province": "安徽",
    "city": "马鞍山"
}, {
    "id": 214,
    "province": "安徽",
    "city": "芜湖"
}, {
    "id": 215,
    "province": "安徽",
    "city": "铜陵"
}, {
    "id": 216,
    "province": "安徽",
    "city": "安庆"
}, {
    "id": 217,
    "province": "安徽",
    "city": "黄山"
}, {
    "id": 218,
    "province": "安徽",
    "city": "六安"
}, {
    "id": 219,
    "province": "安徽",
    "city": "巢湖"
}, {
    "id": 220,
    "province": "安徽",
    "city": "池州"
}, {
    "id": 221,
    "province": "安徽",
    "city": "宣城"
}, {
    "id": 222,
    "province": "福建",
    "city": "福建"
}, {
    "id": 223,
    "province": "福建",
    "city": "福州"
}, {
    "id": 224,
    "province": "福建",
    "city": "南平"
}, {
    "id": 225,
    "province": "福建",
    "city": "莆田"
}, {
    "id": 226,
    "province": "福建",
    "city": "三明"
}, {
    "id": 227,
    "province": "福建",
    "city": "泉州"
}, {
    "id": 228,
    "province": "福建",
    "city": "厦门"
}, {
    "id": 229,
    "province": "福建",
    "city": "漳州"
}, {
    "id": 230,
    "province": "福建",
    "city": "龙岩"
}, {
    "id": 231,
    "province": "福建",
    "city": "宁德"
}, {
    "id": 232,
    "province": "江西",
    "city": "江西"
}, {
    "id": 233,
    "province": "江西",
    "city": "南昌"
}, {
    "id": 234,
    "province": "江西",
    "city": "九江"
}, {
    "id": 235,
    "province": "江西",
    "city": "景德镇"
}, {
    "id": 236,
    "province": "江西",
    "city": "鹰潭"
}, {
    "id": 237,
    "province": "江西",
    "city": "新余"
}, {
    "id": 238,
    "province": "江西",
    "city": "萍乡"
}, {
    "id": 239,
    "province": "江西",
    "city": "赣州"
}, {
    "id": 240,
    "province": "江西",
    "city": "上饶"
}, {
    "id": 241,
    "province": "江西",
    "city": "抚州"
}, {
    "id": 242,
    "province": "江西",
    "city": "宜春"
}, {
    "id": 243,
    "province": "江西",
    "city": "吉安"
}, {
    "id": 244,
    "province": "山东",
    "city": "济南"
}, {
    "id": 245,
    "province": "山东",
    "city": "青岛"
}, {
    "id": 246,
    "province": "山东",
    "city": "聊城"
}, {
    "id": 247,
    "province": "山东",
    "city": "德州"
}, {
    "id": 248,
    "province": "山东",
    "city": "东营"
}, {
    "id": 249,
    "province": "山东",
    "city": "淄博"
}, {
    "id": 250,
    "province": "山东",
    "city": "潍坊"
}, {
    "id": 251,
    "province": "山东",
    "city": "烟台"
}, {
    "id": 252,
    "province": "山东",
    "city": "威海"
}, {
    "id": 253,
    "province": "山东",
    "city": "日照"
}, {
    "id": 254,
    "province": "山东",
    "city": "临沂"
}, {
    "id": 255,
    "province": "山东",
    "city": "枣庄"
}, {
    "id": 256,
    "province": "山东",
    "city": "济宁"
}, {
    "id": 257,
    "province": "山东",
    "city": "泰安"
}, {
    "id": 258,
    "province": "山东",
    "city": "莱芜"
}, {
    "id": 259,
    "province": "山东",
    "city": "滨州"
}, {
    "id": 260,
    "province": "山东",
    "city": "菏泽"
}, {
    "id": 261,
    "province": "河南",
    "city": "河南"
}, {
    "id": 262,
    "province": "河南",
    "city": "郑州"
}, {
    "id": 263,
    "province": "河南",
    "city": "开封"
}, {
    "id": 264,
    "province": "河南",
    "city": "三门峡"
}, {
    "id": 265,
    "province": "河南",
    "city": "洛阳"
}, {
    "id": 266,
    "province": "河南",
    "city": "焦作"
}, {
    "id": 267,
    "province": "河南",
    "city": "新乡"
}, {
    "id": 268,
    "province": "河南",
    "city": "鹤壁"
}, {
    "id": 269,
    "province": "河南",
    "city": "安阳"
}, {
    "id": 270,
    "province": "河南",
    "city": "濮阳"
}, {
    "id": 271,
    "province": "河南",
    "city": "商丘"
}, {
    "id": 272,
    "province": "河南",
    "city": "许昌"
}, {
    "id": 273,
    "province": "河南",
    "city": "漯河"
}, {
    "id": 274,
    "province": "河南",
    "city": "平顶山"
}, {
    "id": 275,
    "province": "河南",
    "city": "南阳"
}, {
    "id": 276,
    "province": "河南",
    "city": "信阳"
}, {
    "id": 277,
    "province": "河南",
    "city": "周口"
}, {
    "id": 278,
    "province": "河南",
    "city": "驻马店"
}, {
    "id": 279,
    "province": "河南",
    "city": "济源"
}, {
    "id": 280,
    "province": "湖北",
    "city": "武汉"
}, {
    "id": 281,
    "province": "湖北",
    "city": "湖北"
}, {
    "id": 282,
    "province": "湖北",
    "city": "十堰"
}, {
    "id": 283,
    "province": "湖北",
    "city": "襄樊"
}, {
    "id": 284,
    "province": "湖北",
    "city": "荆门"
}, {
    "id": 285,
    "province": "湖北",
    "city": "孝感"
}, {
    "id": 286,
    "province": "湖北",
    "city": "黄冈"
}, {
    "id": 287,
    "province": "湖北",
    "city": "鄂州"
}, {
    "id": 288,
    "province": "湖北",
    "city": "黄石"
}, {
    "id": 289,
    "province": "湖北",
    "city": "咸宁"
}, {
    "id": 290,
    "province": "湖北",
    "city": "荆州"
}, {
    "id": 291,
    "province": "湖北",
    "city": "宜昌"
}, {
    "id": 292,
    "province": "湖北",
    "city": "随州"
}, {
    "id": 293,
    "province": "湖北",
    "city": "仙桃"
}, {
    "id": 294,
    "province": "湖北",
    "city": "天门"
}, {
    "id": 295,
    "province": "湖北",
    "city": "潜江"
}, {
    "id": 296,
    "province": "湖北",
    "city": "神农架"
}, {
    "id": 297,
    "province": "湖北",
    "city": "恩施州"
}, {
    "id": 298,
    "province": "湖南",
    "city": "湖南"
}, {
    "id": 299,
    "province": "湖南",
    "city": "长沙"
}, {
    "id": 300,
    "province": "湖南",
    "city": "张家界"
}, {
    "id": 301,
    "province": "湖南",
    "city": "常德"
}, {
    "id": 302,
    "province": "湖南",
    "city": "益阳"
}, {
    "id": 303,
    "province": "湖南",
    "city": "岳阳"
}, {
    "id": 304,
    "province": "湖南",
    "city": "株洲"
}, {
    "id": 305,
    "province": "湖南",
    "city": "湘潭"
}, {
    "id": 306,
    "province": "湖南",
    "city": "衡阳"
}, {
    "id": 307,
    "province": "湖南",
    "city": "郴州"
}, {
    "id": 308,
    "province": "湖南",
    "city": "永州"
}, {
    "id": 309,
    "province": "湖南",
    "city": "邵阳"
}, {
    "id": 310,
    "province": "湖南",
    "city": "怀化"
}, {
    "id": 311,
    "province": "湖南",
    "city": "娄底"
}, {
    "id": 312,
    "province": "湖南",
    "city": "湘西州"
}, {
    "id": 313,
    "province": "广东",
    "city": "广东"
}, {
    "id": 314,
    "province": "广东",
    "city": "广州"
}, {
    "id": 315,
    "province": "广东",
    "city": "深圳"
}, {
    "id": 316,
    "province": "广东",
    "city": "清远"
}, {
    "id": 317,
    "province": "广东",
    "city": "韶关"
}, {
    "id": 318,
    "province": "广东",
    "city": "河源"
}, {
    "id": 319,
    "province": "广东",
    "city": "梅州"
}, {
    "id": 320,
    "province": "广东",
    "city": "潮州"
}, {
    "id": 321,
    "province": "广东",
    "city": "汕头"
}, {
    "id": 322,
    "province": "广东",
    "city": "揭阳"
}, {
    "id": 323,
    "province": "广东",
    "city": "汕尾"
}, {
    "id": 324,
    "province": "广东",
    "city": "惠州"
}, {
    "id": 325,
    "province": "广东",
    "city": "东莞"
}, {
    "id": 326,
    "province": "广东",
    "city": "珠海"
}, {
    "id": 327,
    "province": "广东",
    "city": "中山"
}, {
    "id": 328,
    "province": "广东",
    "city": "江门"
}, {
    "id": 329,
    "province": "广东",
    "city": "佛山"
}, {
    "id": 330,
    "province": "广东",
    "city": "肇庆"
}, {
    "id": 331,
    "province": "广东",
    "city": "云浮"
}, {
    "id": 332,
    "province": "广东",
    "city": "阳江"
}, {
    "id": 333,
    "province": "广东",
    "city": "茂名"
}, {
    "id": 334,
    "province": "广东",
    "city": "湛江"
}, {
    "id": 335,
    "province": "广西",
    "city": "广西"
}, {
    "id": 336,
    "province": "广西",
    "city": "南宁"
}, {
    "id": 337,
    "province": "广西",
    "city": "桂林"
}, {
    "id": 338,
    "province": "广西",
    "city": "柳州"
}, {
    "id": 339,
    "province": "广西",
    "city": "梧州"
}, {
    "id": 340,
    "province": "广西",
    "city": "贵港"
}, {
    "id": 341,
    "province": "广西",
    "city": "玉林"
}, {
    "id": 342,
    "province": "广西",
    "city": "钦州"
}, {
    "id": 343,
    "province": "广西",
    "city": "北海"
}, {
    "id": 344,
    "province": "广西",
    "city": "防城港"
}, {
    "id": 345,
    "province": "广西",
    "city": "崇左"
}, {
    "id": 346,
    "province": "广西",
    "city": "百色"
}, {
    "id": 347,
    "province": "广西",
    "city": "河池"
}, {
    "id": 348,
    "province": "广西",
    "city": "来宾"
}, {
    "id": 349,
    "province": "广西",
    "city": "贺州"
}, {
    "id": 350,
    "province": "海南",
    "city": "海南"
}, {
    "id": 351,
    "province": "海南",
    "city": "海口"
}, {
    "id": 352,
    "province": "海南",
    "city": "三亚"
}, {
    "id": 353,
    "province": "海南",
    "city": "文昌"
}, {
    "id": 354,
    "province": "海南",
    "city": "琼海"
}, {
    "id": 355,
    "province": "海南",
    "city": "万宁"
}, {
    "id": 356,
    "province": "海南",
    "city": "五指山"
}, {
    "id": 357,
    "province": "海南",
    "city": "东方"
}, {
    "id": 358,
    "province": "海南",
    "city": "儋州"
}, {
    "id": 359,
    "province": "海南",
    "city": "临高"
}, {
    "id": 360,
    "province": "海南",
    "city": "澄迈"
}, {
    "id": 361,
    "province": "海南",
    "city": "定安"
}, {
    "id": 362,
    "province": "海南",
    "city": "屯昌"
}, {
    "id": 363,
    "province": "海南",
    "city": "昌江"
}, {
    "id": 364,
    "province": "海南",
    "city": "白沙"
}, {
    "id": 365,
    "province": "海南",
    "city": "琼中"
}, {
    "id": 366,
    "province": "海南",
    "city": "陵水"
}, {
    "id": 367,
    "province": "海南",
    "city": "保亭"
}, {
    "id": 368,
    "province": "海南",
    "city": "乐东"
}, {
    "id": 369,
    "province": "四川",
    "city": "四川"
}, {
    "id": 370,
    "province": "四川",
    "city": "成都"
}, {
    "id": 371,
    "province": "四川",
    "city": "广元"
}, {
    "id": 372,
    "province": "四川",
    "city": "绵阳"
}, {
    "id": 373,
    "province": "四川",
    "city": "德阳"
}, {
    "id": 374,
    "province": "四川",
    "city": "南充"
}, {
    "id": 375,
    "province": "四川",
    "city": "广安"
}, {
    "id": 376,
    "province": "四川",
    "city": "遂宁"
}, {
    "id": 377,
    "province": "四川",
    "city": "内江"
}, {
    "id": 378,
    "province": "四川",
    "city": "乐山"
}, {
    "id": 379,
    "province": "四川",
    "city": "自贡"
}, {
    "id": 380,
    "province": "四川",
    "city": "泸州"
}, {
    "id": 381,
    "province": "四川",
    "city": "宜宾"
}, {
    "id": 382,
    "province": "四川",
    "city": "攀枝花"
}, {
    "id": 383,
    "province": "四川",
    "city": "巴中"
}, {
    "id": 384,
    "province": "四川",
    "city": "达州"
}, {
    "id": 385,
    "province": "四川",
    "city": "资阳"
}, {
    "id": 386,
    "province": "四川",
    "city": "眉山"
}, {
    "id": 387,
    "province": "四川",
    "city": "雅安"
}, {
    "id": 388,
    "province": "四川",
    "city": "阿坝"
}, {
    "id": 389,
    "province": "四川",
    "city": "甘孜"
}, {
    "id": 390,
    "province": "四川",
    "city": "凉山"
}, {
    "id": 391,
    "province": "贵州",
    "city": "贵州"
}, {
    "id": 392,
    "province": "贵州",
    "city": "贵阳"
}, {
    "id": 393,
    "province": "贵州",
    "city": "六盘水"
}, {
    "id": 394,
    "province": "贵州",
    "city": "遵义"
}, {
    "id": 395,
    "province": "贵州",
    "city": "安顺"
}, {
    "id": 396,
    "province": "贵州",
    "city": "毕节"
}, {
    "id": 397,
    "province": "贵州",
    "city": "铜仁"
}, {
    "id": 398,
    "province": "贵州",
    "city": "黔东南"
}, {
    "id": 399,
    "province": "贵州",
    "city": "黔南"
}, {
    "id": 400,
    "province": "贵州",
    "city": "黔西南"
}, {
    "id": 401,
    "province": "云南",
    "city": "云南"
}, {
    "id": 402,
    "province": "云南",
    "city": "昆明"
}, {
    "id": 403,
    "province": "云南",
    "city": "曲靖"
}, {
    "id": 404,
    "province": "云南",
    "city": "玉溪"
}, {
    "id": 405,
    "province": "云南",
    "city": "保山"
}, {
    "id": 406,
    "province": "云南",
    "city": "昭通"
}, {
    "id": 407,
    "province": "云南",
    "city": "丽江"
}, {
    "id": 408,
    "province": "云南",
    "city": "思茅"
}, {
    "id": 409,
    "province": "云南",
    "city": "临沧"
}, {
    "id": 410,
    "province": "云南",
    "city": "德宏"
}, {
    "id": 411,
    "province": "云南",
    "city": "怒江"
}, {
    "id": 412,
    "province": "云南",
    "city": "迪庆"
}, {
    "id": 413,
    "province": "云南",
    "city": "大理"
}, {
    "id": 414,
    "province": "云南",
    "city": "楚雄"
}, {
    "id": 415,
    "province": "云南",
    "city": "红河"
}, {
    "id": 416,
    "province": "云南",
    "city": "文山"
}, {
    "id": 417,
    "province": "云南",
    "city": "西双版纳"
}, {
    "id": 418,
    "province": "西藏",
    "city": "西藏"
}, {
    "id": 419,
    "province": "西藏",
    "city": "拉萨"
}, {
    "id": 420,
    "province": "西藏",
    "city": "那曲"
}, {
    "id": 421,
    "province": "西藏",
    "city": "昌都"
}, {
    "id": 422,
    "province": "西藏",
    "city": "林芝"
}, {
    "id": 423,
    "province": "西藏",
    "city": "山南"
}, {
    "id": 424,
    "province": "西藏",
    "city": "日喀则"
}, {
    "id": 425,
    "province": "西藏",
    "city": "阿里"
}, {
    "id": 426,
    "province": "陕西",
    "city": "陕西"
}, {
    "id": 427,
    "province": "陕西",
    "city": "西安"
}, {
    "id": 428,
    "province": "陕西",
    "city": "延安"
}, {
    "id": 429,
    "province": "陕西",
    "city": "铜川"
}, {
    "id": 430,
    "province": "陕西",
    "city": "渭南"
}, {
    "id": 431,
    "province": "陕西",
    "city": "咸阳"
}, {
    "id": 432,
    "province": "陕西",
    "city": "宝鸡"
}, {
    "id": 433,
    "province": "陕西",
    "city": "汉中"
}, {
    "id": 434,
    "province": "陕西",
    "city": "榆林"
}, {
    "id": 435,
    "province": "陕西",
    "city": "安康"
}, {
    "id": 436,
    "province": "陕西",
    "city": "商洛"
}, {
    "id": 437,
    "province": "甘肃",
    "city": "甘肃"
}, {
    "id": 438,
    "province": "甘肃",
    "city": "兰州"
}, {
    "id": 439,
    "province": "甘肃",
    "city": "嘉峪关"
}, {
    "id": 440,
    "province": "甘肃",
    "city": "白银"
}, {
    "id": 441,
    "province": "甘肃",
    "city": "天水"
}, {
    "id": 442,
    "province": "甘肃",
    "city": "武威"
}, {
    "id": 443,
    "province": "甘肃",
    "city": "酒泉"
}, {
    "id": 444,
    "province": "甘肃",
    "city": "张掖"
}, {
    "id": 445,
    "province": "甘肃",
    "city": "庆阳"
}, {
    "id": 446,
    "province": "甘肃",
    "city": "平凉"
}, {
    "id": 447,
    "province": "甘肃",
    "city": "定西"
}, {
    "id": 448,
    "province": "甘肃",
    "city": "陇南"
}, {
    "id": 449,
    "province": "甘肃",
    "city": "临夏"
}, {
    "id": 450,
    "province": "甘肃",
    "city": "甘南"
}, {
    "id": 451,
    "province": "青海",
    "city": "青海"
}, {
    "id": 452,
    "province": "青海",
    "city": "西宁"
}, {
    "id": 453,
    "province": "青海",
    "city": "海东"
}, {
    "id": 454,
    "province": "青海",
    "city": "海北"
}, {
    "id": 455,
    "province": "青海",
    "city": "海南"
}, {
    "id": 456,
    "province": "青海",
    "city": "黄南"
}, {
    "id": 457,
    "province": "青海",
    "city": "果洛"
}, {
    "id": 458,
    "province": "青海",
    "city": "玉树"
}, {
    "id": 459,
    "province": "青海",
    "city": "海西"
}, {
    "id": 460,
    "province": "宁夏",
    "city": "宁夏"
}, {
    "id": 461,
    "province": "宁夏",
    "city": "银川"
}, {
    "id": 462,
    "province": "宁夏",
    "city": "石嘴山"
}, {
    "id": 463,
    "province": "宁夏",
    "city": "吴忠"
}, {
    "id": 464,
    "province": "宁夏",
    "city": "固原"
}, {
    "id": 465,
    "province": "宁夏",
    "city": "中卫"
}, {
    "id": 466,
    "province": "新疆",
    "city": "新疆"
}, {
    "id": 467,
    "province": "新疆",
    "city": "乌鲁木齐"
}, {
    "id": 468,
    "province": "新疆",
    "city": "克拉玛依"
}, {
    "id": 469,
    "province": "新疆",
    "city": "石河子"
}, {
    "id": 470,
    "province": "新疆",
    "city": "阿拉尔"
}, {
    "id": 471,
    "province": "新疆",
    "city": "图木舒克"
}, {
    "id": 472,
    "province": "新疆",
    "city": "五家渠"
}, {
    "id": 473,
    "province": "新疆",
    "city": "喀什"
}, {
    "id": 474,
    "province": "新疆",
    "city": "阿克苏"
}, {
    "id": 475,
    "province": "新疆",
    "city": "和田"
}, {
    "id": 476,
    "province": "新疆",
    "city": "吐鲁番"
}, {
    "id": 477,
    "province": "新疆",
    "city": "哈密"
}, {
    "id": 478,
    "province": "新疆",
    "city": "克孜勒苏柯"
}, {
    "id": 479,
    "province": "新疆",
    "city": "博尔塔拉"
}, {
    "id": 480,
    "province": "新疆",
    "city": "昌吉"
}, {
    "id": 481,
    "province": "新疆",
    "city": "巴音郭楞"
}, {
    "id": 482,
    "province": "新疆",
    "city": "伊犁"
}, {
    "id": 483,
    "province": "新疆",
    "city": "塔城"
}, {
    "id": 484,
    "province": "新疆",
    "city": "阿勒泰"
}, {
    "id": 485,
    "province": "香港",
    "city": "香港"
}, {
    "id": 486,
    "province": "澳门",
    "city": "澳门"
}, {
    "id": 487,
    "province": "台湾",
    "city": "台湾"
}, {
    "id": 488,
    "province": "台湾",
    "city": "台北"
}, {
    "id": 489,
    "province": "台湾",
    "city": "高雄"
}, {
    "id": 490,
    "province": "台湾",
    "city": "台中"
}, {
    "id": 491,
    "province": "台湾",
    "city": "花莲"
}, {
    "id": 492,
    "province": "台湾",
    "city": "基隆"
}, {
    "id": 493,
    "province": "台湾",
    "city": "嘉义"
}, {
    "id": 494,
    "province": "台湾",
    "city": "金门"
}, {
    "id": 495,
    "province": "台湾",
    "city": "连江"
}, {
    "id": 496,
    "province": "台湾",
    "city": "苗栗"
}, {
    "id": 497,
    "province": "台湾",
    "city": "南投"
}, {
    "id": 498,
    "province": "台湾",
    "city": "澎湖"
}, {
    "id": 499,
    "province": "台湾",
    "city": "屏东"
}, {
    "id": 500,
    "province": "台湾",
    "city": "台东"
}, {
    "id": 501,
    "province": "台湾",
    "city": "台南"
}, {
    "id": 502,
    "province": "台湾",
    "city": "桃园"
}, {
    "id": 503,
    "province": "台湾",
    "city": "新竹"
}, {
    "id": 504,
    "province": "台湾",
    "city": "宜兰"
}, {
    "id": 505,
    "province": "台湾",
    "city": "云林"
}, {
    "id": 506,
    "province": "台湾",
    "city": "彰化"
} ]

def pprint(content):
    text.insert(INSERT,content)
    text.insert(INSERT,'\n')

def getExpirationDateFromToken(token):
    """由token获取过期时间

    Args:
        token (_type_): _description_
    """
    import base64
    expirationdate = token.split('.')[1][8:24]
    expirationdate = int(base64.b64decode(expirationdate)[1:-1])
    # expirationdate = time.localtime(int(expirationdate))
    # expirationdate = time.strftime("%Y-%m-%d %H:%M:%S", expirationdate)
    return expirationdate


def getUserInfo():
    """获取个人信息

    Args:
    """
    text.delete(1.0,'end')
    token = entry.get()
    expirationdate = getExpirationDateFromToken(token)
    # pprint(expirationdate)
    # pprint(time.time())
    expirationdate_int = time.localtime(int(expirationdate))
    expirationdate_format = time.strftime("%Y-%m-%d %H:%M:%S", expirationdate_int)
    if(time.time() >= expirationdate):
        pprint(f"当前t已过期，过期时间为：{expirationdate_format}")
        return
    
    BASE_URL = "https://cat-match.easygame2021.com/sheep/v1/game"
    url = f"{BASE_URL}/personal_info?"
    request_manager = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where(), timeout=30)
    headers={
        "Connection": "keep-alive",
        "t": token,
        "content-type": "application/json",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.29(0x18001d2c) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wx141bfb9b73c970a9/66/page-frame.html"
    }
    try:
        # 日常相关
        response = request_manager.request("GET", url, headers=headers, preload_content=False)
        content = response.read()
        content = json.loads(content)
        response.close()

        # 竞赛相关
        url_race = f"{BASE_URL}/race/rank_list?detail=1"
        response_race = request_manager.request("GET", url_race, headers=headers, preload_content=False)
        content_race = response_race.read()
        content_race = json.loads(content_race)
        response_race.close()

        # 皮肤相关
        url_skin = f"{BASE_URL}/skin/info?"
        response_skin = request_manager.request("GET", url_skin, headers=headers, preload_content=False)
        content_skin = response_skin.read()
        content_skin = json.loads(content_skin)
        response_skin.close()
        
        area_expire_at = time.localtime(int(content['data']['area_expire_at']))
        area_expire_at = time.strftime("%Y-%m-%d %H:%M:%S", area_expire_at)

        register_time = time.localtime(int(content['data']['register_time']))
        register_time = time.strftime("%Y-%m-%d %H:%M:%S", register_time)

        today_ts = time.localtime(int(content['data']['today_ts']))
        today_ts = time.strftime("%Y-%m-%d %H:%M:%S", today_ts)

        # {
        #     "id": 313,
        #     "province": "广东",
        #     "city": "广东"
        # }
        province =  [d['province'] for d in city_id if d["id"] == content['data']['area_id']][0]
        city = [d['city'] for d in city_id if d["id"] == content['data']['area_id']][0]

        # 大世界相关

        pprint(f"{'='*20}广告{'='*21}")
        pprint(f"欢迎进Q群331240392定制相关业务")
        pprint(f"{'='*10}本软件由 星期六的故事 提供{'='*10}")
        # pprint(f"用户数据：{content['data']}")
        pprint(f"用户名：{content['data']['nick_name']}")
        pprint(f"注册时间：{register_time}")
        pprint(f"t值过期时间：{expirationdate_format}")
        pprint(f"所属地区：{province}省 {city}")
        pprint(f"定位重置时间：{area_expire_at}")
        # pprint(f"皮肤数量：{content['data']['skin']}")
        pprint(f"今日是否已通关日常：{'是' if content['data']['today_state']==1 else '否'}")
        if(content['data']['today_state'] == 1):
            pprint(f"今日日常通关时刻：{today_ts}")
        
        race = [item for item in content_race['data']['list'] if item['uid']== content['data']['uid']][0]
        # pprint(f"{race}") 
        # pprint(f"{content_race['data']['list']}") 
        pprint(f"竞赛日期: {content_race['data']['race_id']}")
        pprint(f"竞赛排名: {race['rank']}, 完成进度: {race['percent']}%, 将获得萝卜: {race['exp']}")

        recent_1_skin = content_skin['data']['skin_list'][-1]
        recent_2_skin = content_skin["data"]['skin_list'][-2]
        recent_3_skin = content_skin["data"]['skin_list'][-3]

        
        local_time_now = time.localtime(int(time.time()))
        # pprint(f"当前时间：{local_time_now.tm_year}-{local_time_now.tm_mon}-{local_time_now.tm_mday}")
        local_time_now_0 = int(time.time()-local_time_now.tm_hour*60*60-local_time_now.tm_min*60-local_time_now.tm_sec+5)
        local_time_now_0_format = time.localtime(local_time_now_0)
        local_time_now_0_format = time.strftime("%Y-%m-%d %H:%M:%S", local_time_now_0_format)
        # pprint(f"{local_time_now_0_format}")

        # {
        # id: 354,
        # created_at: 1679250655,
        # reason: 'wd:632c4756c94ad51bae5e9794'
        # }
        # Mon Mar 20 2023 02:30:55 GMT+0800 (中国标准时间)
        # { id: 366, created_at: 1679328963, reason: 'a:广东' }
        # { id: 318, created_at: 1679069346, reason: 'ac:season' }
        # { id: 51, created_at: 1675355783, reason: 'f:wx' }
        # { id: 210, created_at: 1673194353, reason: 't:40' }
        # { id: 57, created_at: 1671122805, reason: 'ta:0' }
        world_skin_count = 0
        if recent_1_skin['created_at'] >= local_time_now_0:
            if recent_1_skin['reason'].split(':')[0] == 'wd':
                pprint(f"今日大世界获得皮肤: {recent_1_skin['id']}")
            elif recent_1_skin['reason'].split(':')[1] == 'season':
                pprint(f"赛季获得皮肤: {recent_1_skin['id']}")
            elif recent_1_skin['reason'].split(':')[0] == 't':
                pprint(f"今日话题获得皮肤: {recent_1_skin['id']}")
            else: pprint(f"今日常规获得皮肤: {recent_1_skin['id']}")
        if recent_2_skin['created_at'] >= local_time_now_0:
            if recent_2_skin['reason'].split(':')[0] == 'wd':
                pprint(f"今日大世界获得皮肤: {recent_2_skin['id']}")
            elif recent_2_skin['reason'].split(':')[1] == 'season':
                pprint(f"赛季获得皮肤: {recent_2_skin['id']}")
            elif recent_2_skin['reason'].split(':')[0] == 't':
                pprint(f"今日话题获得皮肤: {recent_2_skin['id']}")
            else: pprint(f"今日常规获得皮肤: {recent_2_skin['id']}")
        if recent_3_skin['created_at'] >= local_time_now_0:
            if recent_3_skin['reason'].split(':')[0] == 'wd':
                pprint(f"今日大世界获得皮肤: {recent_3_skin['id']}")
            elif recent_3_skin['reason'].split(':')[1] == 'season':
                pprint(f"赛季获得皮肤: {recent_3_skin['id']}")
            elif recent_3_skin['reason'].split(':')[0] == 't':
                pprint(f"今日话题获得皮肤: {recent_3_skin['id']}")
            else: pprint(f"今日常规获得皮肤: {recent_3_skin['id']}")

        # pprint(f"t值：{token}")
        pprint(f"{'='*20}结束{'='*21}")
        return True
    except Exception as e:
        pprint(str(e))
        return None

if __name__ == "__main__":
    # 创建窗口：实例化一个窗口对象。
    root = Tk()

    # 窗口大小
    root.geometry("800x480+347+128")

    #  窗口标题
    root.title("由token获取个人信息")

    frame1 = Frame(root)
    frame2 = Frame(root)
    frame3 = Frame(root)

    # 添加标签控件
    label = Label(frame1,text="输入t(token)值:",font=("宋体",25),fg="black")

    # 定位
    label.grid()

    # 添加输入框
    entry = Entry(frame2,width=40,font=("宋体",25),fg="black")
    entry.grid(row=0,column=0, padx=10)

    # 添加点击按钮
    button = Button(frame2,text="转换",font=("宋体",18),fg="blue",command=getUserInfo)
    button.grid(row=0,column=1)

    # 多行文本
    text = Text(frame3,width=70,autoseparators=True,state="normal",wrap="word",spacing2=2,spacing3=6,tabs=10,font=("宋体",20),fg="black")
    scroll = Scrollbar(frame3,orient=VERTICAL)
    scroll.pack(side=RIGHT,fill=Y)
    scroll.config(command=text.yview)
    text.config(yscrollcommand=scroll.set)
    text.pack(side=LEFT,fill=X)


    frame1.pack(pady=5,fill=X)
    frame2.pack(fill='both')
    frame3.pack(fill='both')

    # 显示窗口
    root.mainloop()