import json
import pprint
import glob
import os.path

files = glob.glob('*.tex')
Assenbly_description = "アセンブリ用のレポートに調整されたテンプレートです。"
Ethics_description = "科学技術と倫理に調整されたレポートテンプレート。一部下線等ズレあり"
main_template_description = "レポート用に調整され様々なマクロの用意されたメインテンプレート。ファイル内のコメント等を参照"


json_data = {}
for file in files:
    f_name = file.rstrip('tex')
    f_name = f_name.rstrip('.')
    if (f_name == "assembly"):
        description = Assenbly_description
    elif (f_name == "ethics"):
        description = Ethics_description
    elif (f_name == "main_template"):
        description = main_template_description

    with open(file) as f:
        lines  = [s.strip() for s in f.readlines()]            
        incl = {
            "prefix":f_name,
            "body":lines,
            "description":description
        }
        json_data[f_name] = incl
    with open('latex.json','w') as j:
        json.dump(json_data, j ,indent=4, ensure_ascii=False)

print("Created latex.json! \nCopy to your snippets/latex.json")