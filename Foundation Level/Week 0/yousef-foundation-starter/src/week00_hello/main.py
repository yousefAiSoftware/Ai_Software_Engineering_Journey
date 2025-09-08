from datetime import datetime

def greet(name: str) -> str:
    return f"أهلًا {name}! ✅ تم إعداد بيئة العمل بنجاح — {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

if __name__ == "__main__":
    print(greet("يوسف"))
