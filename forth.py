import streamlit as st
import time

# 设置页面标题
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
