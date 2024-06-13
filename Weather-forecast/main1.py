import requests
import json
import pandas as pd
import requests
import csv
import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import SUNKEN, Label
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk, font
from PIL import Image, ImageTk
from matplotlib.font_manager import FontProperties
from tkinter import Tk, Label, W, E
from tkinter import Tk, Canvas
from PIL import Image, ImageTk, ImageDraw, ImageFont



def create_transparent_watermark(root, text="水印文字", font_path="Arial", font_size=48):
    # 确保窗口已经设置尺寸
    width = root.winfo_width() or 800  # 如果宽度为0，提供默认值
    height = root.winfo_height() or 600  # 如果高度为0，提供默认值

    # 创建一个带有透明背景的PIL图像
    background = Image.new('RGBA', (width, height), (255, 255, 255, 0))

    # 尝试使用指定的字体路径创建字体对象
    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError as e:
        print(f"无法加载字体: {e}")
        return  # 字体加载失败，退出函数

    # 使用PIL的ImageDraw来绘制文本
    draw = ImageDraw.Draw(background)
    text_width, text_height = draw.textsize(text, font=font)  # 获取文本尺寸

    # 计算文本的x和y坐标，这里以中心对齐为例
    x = (width - text_width) // 2
    y = (height - text_height) // 2
    draw.text((x, y), text, font=font, fill=(0, 0, 0, 255))  # 绘制文本

    # 将PIL图像转换为Tkinter的PhotoImage
    photo = ImageTk.PhotoImage(background)

    # 创建一个Label控件，使用photoimage作为其图像，并覆盖整个窗口
    watermark = tk.Label(root, image=photo, bg='transparent')
    watermark.image = photo  # 保存对图像的引用
    watermark.pack(side='top', fill='both', expand=True)  # 使用pack布局






# 指定中文字体路径，例如 'SimHei'（黑体）
chinese_font_path = 'C:\\Windows\\Fonts\\SimHei.ttf'  # 适用于 macOS
# chinese_font_path = 'C:\\Windows\\Fonts\\SimHei.ttf'  # 适用于 Windows

# 创建一个 FontProperties 对象，指定中文字体路径
chinese_font = FontProperties(fname=chinese_font_path)

# 配置 matplotlib 使用中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号 '-' 显示为方块的问题

headers = {

    'Cookie':'Hm_lvt_aadbcc83cc37610f46f503983c444e90=1718194959; Hm_lpvt_aadbcc83cc37610f46f503983c444e90=1718194959; Hm_lvt_0b8b0a2a4a45cbaaa6f549dcad3329a6=1718194959; Hm_lpvt_0b8b0a2a4a45cbaaa6f549dcad3329a6=1718194959',

    'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'

}


url =  'https://air.cnemc.cn:18007/CityData/GetAllCityRealTimeAQIModels'

data = {

}

response = requests.post(url = url,data=data,verify=False)



# 发起请求
data_list = response.json()  # 将 JSON 响应转换为 Python 列表

# 将数据转换为 DataFrame
df = pd.DataFrame(data_list)

# 现在你可以使用 Pandas 的功能来处理数据
# 例如，保存到 CSV 文件
df.to_csv('data.csv', index=False,encoding='gbk')

file_path = 'data.csv'

# 读取 CSV 文件
df = pd.read_csv(file_path, encoding='GBK')

# 打印原始列名


# 定义新的列名映射
# 这里的键是原始列名，值是新的列名
column_mapping = {
    'Id': '序号',
    'TimePoint': '时间',
    'AQI': '空气指数',
    'COLevel': '二氧化碳等级',
    'NO2Level': '二氧化氮等级',
    'O3Level': 'new_column_name2',
    'PM10Level': 'PM10',
    'PM2_5Level': 'PM2.5',
    'SO2Level': '二氧化硫等级',
    'Area': '地区',
    'AqiLevel': 'new_column_name1',
    'PrimaryPollutant': 'new_column_name2',
    'Quality': '质量',
    'Measure': 'new_column_name2',
    'Unheathful': 'new_column_name1',
    'Latitude': 'new_column_name2',
    'Longitude': 'new_column_name1',
    'ProvinceId': 'new_column_name2',
    # ... 继续添加所有需要更改的列名映射
}

# 修改列名
df.rename(columns=column_mapping, inplace=True)

