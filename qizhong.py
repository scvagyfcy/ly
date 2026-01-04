import pandas as pd
import pickle
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

# 设置页面配置
st.set_page_config(page_title="学生成绩分析", page_icon="🏥", layout="wide")

# 初始化 session_state
if 'ind' not in st.session_state:
    st.session_state['ind'] = 0

# 创建侧边栏导航
nav = st.sidebar.radio("导航菜单", ["项目介绍", "专业数据分析", "成绩预测"])
# 设置 pandas 显示选项，确保中文字符在终端或页面显示时宽度正常，不乱码
pd.set_option('display.unicode.east_asian_width', True)

def introduce_page():
    """
    应用介绍页面
    显示应用的欢迎信息和背景介绍
    """
    st.markdown(
        """
        # 学生成绩分析与预测系统
        """
    )
    # 分割线
    st.markdown('***')
    left_col, right_col = st.columns(2)
    with left_col:
        st.markdown(
            """
            ### 🗒️项目概述
           
            本项目是一个基于streamlit的学生成绩分析平台，通过数据可视化和机器学习技术，帮助教育工作者和学生深入了解学业表现，并预测期末考试成绩。
            """
        )
        st.markdown(
            """
            ### ✨主要特点
            - 📊 数据可视化：多维度展示学生学业数据
            - 📚 专业分析：按专业分类的详细统计分析
            - 🧠 智能预测：基于机器学习模型的成绩预测
            - 💡 学习建议：根据预测结果提供个性化反馈
           
            """
        )
    
    with right_col:
        img_data = [
            {
                'img': '1.png',
            },
            {
                'img': '2.png',
            },
            {
                'img': '3.png',
            },
        ]
       
        def nextImg():
            st.session_state['ind'] = (st.session_state['ind'] + 1) % len(img_data)
       
        def prevImg():
            st.session_state['ind'] = (st.session_state['ind'] - 1 + len(img_data)) % len(img_data)
       
        st.image(img_data[st.session_state['ind']]['img'], use_container_width=True)
       
        button_col1, button_col2 = st.columns(2)
       
        with button_col1:
            st.button('上一张', use_container_width=True, on_click=prevImg)

        with button_col2:
            st.button('下一张', use_container_width=True, on_click=nextImg)
   
    # 分割线
    st.markdown('***')
    st.markdown('### 🎯 项目目标')
   
    # 创建三列布局
    col_1, col_2, col_3 = st.columns(3)
   
    with col_1:
        st.markdown("""
        #### 🎯 目标一：分析影响因素
        - 识别关键学习指标
        - 探索成绩相关因素
        - 提供数据支持决策
        """)
   
    with col_2:
        st.markdown("""
        #### 🎯 目标二：可视化展示
        - 专业对比分析
        - 性别差异研究
        - 学习模式识别
        """)
   
    with col_3:
        st.markdown("""
        #### 🎯 目标三：成绩预测
        - 机器学习模型
        - 个性化预测
        - 及时干预预警
        """)
   
    # 分割线
    st.markdown('***')
    st.markdown('### 🛠️ 技术架构')
   
    # 创建四列布局
    col_1_1, col_2_1, col_3_1, col_4_1 = st.columns(4)
    with col_1_1:
        st.subheader('前端框架')
        qianduan_code = 'Streamlit'
        st.code(qianduan_code)
    with col_2_1:
        st.subheader('数据处理')
        shujuchuli = 'Pandas、NumPy'
        st.code(shujuchuli)
    with col_3_1:
        st.subheader('可视化')
        keshihua = 'Plotly、Matplotlib'
        st.code(keshihua)
    with col_4_1:
        st.subheader('机器学习')
        Scikit = 'Scikit-learn'
        st.code(Scikit)

