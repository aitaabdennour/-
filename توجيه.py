import customtkinter as ctk

# إعداد الثيم
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# البيانات
data = {
    "علوم رياضية A": "الهندسة، الذكاء الاصطناعي، تحليل البيانات، الأمن المعلوماتي، الطيران",
    "علوم رياضية B": "الهندسة الصناعية، البرمجة، الروبوتيك، الرياضيات التطبيقية",
    "علوم تجريبية": "الطب، الصيدلة، التمريض، البيولوجيا، البحث العلمي",
    "علوم اقتصادية": "التجارة، المحاسبة، التسويق، إدارة الأعمال، البنوك",
    "تدبير محاسباتي": "المحاسبة، التدقيق، إدارة الشركات",
    "آداب": "الصحافة، الترجمة، التعليم، القانون، الإعلام",
    "علوم إنسانية": "علم النفس، الاجتماع، التعليم، العمل الاجتماعي",
    "علوم فيزيائية": "الطاقة المتجددة، الهندسة الكهربائية، الفيزياء التطبيقية",
    "علوم الحياة والأرض": "البيئة، الزراعة، البيولوجيا، البحث العلمي",
    "فنون تطبيقية": "التصميم، الغرافيك، تصميم الألعاب، الإشهار"
}

# إنشاء التطبيق
app = ctk.CTk()
app.title("🎓 التوجيه الدراسي")
app.geometry("1000x650")

# العنوان
title = ctk.CTkLabel(
    app,
    text="🎓 نظام التوجيه الدراسي في المغرب",
    font=("Arial", 28, "bold")
)
title.pack(pady=20)

# إطار رئيسي
main_frame = ctk.CTkFrame(app)
main_frame.pack(pady=20, padx=20, fill="both", expand=True)

# إطار الأزرار
buttons_frame = ctk.CTkFrame(main_frame)
buttons_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

# إطار النتيجة
result_frame = ctk.CTkFrame(main_frame)
result_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

# نص النتيجة
result_label = ctk.CTkLabel(
    result_frame,
    text="اختر شعبة من اليسار 👈",
    wraplength=400,
    justify="right",
    font=("Arial", 16)
)
result_label.pack(pady=30, padx=20)

# دالة العرض
def show_result(branch):
    result = data[branch]
    result_label.configure(text=f"📌 {branch}\n\n🎯 الآفاق:\n{result}")

# إنشاء الأزرار
row = 0
col = 0

for branch in data:
    btn = ctk.CTkButton(
        buttons_frame,
        text=branch,
        width=200,
        height=50,
        command=lambda b=branch: show_result(b)
    )
    btn.grid(row=row, column=col, padx=10, pady=10)

    col += 1
    if col == 2:
        col = 0
        row += 1

# زر الخروج
exit_btn = ctk.CTkButton(
    app,
    text="❌ خروج",
    fg_color="red",
    command=app.quit
)
exit_btn.pack(pady=10)

app.mainloop()