# 打印修改后的列名
print("修改后的列名:", df.columns)

# 将修改后的 DataFrame 保存到新的 CSV 文件
# 如果你想覆盖原始文件，可以将 '修改后数据.csv' 替换为原始文件名
df.to_csv('修改后数据.csv', index=False,encoding='gbk')

# 读取 CSV 文件
df = pd.read_csv('修改后数据.csv', encoding='gbk')

# 添加序号列
df['序号'] = range(1, len(df) + 1)

# 保存包含序号列的 DataFrame 到新的 CSV 文件
df.to_csv('修改后数据.csv', index=False, encoding='gbk')





for item in response.json():
    for key, value in item.items():
        print(f"{key}: {value}")
file_path = 'data.csv'

print(df)


import matplotlib.pyplot as plt


def create_bar_chart(filtered_data):
    if filtered_data.empty:
        print("没有数据可以绘制图表。")
        return None

    columns = [ 'PM10', 'PM2.5', '二氧化碳等级', '二氧化硫等级']
    colors = [ 'green', 'orange', 'red', 'purple']

    # 创建柱形图和轴对象
    fig, ax = plt.subplots(figsize=(4, 2))  # 调整大小以适应多个柱状图

    # 获取地区名称作为 x 轴的类别数量
    n_groups = len(filtered_data['地区'].unique())

    # 计算每个柱子的宽度和间距
    bar_width = 0.3
    indices = range(n_groups)

    # 绘制柱状图
    for i, column in enumerate(columns):
        data = filtered_data[column]

        # 计算每个柱子的 x 位置
        positions = [index + i * bar_width for index in indices]

        # 绘制柱子
        ax.bar(positions, data, bar_width, color=colors[i], label=column)

    # 设置图表标题和轴标签
    ax.set_title('空气质量指数和相关数据')
    ax.set_xlabel('地区')
    ax.set_ylabel('数值')

    # 设置 x 轴的标签（这里假设 '地区' 列的数据是有序的）
    ax.set_xticks(indices)
    ax.set_xticklabels(filtered_data['地区'].unique(), rotation=45)

    # 设置图例
    ax.legend()

    # 自动调整 y 轴的范围以适应数据
    ax.autoscale(axis='y', tight=True)

    # 调整子图参数，确保图例和标签不会超出图表范围
    plt.subplots_adjust(left=0.15, right=0.95, top=0.9, bottom=0.1)

    return fig

def search_data(key_word):
    return df[df['地区'].str.contains(key_word, na=False)]

# 定义一个函数，用于更新Treeview显示查询结果
def update_treeview(event=None):
    keyword = search_entry.get()
    result_df = search_data(keyword)
    # 清空Treeview
    for i in tree.get_children():
        tree.delete(i)
    # 将查询结果添加到Treeview
    for index, row in result_df.iterrows():
        tree.insert('', 'end', values=row.tolist())


def read_csv_file(file_path):
    return pd.read_csv('修改后数据.csv', encoding='gbk')

def search_data(key_word):
    # 在地区列中搜索关键字
    return df[df['地区'].str.contains(key_word, na=False)]

def open_new_window():
    # 创建一个 Toplevel 窗口作为新窗口
    new_window = tk.Toplevel(root)
    new_window.title("查询结果")

    # 设置新窗口的大小
    new_width = 700
    new_height = 400

    # 根据屏幕的尺寸计算新窗口的位置
    screen_width = new_window.winfo_screenwidth()
    screen_height = new_window.winfo_screenheight()
    x = (screen_width - new_width) // 2
    y = (screen_height - new_height) // 2
    new_window.geometry(f'{new_width}x{new_height}+{x}+{y}')

    # 读取数据
    file_path = '修改后数据.csv'  # 替换为你的CSV文件路径
    global df  # 声明 df 为全局变量，以便在搜索时使用
    df = read_csv_file(file_path)

    # 搜索关键字
    key_word = search_entry.get()

    filtered_data = search_data(key_word)
    print(filtered_data)
    # 创建 Treeview 控件
    columns_to_display = ['地区', '空气指数', 'PM10', 'PM2.5','二氧化碳等级','二氧化硫等级']
    selected_data = filtered_data[columns_to_display]
    # 创建 Treeview 控件，并只包含您选择的列
    tree = ttk.Treeview(new_window, columns=columns_to_display, show='headings')

    # 设置列标题
    for col in selected_data:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    fig = create_bar_chart(filtered_data)

    # 检查 fig 是否被创建
    if fig:
        # 将图表添加到 Tkinter 窗口
        canvas = FigureCanvasTkAgg(fig, master=new_window)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # 如果有结果，将它们添加到 Treeview
    if not selected_data.empty:
        for index, row in selected_data.iterrows():
            tree.insert('', 'end', values=row.tolist())

    else:
        # 如果没有结果，显示提示信息
        label = tk.Label(new_window, text="没有找到匹配的数据。")
        label.pack(expand=True, fill='both')

    # 添加滚动条
    scrollbar_y = ttk.Scrollbar(new_window, orient="vertical", command=tree.yview)
    scrollbar_y.pack(side="right", fill="y")
    tree.config(yscrollcommand=scrollbar_y.set)

    scrollbar_x = ttk.Scrollbar(new_window, orient="horizontal", command=tree.xview)
    scrollbar_x.pack(side="bottom", fill="x")
    tree.config(xscrollcommand=scrollbar_x.set)
    tree.pack(expand=True, fill='both')



