
import pandas as pd

path = '../data/AMap_adcode_citycode.xlsx'
df = pd.read_excel(path)


list= []
for index, row in df.iterrows():
    list.append({"adcode":row['adcode'], "citycode":row['citycode'], "name":row['中文名']})


def identify_parent_adcode(adcode):
    """
    根据adcode识别parentAdcode
    """
    redict={"parentAdcode":0,"level":""}
    if not adcode:
        redict["level"]=""
        redict["parentAdcode"]=0
        return redict

    code_str = str(adcode).zfill(6)

    # 国家级
    if adcode == 100000:
        redict["level"] = "country"
        redict["parentAdcode"] = 0
        return redict
    # 省级 (xx0000)
    if code_str.endswith('0000'):
        redict["level"] = "province"
        redict["parentAdcode"] = 100000
        return redict

    # 地级 (xxxx00，但不包括xx0000)
    if code_str.endswith('00') and not code_str.endswith('0000'):
        province_code = code_str[:2] + '0000'
        redict["level"] = "city"
        redict["parentAdcode"] = int(province_code)
        return redict

    else:
        # 对于直辖市的区级单位，parentAdcode应该是省级代码
        province_code = code_str[:2] + '0000'
        city_code = code_str[:4] + '00'

        # 判断是否为直辖市(北京、天津、上海、重庆)
        if code_str[:2] in ['11', '12', '31', '50']:
            redict["level"] = "district"
            redict["parentAdcode"] = int(province_code)
        else:
            redict["level"] = "district"
            redict["parentAdcode"] = int(city_code)
        return redict


# 批量处理数据
def process_adcode_data(data_list):
    """
    处理整个adcode数据列表，添加parentAdcode字段
    """
    result = []
    for item in data_list:
        new_item = item.copy()
        area_dict = identify_parent_adcode(item['adcode'])
        new_item['parentAdcode'] = area_dict["parentAdcode"]
        new_item['level'] = area_dict["level"]
        result.append(new_item)
    return result

processed_data = process_adcode_data(list)

try:
    with open('./city.txt', 'w+', encoding='utf-8') as src_f:
        src_f.write( str(processed_data))
except Exception as e:
    print(e)


