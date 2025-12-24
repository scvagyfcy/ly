import streamlit as st

# 设置页面配置
st.set_page_config(page_title="羊羊简历", page_icon="📄", layout="wide")

# 应用标题
st.title("懒洋洋")


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
