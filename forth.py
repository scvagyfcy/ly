import streamlit as st

# 设置页面标题
st.title("我的图片相册")

# 准备图片数据：列表中每个元素是(图片路径, 图注)
# 注意：请将这里的图片路径替换为你本地的图片路径，或使用网络图片URL
image_data = [
    ("cat1.jpg", "橘白相间的猫咪，正慵懒地晒太阳"),
    ("dog.jpg", "活泼的小狗在草地上奔跑"),
    ("flower.jpg", "盛放的向日葵，充满生机")
]

# 初始化会话状态，记录当前显示的图片索引
if "current_idx" not in st.session_state:
    st.session_state.current_idx = 0

# 定义切换图片的函数
def prev_image():
    st.session_state.current_idx = (st.session_state.current_idx - 1) % len(image_data)

def next_image():
    st.session_state.current_idx = (st.session_state.current_idx + 1) % len(image_data)

# 显示当前图片和图注
current_img, current_caption = image_data[st.session_state.current_idx]
st.image(current_img, caption=current_caption, use_column_width=True)

# 按钮布局：上一张 + 下一张
col1, col2 = st.columns(2)
with col1:
    st.button("上一张", on_click=prev_image)
with col2:
    st.button("下一张", on_click=next_image)