def data_chart():
    """
    专业数据分析页面
    显示各种专业相关的数据分析和可视化图表
    """
    # 从CSV文件读取数据 - 核心修改：增强编码适配逻辑
    df = None
    # 定义常见的中文文件编码列表（按优先级排序）
    encodings = ['utf-8-sig', 'gbk', 'gb2312', 'utf-8', 'latin-1']
    
    for encoding in encodings:
        try:
            df = pd.read_csv('student_data_adjusted_rounded.csv', encoding=encoding)
            # 验证数据是否读取成功
            if not df.empty:
                st.success(f"✅ 成功读取文件，使用编码：{encoding}")
                break  # 读取成功则退出循环
        except FileNotFoundError:
            st.error("❌ 找不到 student_data_adjusted_rounded.csv 文件，请确保文件在同一目录下")
            return
        except UnicodeDecodeError:
            # 该编码失败，继续尝试下一个
            continue
        except Exception as e:
            st.warning(f"⚠️ 使用 {encoding} 编码读取时出错：{str(e)}，尝试下一个编码...")
            continue
    
    # 如果所有编码都尝试失败
    if df is None or df.empty:
        st.error("❌ 所有编码都无法读取文件，请检查文件是否损坏或格式是否正确")
        return
   
    # 1. 各专业男女性别比例
    st.markdown('### 1. 各专业男女性别比例')
   
    # 计算各专业男女比例
    gender_ratio = df.groupby(['专业', '性别']).size().unstack(fill_value=0)
    gender_ratio['男性比例'] = gender_ratio['男'] / (gender_ratio['男'] + gender_ratio['女'])
    gender_ratio['女性比例'] = gender_ratio['女'] / (gender_ratio['男'] + gender_ratio['女'])
   
    # 创建图表和表格的左右布局
    col1, col2 = st.columns([2, 1])  # 图表占2份，表格占1份
   
    with col1:
        # 创建柱状图
        fig1 = go.Figure()
        fig1.add_trace(go.Bar(
            x=gender_ratio.index,
            y=gender_ratio['男性比例'],
            name='男性比例',
            marker_color='royalblue'
        ))
        fig1.add_trace(go.Bar(
            x=gender_ratio.index,
            y=gender_ratio['女性比例'],
            name='女性比例',
            marker_color='skyblue'
        ))
       
        fig1.update_layout(
            title='各专业男女性别比例',
            xaxis_title='专业',
            yaxis_title='比例',
            barmode='group',
            height=400
        )
       
        st.plotly_chart(fig1, use_container_width=True)
   
    with col2:
        # 显示数据表格
        st.dataframe(gender_ratio[['男性比例', '女性比例']].round(4))
   
    # 2. 各专业学习指标对比
    st.markdown('### 2. 各专业学习指标对比')
   
    # 计算各专业平均学习指标 - 使用正确的列名
    study_metrics = df.groupby('专业').agg({
        '期中考试分数': 'mean',      # F列
        '期末考试分数': 'mean',      # I列
        '每周学习时长（小时）': 'mean'        # D列
    }).reset_index()
   
    # 创建图表和表格的左右布局
    col1, col2 = st.columns([2, 1])  # 图表占2份，表格占1份
   
    with col1:
        # 创建折线图
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(
            x=study_metrics['专业'],
            y=study_metrics['期中考试分数'],
            mode='lines+markers',
            name='期中考试分数',
            line=dict(color='royalblue')
        ))
        fig2.add_trace(go.Scatter(
            x=study_metrics['专业'],
            y=study_metrics['期末考试分数'],
            mode='lines+markers',
            name='期末考试分数',
            line=dict(color='red')
        ))
        fig2.add_trace(go.Scatter(
            x=study_metrics['专业'],
            y=study_metrics['每周学习时长（小时）'],
            mode='lines+markers',
            name='每周学习时长(小时)',
            line=dict(color='green'),
            yaxis='y2'
        ))
       
        fig2.update_layout(
            title='各专业学习指标对比',
            xaxis_title='专业',
            yaxis_title='分数',
            yaxis2=dict(
                title='每周学习时长(小时)',
                overlaying='y',
                side='right'
            ),
            height=400
        )
       
        st.plotly_chart(fig2, use_container_width=True)
   
    with col2:
        # 显示数据表格
        st.dataframe(study_metrics.round(2))
   
    # 3. 各专业出勤率分析
    st.markdown('### 3. 各专业出勤率分析')
   
    # 计算各专业平均出勤率 - 使用正确的列名
    attendance = df.groupby('专业')['上课出勤率'].mean().reset_index()  # E列
   
    # 创建图表和表格的左右布局
    col1, col2 = st.columns([2, 1])  # 图表占2份，表格占1份
   
    with col1:
        # 创建柱状图
        fig3 = px.bar(
            attendance,
            x='专业',
            y='上课出勤率',
            color='上课出勤率',
            color_continuous_scale='Greens'
        )
       
        fig3.update_layout(
            title='各专业出勤率分析',
            xaxis_title='专业',
            yaxis_title='平均出勤率',
            height=400
        )
       
        st.plotly_chart(fig3, use_container_width=True)
   
    with col2:
        # 显示数据表格
        st.dataframe(attendance.round(4))
   
    # 4. 大数据管理专业专项分析
    st.markdown('### 4. 大数据管理专业专项分析')
   
    # 筛选大数据管理专业的数据
    big_data_df = df[df['专业'] == '大数据管理']
   
    # 计算统计数据 - 使用正确的列名
    avg_attendance = big_data_df['上课出勤率'].mean() * 100  # E列
    avg_final_score = big_data_df['期末考试分数'].mean()     # I列
    pass_rate = (big_data_df['期末考试分数'] >= 60).mean() * 100
    avg_study_hours = big_data_df['每周学习时长（小时）'].mean()     # D列
   
    # 显示关键指标
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("平均出勤率", f"{avg_attendance:.1f}%")
    with col2:
        st.metric("平均期末分数", f"{avg_final_score:.1f}分")
    with col3:
        st.metric("通过率", f"{pass_rate:.1f}%")
    with col4:
        st.metric("平均学习时长", f"{avg_study_hours:.1f}小时")
   
    # 期末成绩分布
    st.markdown('#### 大数据管理专业期末成绩分布')
   
    # 创建图表和表格的左右布局
    col1, col2 = st.columns(2)  # 图表占2份，表格占1份
   
    with col1:
        fig4 = px.histogram(
            big_data_df,
            x='期末考试分数',  # I列
            nbins=10,
            color_discrete_sequence=['royalblue']
        )
       
        fig4.update_layout(
            title='大数据管理专业期末成绩分布',
            xaxis_title='期末考试分数',
            yaxis_title='人数',
            height=600
        )
       
        st.plotly_chart(fig4, use_container_width=True)
   
    with col2:
        st.markdown('#### 大数据管理专业学习时长分布')
        # 将学习时长分组统计
        study_hours_bins = pd.cut(big_data_df['每周学习时长（小时）'],
                                  bins=10,
                                  labels=False) + 1
        study_hours_count = study_hours_bins.value_counts().sort_index()
       
        fig5 = px.bar(
            x=study_hours_count.index,
            y=study_hours_count.values,
            labels={'x': '学习时长区间', 'y': '人数'},
            color_discrete_sequence=['royalblue']
        )
 
        st.plotly_chart(fig5, use_container_width=True)

