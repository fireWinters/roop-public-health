'''
Author: Diana Tang
Date: 2024-09-23 01:02:04
LastEditors: Diana Tang
Description: 环境是roop-env
FilePath: /roop-public-health/test.py
'''
import customtkinter as ctk

# 创建主窗口
app = ctk.CTk()
app.geometry("400x300")

# 添加一个按钮测试
button = ctk.CTkButton(app, text="Test Button")
button.pack(pady=20)

app.mainloop()
