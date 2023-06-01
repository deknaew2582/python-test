
"""
Convert Number to Thai Text.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลข เป็นตัวหนังสือภาษาไทย
โดยที่ค่าที่รับต้องมีค่ามากกว่าหรือเท่ากับ 0 และน้อยกว่า 10 ล้าน

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""
#


def convert_number_to_thai_text(number):
    number_thai_text = ""
    if number < 0 or number > 10000000:
        return None
    number_text = str(number)
    lenNumber = len(number_text)
    if lenNumber == 1:  # หน่วย
        if number == 0:
            number_thai_text = "ศูนย์"
        else:
            number_thai_text = get_thai_text_by_number(number)
    elif lenNumber == 2:
        if int(number_text[0]) == 1:
            number_thai_text = "สิบ" + \
                get_thai_text_by_number(int(number_text[1]))
        elif int(number_text[0]) == 2:
            number_thai_text = "ยี่สิบ" + \
                get_thai_text_by_number(int(number_text[1]))
        else:
            number_thai_text = get_thai_text_by_number(
                int(number_text[0])) + "สิบ"+get_thai_text_by_number(int(number_text[1]))
    elif lenNumber == 3:
        number_thai_text = get_thai_text_by_number(int(number_text[0])) + "ร้อย"+get_thai_text_by_number(
            int(number_text[1])) + "สิบ"+get_thai_text_by_number(int(number_text[2]))
    elif lenNumber == 4:
        number_thai_text = get_thai_text_by_number(int(number_text[0])) + "พัน"+get_thai_text_by_number(int(
            number_text[1])) + "ร้อย"+get_thai_text_by_number(int(number_text[2])) + "สิบ"+get_thai_text_by_number(int(number_text[3]))
    elif lenNumber == 5:
        number_thai_text = get_thai_text_by_number(int(number_text[0])) + "หมื่น"+get_thai_text_by_number(int(number_text[1])) + "พัน"+get_thai_text_by_number(
            int(number_text[2]))+"ร้อย"+get_thai_text_by_number(int(number_text[3])) + "สิบ"+get_thai_text_by_number(int(number_text[4]))
    elif lenNumber == 6:
        number_thai_text = get_thai_text_by_number(int(number_text[0])) + "แสน"+get_thai_text_by_number(int(number_text[1])) + "หมื่น"+get_thai_text_by_number(int(
            number_text[2]))+"พัน"+get_thai_text_by_number(int(number_text[3])) + "ร้อย"+get_thai_text_by_number(int(number_text[4]))+"สิบ"+get_thai_text_by_number(int(number_text[5]))
    elif lenNumber == 7:  # ล้าน
        number_thai_text = get_thai_text_by_number(int(number_text[0])) + "ล้าน"+get_thai_text_by_number(int(number_text[1])) + "แสน"+get_thai_text_by_number(int(number_text[2]))+"หมื่น"+get_thai_text_by_number(
            int(number_text[3])) + "พัน"+get_thai_text_by_number(int(number_text[4]))+"ร้อย"+get_thai_text_by_number(int(number_text[5]))+"สิบ"+get_thai_text_by_number(int(number_text[6]))

    if lenNumber > 1:
        findTail = number_thai_text.find("หนึ่ง", lenNumber-len('หนึ่ง'))
        if findTail != -1:
            number_thai_text = number_thai_text[:findTail] + "เอ็ด"
    return number_thai_text


def get_thai_text_by_number(unit):
    if unit < 0:
        return None
    unit_text = ""
    if unit == 1:
        unit_text = "หนึ่ง"
    elif unit == 2:
        unit_text = "สอง"
    elif unit == 3:
        unit_text = "สาม"
    elif unit == 4:
        unit_text = "สี่"
    elif unit == 5:
        unit_text = "ห้า"
    elif unit == 6:
        unit_text = "หก"
    elif unit == 7:
        unit_text = "เจ็ด"
    elif unit == 8:
        unit_text = "แปด"
    elif unit == 9:
        unit_text = "เก้า"
    return unit_text


if __name__ == "__main__":
    inputNumber = 23
    print(inputNumber, "in Thai text is",
          convert_number_to_thai_text(inputNumber))