def grade_prediction():
    """
    成绩预测页面
    使用机器学习模型预测学生期末成绩
    """
    st.markdown("### 🧠 成绩预测")
   
    try:
        with open('grade_prediction_model.pkl', 'rb') as f:
            model_data = pickle.load(f)
       
        model = model_data['model']
        le_gender = model_data['le_gender']
        le_major = model_data['le_major']
       
    except FileNotFoundError:
        st.error("❌ 找不到模型文件 'grade_prediction_model.pkl'，请先运行训练脚本")
        return
    except Exception as e:
        st.error(f"❌ 加载模型时出错: {e}")
        return
   
    st.markdown("#### 请输入学生信息")
   
    col1, col2 = st.columns(2)
   
    with col1:
        student_id = st.text_input("学号", placeholder="请输入学号", max_chars=20)
        gender = st.selectbox("性别", ["男", "女"])
        major = st.selectbox("专业", ["工商管理", "人工智能", "财务管理", "电子商务", "大数据管理"])
        study_hours = st.slider("每周学习时长（小时）", 0.0, 50.0, 15.0, 0.5)
   
    with col2:
        attendance = st.slider("上课出勤率", 0.0, 1.0, 0.85, 0.01)
        mid_score = st.slider("期中考试分数", 0.0, 100.0, 75.0, 0.5)
        homework_rate = st.slider("作业完成率", 0.0, 1.0, 0.85, 0.01)
   
    if st.button("🔮 预测成绩", type="primary"):
        gender_encoded = le_gender.transform([gender])[0]
        major_encoded = le_major.transform([major])[0]
       
        input_data = pd.DataFrame({
            '性别_encoded': [gender_encoded],
            '专业_encoded': [major_encoded],
            '每周学习时长（小时）': [study_hours],
            '上课出勤率': [attendance],
            '期中考试分数': [mid_score],
            '作业完成率': [homework_rate]
        })
       
        predicted_score = model.predict(input_data)[0]
       
        st.markdown('***')
        st.markdown("### 📊 预测结果")
       
        col1, col2, col3 = st.columns(3)
       
        with col1:
            st.metric(
                "预测期末成绩",
                f"{predicted_score:.1f}分",
                delta=f"{'+' if predicted_score >= 60 else ''}{predicted_score - 60:.1f}分"
            )
       
        with col2:
            if predicted_score >= 90:
                grade = "优秀"
                color = "🌟"
            elif predicted_score >= 80:
                grade = "良好"
                color = "👍"
            elif predicted_score >= 70:
                grade = "中等"
                color = "😊"
            elif predicted_score >= 60:
                grade = "及格"
                color = "✅"
            else:
                grade = "不及格"
                color = "⚠️"
            st.metric("等级评定", f"{color} {grade}")
       
        with col3:
            if predicted_score >= 60:
                status = "通过"
                delta_color = "normal"
            else:
                status = "未通过"
                delta_color = "inverse"
            st.metric("考试状态", status, delta_color=delta_color)
       
        st.markdown('***')
        st.markdown("### 💡 学习建议")
       
        col_center = st.columns([1, 2, 1])
       
        with col_center[1]:
            if predicted_score >= 90:
                st.success("🎉 优秀等级")
                st.image("33.jpg", caption="优秀表现", width=500)
            elif predicted_score >= 80:
                st.success("👏 良好等级")
                st.image("11.jpg", caption="良好表现", width=500)
            elif predicted_score >= 70:
                st.info("📚 中等等级")
                st.image("11.jpg", caption="中等表现", width=500)
            elif predicted_score >= 60:
                st.warning("⚡ 及格等级")
                st.image("44.jpg", caption="及格表现", width=500)
            else:
                st.error("❌ 不及格等级")
                st.image("22.jpg", caption="需要努力", width=500)

# 根据导航选择显示不同页面
if nav == "项目介绍":
    introduce_page()
elif nav == "专业数据分析":
    data_chart()
else:
    grade_prediction()
