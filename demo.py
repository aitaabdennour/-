import tkinter as tk

# بيانات الشعب والآفاق
data = {
    "علوم رياضية": "الهندسة، البرمجة، الذكاء الاصطناعي، الطيران",
    "علوم تجريبية": "الطب، الصيدلة، البيولوجيا، التمريض",
    "علوم اقتصادية": "التجارة، المحاسبة، إدارة الأعمال",
    "آداب": "الصحافة، التعليم، القانون، الترجمة",
    "علوم إنسانية": "علم النفس، الاجتماع، التعليم"
}

# إنشاء نافذة
root = tk.Tk()
root.title("التوجيه في المغرب")
root.geometry("600x400")

# عنوان (كبرناه)
title = tk.Label(root, text="اختر الشعبة لمعرفة الآفاق", font=("Arial", 20, "bold"))
title.pack(pady=20)

# قائمة اختيار (كبرناها)
selected = tk.StringVar()
selected.set("علوم رياضية")

menu = tk.OptionMenu(root, selected, *data.keys())
menu.config(font=("Arial", 14))
menu.pack(pady=10)

# نتيجة (كبرناها)
result_label = tk.Label(root, text="", font=("Arial", 14), wraplength=450)
result_label.pack(pady=20)

# زر (كبرناه)
def show_result():
    choice = selected.get()
    result = data[choice]
    result_label.config(text=f"الآفاق:\n{result}")

btn = tk.Button(root, text="عرض الآفاق", font=("Arial", 14), command=show_result)
btn.pack()

root.mainloop()