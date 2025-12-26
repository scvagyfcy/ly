import streamlit as st
import pandas as pd
import random
import os
import time

# 设置页面配置
st.set_page_config(
    page_title="多功能应用整合",
    page_icon="🚀",
    layout="wide"
)

# 自定义样式：优化顶部导航栏外观
st.markdown("""
    <style>
        /* 顶部导航按钮样式 */
        .nav-button {
            border: none;
            padding: 0.5rem 1rem;
            border-radius: 8px;
            cursor: pointer;
            font-size: 16px;
            font-weight: 500;
            transition: all 0.2s ease;
            width: 100%;
        }
        .nav-button-selected {
            background-color: #0EA5E9;
            color: white;
        }
        .nav-button-unselected {
            background-color: #f0f2f6;
            color: #333;
        }
        .nav-button-unselected:hover {
            background-color: #e6e9ed;
        }
        /* 移除默认的Streamlit边距，让导航栏更紧凑 */
        div[data-testid="stHorizontalBlock"] {
            gap: 8px;
            margin-bottom: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# 初始化会话状态：记录当前选中的页面
if "current_page" not in st.session_state:
    st.session_state.current_page = "音乐播放器"

# 定义所有功能页面名称
page_names = ["音乐播放器", "图片相册", "小组档案", "动漫视频", "美食仪表盘", "简历生成器"]

# 创建顶部导航栏
st.markdown("### 功能导航")
# 创建与页面数量匹配的列
cols = st.columns(len(page_names))
for idx, col in enumerate(cols):
    page_name = page_names[idx]
    # 判断当前按钮是否为选中状态，应用不同样式
    if st.session_state.current_page == page_name:
        button_style = "nav-button nav-button-selected"
    else:
        button_style = "nav-button nav-button-unselected"
    
    # 渲染按钮并处理点击事件
    with col:
        if st.button(
            page_name,
            key=f"nav_{idx}",
            use_container_width=True
        ):
            st.session_state.current_page = page_name
            st.rerun()  # 重新运行应用以切换页面

# 音乐播放器页面
def music_player():
    st.title("简易音乐播放器")
    
    # 初始化会话状态
    if "current_idx" not in st.session_state:
        st.session_state.current_idx = 0
    if "is_playing" not in st.session_state:
        st.session_state.is_playing = False
    if "progress" not in st.session_state:
        st.session_state.progress = 0
    
    # 歌曲数据
    songs = [
        {
            "title": "起风了",
            "artist": "冯沁苑",
            "duration": "5:25",
            "cover": "http://p2.music.126.net/diGAyEmpymX8G7JcnElncQ==/109951163699673355.jpg?param=130y130",
            "audio": "https://music.163.com/song/media/outer/url?id=1330348068"
        },
        {
            "title": "碎碎念",
            "artist": "队长", 
            "duration": "2:12",
            "cover": "http://p1.music.126.net/RYIrCEYzgeAD85DJ0rgOQA==/109951169256300966.jpg?param=130y130",
            "audio": "https://music.163.com/song/media/outer/url?id=2097443876"
        },
        {
            "title": "于是",
            "artist": "郑润泽",
            "duration": "3:52", 
            "cover": "http://p2.music.126.net/BtXjoRNLCZjoSV-3Ag3M0Q==/109951164458656122.jpg?param=640y300",
            "audio": "https://music.163.com/song/media/outer/url?id=1303464858"
        }
    ]
    
    # 切换函数
    def prev_song():
        st.session_state.current_idx = (st.session_state.current_idx - 1) % len(songs)
        st.session_state.progress = 0
    
    def next_song():
        st.session_state.current_idx = (st.session_state.current_idx + 1) % len(songs)
        st.session_state.progress = 0
    
    # 播放控制
    def toggle_play():
        st.session_state.is_playing = not st.session_state.is_playing
    
    # 获取当前歌曲
    current_song = songs[st.session_state.current_idx]
    
    # 显示专辑封面和歌曲信息
    col1, col2 = st.columns([2, 3])
    
    with col1:
        st.image(current_song["cover"], caption="专辑封面", width=250)
    
    with col2:
        st.markdown(f"## {current_song['title']}")
        st.markdown(f"**歌手**: {current_song['artist']}")
        st.markdown(f"**时长**: {current_song['duration']}")
    
    # 控制按钮
    col3, col4 = st.columns(2)
    with col3:
        st.button("上一首", on_click=prev_song)
    with col4:
        st.button("下一首", on_click=next_song)
    
    # 播放/暂停按钮
    play_text = "⏸️ 暂停" if st.session_state.is_playing else "▶️ 播放"
    st.button(play_text, on_click=toggle_play)
    
    # 进度条
    st.progress(st.session_state.progress / 100)
    
    # 时间显示
    st.markdown(f"0:00 / {current_song['duration']}")
    
    # 音频播放器
    st.audio(current_song["audio"])

# 图片相册页面
def image_gallery():
    st.title("我的图片相册")
    
    # 准备图片数据：列表中每个元素是(图片路径, 图注)
    image_data = [
         ("cat1.jpg", "橘白相间的猫咪，正慵懒地晒太阳"),
    ("dog.jpg", "活泼的小狗在草地上奔跑"),
    ("flower.jpg", "盛放的向日葵，充满生机")
    ]
    
    # 初始化会话状态，记录当前显示的图片索引
    if "img_current_idx" not in st.session_state:
        st.session_state.img_current_idx = 0
    
    # 定义切换图片的函数
    def prev_image():
        st.session_state.img_current_idx = (st.session_state.img_current_idx - 1) % len(image_data)
    
    def next_image():
        st.session_state.img_current_idx = (st.session_state.img_current_idx + 1) % len(image_data)
    
    # 显示当前图片和图注
    current_img, current_caption = image_data[st.session_state.img_current_idx]
    st.image(current_img, caption=current_caption, use_column_width=True)
    
    # 按钮布局：上一张 + 下一张
    col1, col2 = st.columns(2)
    with col1:
        st.button("上一张", on_click=prev_image)
    with col2:
        st.button("下一张", on_click=next_image)

# 小组档案页面
def group_profile():
    # 自定义CSS（优化样式）
    st.markdown("""
        <style>
            /* 全局背景与文字颜色 */
            .stApp { background-color: #121212; color: #e0e0e0; }
            /* 模块卡片样式 */
            .card { background-color: #1e1e1e; padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1.5rem; }
            /* 技能进度条 */
            .progress-container { width: 100%; background-color: #333; border-radius: 4px; height: 8px; margin: 0.5rem 0; }
            .progress-bar { height: 100%; border-radius: 4px; }
            /* 任务状态颜色 */
            .status-done { color: #4CAF50; }
            .status-doing { color: #2196F3; }
            .status-fail { color: #F44336; }
            /* 代码块样式 */
            .code-block { background-color: #2d2d2d; padding: 1rem; border-radius: 0.5rem; font-family: monospace; font-size: 0.9rem; }
        </style>
    """, unsafe_allow_html=True)
    
    
    # 页面标题
    st.markdown("<h1 style='text-align: center;'>😁第十八小组档案😁</h1>", unsafe_allow_html=True)
    
    
    # 基础信息模块
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<h2 style='margin-top: 0;'><i class='fa-solid fa-key' style='color: #FFC107; margin-right: 0.5rem;'></i>👧🏻👧🏻基础信息</h2>", unsafe_allow_html=True)
    st.markdown("""
        <p>学生ID: 22053040223</p>
        <p>学生ID: 22053040213</p>
        <p>注册时间: 2025-12-18 08:55:13 <span style='color: #4CAF50; margin-left: 0.5rem;'>| 档案状态: 正常</span></p>
        <p>当前院校: 计算机与信息工程学院 | 安全等级: 超高</p>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    
    # 技能矩阵模块
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<h2 style='margin-top: 0;'><i class='fa-solid fa-chart-simple' style='color: #2196F3; margin-right: 0.5rem;'></i>🏆技能进度</h2>", unsafe_allow_html=True)
    
    # 三列布局展示技能
    col1, col2, col3 = st.columns(3)
    
    # 吃饭
    with col1:
        st.markdown("<p style='margin-bottom: 0.2rem;'>🍛吃饭 <i class='fa-solid fa-arrow-up' style='color: #4CAF50; font-size: 0.8rem;'></i></p>", unsafe_allow_html=True)
        st.markdown("<p style='font-weight: bold; margin-top: 0;'>99%</p>", unsafe_allow_html=True)
        st.markdown("""
            <div class='progress-container'>
                <div class='progress-bar' style='width: 95%; background-color: #4CAF50;'></div>
            </div>
            <p style='font-size: 0.8rem; color: #bbb; margin-top: 0.2rem;'>↑ 2%</p>
        """, unsafe_allow_html=True)
    
    # 睡觉
    with col2:
        st.markdown("<p style='margin-bottom: 0.2rem;'>😴睡觉</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-weight: bold; margin-top: 0;'>99%</p>", unsafe_allow_html=True)
        st.markdown("""
            <div class='progress-container'>
                <div class='progress-bar' style='width: 87%; background-color: #2196F3;'></div>
            </div>
            <p style='font-size: 0.8rem; color: #bbb; margin-top: 0.2rem;'>↓ 1%</p>
        """, unsafe_allow_html=True)
    
    # 打游戏
    with col3:
        st.markdown("<p style='margin-bottom: 0.2rem;'>🎮打游戏<i class='fa-solid fa-arrow-down' style='color: #F44336; font-size: 0.8rem;'></i></p>", unsafe_allow_html=True)
        st.markdown("<p style='font-weight: bold; margin-top: 0;'>99%</p>", unsafe_allow_html=True)
        st.markdown("""
            <div class='progress-container'>
                <div class='progress-bar' style='width: 68%; background-color: #F44336;'></div>
            </div>
            <p style='font-size: 0.8rem; color: #bbb; margin-top: 0.2rem;'>↓ 10%</p>
        """, unsafe_allow_html=True)
    
    # Streamlit课程进度
    st.markdown("<h3 style='margin-top: 1rem; font-size: 1rem;'>Streamlit课程进度</h3>", unsafe_allow_html=True)
    st.markdown("""
        <div class='progress-container'>
            <div class='progress-bar' style='width: 60%; background-color: #9C27B0;'></div>
        </div>
        <p style='font-size: 0.8rem; color: #bbb; margin-top: 0.2rem;'>Streamlit课程进度</p>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    
    # 任务日志模块
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<h2 style='margin-top: 0;'><i class='fa-solid fa-list-check' style='color: #FFC107; margin-right: 0.5rem;'></i>🛎任务日志</h2>", unsafe_allow_html=True)
    
    # 任务表格
    tasks = [
        {"日期": "2024-10-01", "任务": "学生数字档案", "状态": "完成", "难度": "★★★★☆"},
        {"日期": "2025-06-05", "任务": "课程管理系统", "状态": "进行中", "难度": "★★★☆☆"},
        {"日期": "2025-06-12", "任务": "智能图像展示", "状态": "未完成", "难度": "★★★★☆"},
    ]
    
    # 渲染任务行
    for idx, task in enumerate(tasks):
        # 状态图标
        if task["状态"] == "完成":
            status_icon = "<i class='fa-solid fa-check-circle status-done'></i>"
        elif task["状态"] == "进行中":
            status_icon = "<i class='fa-solid fa-circle-notch fa-spin status-doing'></i>"
        else:
            status_icon = "<i class='fa-solid fa-times-circle status-fail'></i>"
        
        st.markdown(f"""
            <div style='display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;'>
                <div style='display: flex; gap: 1rem;'>
                    <span>{idx} {task['日期']}</span>
                    <span>{task['任务']}</span>
                </div>
                <div style='display: flex; gap: 1rem; align-items: center;'>
                    <span>{status_icon} {task['状态']}</span>
                    <span style='color: #FFC107;'>{task['难度']}</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    
    # 最新代码成果模块
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<h2 style='margin-top: 0;'><i class='fa-solid fa-code' style='color: #2196F3; margin-right: 0.5rem;'></i>🚩最新代码成果</h2>", unsafe_allow_html=True)
    
    # 代码块
    code_content = """def matrix_breach():
    while True:
        if detect_vulnerability():
            exploit()
            print("ACCESS GRANTED")
        else:
            stealth_evade()
"""
    st.markdown(f"<div class='code-block'>{code_content}</div>", unsafe_allow_html=True)
    
    # 系统消息
    st.markdown("""
        <p style='color: #4CAF50; font-size: 0.9rem; margin-top: 1rem;'>
            <i class='fa-solid fa-server'></i> SYSTEM MESSAGE: 下一个任务目标已解锁。
        </p>
        <p style='font-size: 0.9rem;'>
            <span style='color: #bbb;'>>> TARGET: </span>课程管理系统
        </p>
        <p style='font-size: 0.9rem;'>
            <span style='color: #bbb;'>>> CONTINUE: </span>2025-06-15 01:24:58
        </p>
        <p style='font-size: 0.9rem; color: #F44336;'>
            系统状态: 在线渗透状态: 已加固
        </p>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# 动漫视频页面
def anime_player():
    # 黑色背景
    st.markdown("""
    <style>
        body, .stApp { background-color: #000000; }
    </style>
    """, unsafe_allow_html=True)
    
    # 三集视频数据
    videos = {
        1: {
            "title": "熊和蝴蝶 - 第1集",
            "url": "https://www.w3school.com.cn/example/html5/mov_bbb.mp4"
        },
        2: {
            "title": "熊过河 - 第2集",
            "url": "https://www.w3schools.com/html/movie.mp4"
        },
        3: {
            "title": "雪山的故事 - 第3集",
            "url": "https://media.w3.org/2010/05/sintel/trailer.mp4"
        }
    }
    
    # 保存当前集数
    if "video_current" not in st.session_state:
        st.session_state.video_current = 1
    
    # 视频标题
    st.markdown(f"""
    <div style="color: white; text-align: center; font-size: 20px; font-weight: bold; margin: 10px 0;">
        {videos[st.session_state.video_current]["title"]}
    </div>
    """, unsafe_allow_html=True)
    
    # 播放视频
    st.video(videos[st.session_state.video_current]["url"])
    
    # 三集选择按钮
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("第1集", use_container_width=True, type="primary" if st.session_state.video_current == 1 else "secondary"):
            st.session_state.video_current = 1
            st.rerun()
    
    with col2:
        if st.button("第2集", use_container_width=True, type="primary" if st.session_state.video_current == 2 else "secondary"):
            st.session_state.video_current = 2
            st.rerun()
    
    with col3:
        if st.button("第3集", use_container_width=True, type="primary" if st.session_state.video_current == 3 else "secondary"):
            st.session_state.video_current = 3
            st.rerun()

# 美食仪表盘页面
def food_dashboard():
    # 自定义深色背景样式
    st.markdown("""
        <style>
        .stApp {
            background-color: #121212;
            color: #ffffff;
        }
        .stHeader {background-color: #1e1e1e;}
        .stSelectbox label, .stSubheader {color: #ffffff;}
        .stMarkdown p, .stMarkdown li {color: #e0e0e0;}
        </style>
    """, unsafe_allow_html=True)
    
    # 数据准备
    # 基础餐厅数据
    restaurants_data = {
        "餐厅": ["星艺会尝不忘", "高峰柠檬鸭", "复记老友粉", "好友缘", "西冷牛排店"],
        "类型": ["中餐", "中餐", "快餐", "自助餐", "西餐"],
        "评分": [4.2, 4.5, 4.0, 4.7, 4.3],
        "人均消费(元)": [15, 20, 25, 35, 50],
        "latitude": [22.853838, 22.965046, 22.812200, 22.809105, 22.839699],
        "longitude": [108.222177, 108.353921, 108.266629, 108.378664, 108.245804]
    }
    df_restaurants = pd.DataFrame(restaurants_data)
    
    # 12个月价格走势数据（5家餐厅，12个月）
    months = [f"{i}月" for i in range(1, 13)]
    price_trend = {"月份": months}
    base_prices = df_restaurants["人均消费(元)"].tolist()
    for i, rest in enumerate(df_restaurants["餐厅"]):
        # 生成基础价格±5%波动的月度数据
        price_trend[rest] = [round(base_prices[i] * random.uniform(0.95, 1.05), 1) for _ in range(12)]
    df_price = pd.DataFrame(price_trend)
    
    # 用餐高峰时段数据（模拟客流量）
    peak_times = ["早餐", "午餐", "下午茶", "晚餐", "夜宵"]
    peak_data = {"时段": peak_times}
    for rest in df_restaurants["餐厅"]:
        # 午餐/晚餐设为高峰值
        peak_data[rest] = [random.randint(10,30), random.randint(80,120), random.randint(20,40), random.randint(90,130), random.randint(30,50)]
    df_peak = pd.DataFrame(peak_data)
    
    # 餐厅推荐菜品 - 使用网络图片替代本地图片
    recommend_dishes = {
        "星艺会尝不忘": {"菜品": "老友粉", "图": "a1.jpg"},
    "高峰柠檬鸭": {"菜品": "柠檬鸭", "图": "a2.jpg"},
    "复记老友粉": {"菜品": "经典老友粉", "图": "a3.jpg"},
    "好友缘": {"菜品": "自助海鲜", "图": "a4.jpg"},
    "西冷牛排店": {"菜品": "西冷牛排", "图": "a5.jpg"}
    }
    
    # 页面模块布局
    st.title("🍲 南宁美食数据仪表盘")
    
    # 1. 餐厅位置地图
    st.subheader("🗺️ 餐厅地理位置")
    st.map(
        df_restaurants[["latitude", "longitude", "餐厅"]],
        latitude="latitude",
        longitude="longitude",
        zoom=11,
        height=280
    )
    
    # 2. 餐厅评分柱状图
    st.subheader("⭐ 餐厅评分")
    st.bar_chart(
        df_restaurants,
        x="餐厅",
        y="评分",
        color="#00BFFF",
        height=250
    )
    
    # 3. 12个月价格走势折线图（5条折线）
    st.subheader("📈 不同餐厅价格走势")
    st.line_chart(
        df_price.set_index("月份"),
        height=250
    )
    
    # 4. 用餐高峰时段面积图
    st.subheader("📊 用餐高峰时段")
    st.area_chart(
        df_peak.set_index("时段"),
        height=250
    )
    
    # 5. 餐厅详情选择器
    st.subheader("🏠 餐厅详情")
    selected_rest = st.selectbox("选择餐厅", df_restaurants["餐厅"])
    rest_detail = df_restaurants[df_restaurants["餐厅"] == selected_rest].iloc[0]
    st.markdown(f"""
    - 餐厅名称：{rest_detail["餐厅"]}
    - 餐饮类型：{rest_detail["类型"]}
    - 评分：{rest_detail["评分"]}/5.0
    - 人均消费：{rest_detail["人均消费(元)"]}元
    """)
    
    # 6. 今日午餐推荐
    st.subheader("🥢 今日午餐推荐")
    dish = recommend_dishes[selected_rest]
    st.image(dish["图"], caption=dish["菜品"], width=700)

# 简历生成器页面
def resume_builder():
    # 应用标题
    st.title("懒洋洋简历生成器")
    
    # 创建两列布局
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("小羊信息表单")
        
        # 基本信息
        st.subheader("基本信息")
        name = st.text_input("姓名", "懒洋洋")
        position = st.text_input("职位", "小羊")
        phone = st.text_input("电话", "888888888")
        email = st.text_input("邮箱", "666666666@qq.com")
        birth_date = st.text_input("出生日期", "羊历3507年6月26日")
        
        col1_1, col1_2 = st.columns(2)
        with col1_1:
            gender = st.selectbox("性别", ["公", "母"], index=0)
            education = st.selectbox("学历", ["高中", "专科", "本科", "硕士", "博士"], index=2)
        
        with col1_2:
            experience = st.selectbox("工作经验", ["无经验", "1年", "2年", "3年", "4年", "5年", "6年", "7年", "8年", "9年", "10年以上"], index=6)
            expected_salary = st.text_input("期望薪资", "9123-25390元")
        
        # 语言能力
        st.subheader("语言能力")
        languages = st.multiselect(
            "选择语言能力",
            ["中文", "英语",  "狼语", "羊语", "蛋语", "老虎语"],
            default=["狼语", "羊语"]
        )
        
        # 专业技能
        st.subheader("小羊技能")
        skills = st.multiselect(
            "选择专业技能",
            ["吃饭", "睡觉", "吃零食", "运动", "美食家", "青草蛋糕品鉴家"],
            default=["吃饭", "睡觉", "美食家", "青草蛋糕品鉴家"]
        )
        
        # 最佳联系时间
        best_time = st.text_input("最佳联系时间", "20:41")
        
        # 个人简介
        st.subheader("个羊简介")
        introduction = st.text_area(
            "个人简介",
    "懒洋洋，青青草原上最可爱的小羊，举重若轻。嗅觉灵敏，一旦闻到食物的香味，马上会被吸引过去。",
            height=150
        )
        
        # 座右铭
        motto = st.text_input("座右铭", "懒洋洋大王")
        
        # 上传照片
        st.subheader("上传个人照片")
        uploaded_file = st.file_uploader("选择图片文件", type=['png', 'jpg', 'jpeg'])
        
        # 下载按钮
        if st.button("生成并下载简历"):
            st.success("简历已生成！下载功能将在后续版本中实现。")
    
    with col2:
        st.header("简历实时预览")
        
        # 简历预览区域
        with st.container():
            st.markdown("---")
            
            # 简历头部信息
            col2_1, col2_2 = st.columns([1, 3])
            with col2_1:
                if uploaded_file is not None:
                    st.image(uploaded_file, width=150)
                else:
                    st.markdown("<div style='width:150px; height:150px; border-radius:50%; background-color:#f0f0f0; display:flex; align-items:center; justify-content:center; font-size:48px;'>👤</div>", unsafe_allow_html=True)
            
            with col2_2:
                st.markdown(f"### {name}")
                st.markdown(f"**{position}**")
                st.markdown(f"📱 {phone} | 📧 {email}")
            
            st.markdown("---")
            
            # 个人信息详情
            st.subheader("个人详情")
            col2_3, col2_4 = st.columns(2)
            with col2_3:
                st.markdown(f"**出生日期**: {birth_date}")
                st.markdown(f"**性别**: {gender}")
                st.markdown(f"**工作经验**: {experience}")
            
            with col2_4:
                st.markdown(f"**学历**: {education}")
                st.markdown(f"**期望薪资**: {expected_salary}")
                st.markdown(f"**最佳联系时间**: {best_time}")
            
            if languages:
                st.markdown(f"**语言能力**: {', '.join(languages)}")
            
            st.markdown("---")
            
            # 个人简介
            st.subheader("个人简介")
            st.write(introduction)
            
            # 专业技能
            st.subheader("专业技能")
            for skill in skills:
                st.markdown(f"- {skill}")
            
            # 座右铭
            if motto:
                st.markdown("---")
                st.markdown(f"> *{motto}*")
    
    # 添加页脚说明
    st.markdown("---")
    st.caption("简历生成器 - 数据会实时更新，左侧表单修改后右侧预览将自动变化")

# 根据选中的顶部导航页面显示对应内容
if st.session_state.current_page == "音乐播放器":
    music_player()
elif st.session_state.current_page == "图片相册":
    image_gallery()
elif st.session_state.current_page == "小组档案":
    group_profile()
elif st.session_state.current_page == "动漫视频":
    anime_player()
elif st.session_state.current_page == "美食仪表盘":
    food_dashboard()
elif st.session_state.current_page == "简历生成器":
    resume_builder()
