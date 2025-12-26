import streamlit as st

# ---------------------- 页面配置 ----------------------
st.set_page_config(
    page_title="第十八小组档案",
    layout="centered",  # 居中布局（默认占80%宽度，正好满足“左右各20%空间”）
    initial_sidebar_state="collapsed"
)

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


# ---------------------- 页面标题 ----------------------
st.markdown("<h1 style='text-align: center;'>😁第十八小组档案😁</h1>", unsafe_allow_html=True)


# ---------------------- 基础信息模块 ----------------------
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("<h2 style='margin-top: 0;'><<i class='fa-solid fa-key' style='color: #FFC107; margin-right: 0.5rem;'></</i>👧🏻👧🏻基础信息</h2>", unsafe_allow_html=True)
st.markdown("""
    <p>学生ID: 22053040223</p>
    <p>学生ID: 22053040213</p>
    <p>注册时间: 2025-12-18 08:55:13 <span style='color: #4CAF50; margin-left: 0.5rem;'>| 档案状态: 正常</span></p>
    <p>当前院校: 计算机与信息工程学院 | 安全等级: 超高</p>
""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)


# ---------------------- 技能矩阵模块 ----------------------
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("<h2 style='margin-top: 0;'><<i class='fa-solid fa-chart-simple' style='color: #2196F3; margin-right: 0.5rem;'></</i>🏆技能进度</h2>", unsafe_allow_html=True)

# 三列布局展示技能
col1, col2, col3 = st.columns(3)

# 吃饭
with col1:
    st.markdown("<p style='margin-bottom: 0.2rem;'>🍛吃饭 <<i class='fa-solid fa-arrow-up' style='color: #4CAF50; font-size: 0.8rem;'></</i></p>", unsafe_allow_html=True)
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
    st.markdown("<p style='margin-bottom: 0.2rem;'>🎮打游戏<<i class='fa-solid fa-arrow-down' style='color: #F44336; font-size: 0.8rem;'></</i></p>", unsafe_allow_html=True)
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


# ---------------------- 任务日志模块 ----------------------
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("<h2 style='margin-top: 0;'><<i class='fa-solid fa-list-check' style='color: #FFC107; margin-right: 0.5rem;'></</i>🛎任务日志</h2>", unsafe_allow_html=True)

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
        status_icon = "<<i class='fa-solid fa-check-circle status-done'></</i>"
    elif task["状态"] == "进行中":
        status_icon = "<<i class='fa-solid fa-circle-notch fa-spin status-doing'></</i>"
    else:
        status_icon = "<<i class='fa-solid fa-times-circle status-fail'></</i>"
    
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


# ---------------------- 最新代码成果模块 ----------------------
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("<h2 style='margin-top: 0;'><<i class='fa-solid fa-code' style='color: #2196F3; margin-right: 0.5rem;'></</i>🚩最新代码成果</h2>", unsafe_allow_html=True)

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
        <<i class='fa-solid fa-server'></</i> SYSTEM MESSAGE: 下一个任务目标已解锁。
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