# 将JSON数据转换为pandas DataFrame
df = pd.DataFrame(data)

# 创建主窗口
root = tk.Tk()
#root.geometry('1280x960')
root.title("空气质量数据展示")


root.update_idletasks()  # 更新窗口尺寸信息
create_transparent_watermark(root)

def center_window(width=500, height=500):
    # 获取屏幕的尺寸
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    # 计算 x 和 y 坐标
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    root.geometry(f'{width}x{height}+{int(x)}+{int(y)}')




# 设置窗口大小并居中显示
width = 880
height = 700
center_window(width, height)

image_filename = 'sc.jpg'  # 图片文件路径
image = Image.open(image_filename)
photo = ImageTk.PhotoImage(image)

# 创建一个 Label 显示图片，将其放置在顶部
image_label = tk.Label(root, image=photo)
  # 使用相对位置放置在顶部中间
image_label.pack()
file_path = '修改后数据.csv'
df = pd.read_csv(file_path, encoding='gbk')

# 假设你需要获取的列名是 'Column1', 'Column2', 'Column3', 'Column4', 'Column5'
columns_needed = ['序号', '地区', '时间', '空气指数', 'PM2.5']
df_selected = df[columns_needed]


# 步骤2和3: 创建 Tkinter 窗口并添加 Treeview 控件
tree = ttk.Treeview(root, columns=columns_needed, show='headings')


search_frame = ttk.Frame(root, padding="10")
search_frame.pack(side="top", fill="x")

# 创建标签
search_label = ttk.Label(search_frame, text="输入地区关键字:")
search_label.grid(row=0, column=0, sticky="e")  # 右对齐

# 创建输入框
search_entry = ttk.Entry(search_frame)
search_entry.grid(row=0, column=1, sticky="we")  # 填充x方向，东西对齐

# 创建查询按钮
search_button = ttk.Button(search_frame, text="查询", command=open_new_window)
search_button.grid(row=0, column=2)  # 将按钮放在输入框的右侧

# 使用grid布局管理器，确保组件在同一行
search_frame.columnconfigure(1, weight=1)  # 让输入框占据更多空间










# 定义列的标题和宽度
column_titles = df_selected.columns.tolist()
for col in column_titles:
    tree.heading(col, text=col)  # 设置列标题
    tree.column(col, width=100)  # 设置列宽度，可以根据需要调整

# 步骤4: 更新 Treeview 控件
# 将 DataFrame 的数据添加到 Treeview
for index, row in df_selected.iterrows():
    # 使用 row.tolist() 插入数据，Treeview 会根据列标题自动分配值
    tree.insert('', 'end', values=row.tolist())

# 将 Treeview 控件放入主窗口
scrollbar_y = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
scrollbar_y.pack(side="right", fill="y")

# 创建水平滚动条并与 Treeview 的水平视图链接
scrollbar_x = ttk.Scrollbar(root, orient="horizontal", command=tree.xview)
scrollbar_x.pack(side="bottom", fill="x")

# 将滚动条的命令与 Treeview 的滚动命令链接
tree.config(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

# 将 Treeview 控件放入主窗口

tree.pack(expand=True, fill='both')





# 运行主循环
root.mainloop()






























