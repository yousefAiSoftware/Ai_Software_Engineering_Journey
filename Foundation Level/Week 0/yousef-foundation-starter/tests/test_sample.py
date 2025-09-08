from src.week00_hello.main import greet

def test_greet_message():
    out = greet("يوسف")
    assert "أهلًا يوسف" in out
    assert "تم إعداد بيئة العمل بنجاح" in out
