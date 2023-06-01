"""
เขียนโปรแกรมอะไรก็ได้ที่อยาก present Python's skill set เจ๋ง ๆ ของตัวเอง
ข้อนี้ไม่ต้องทำก็ได้ ไม่มีผลลบกับการให้คะแนน แต่ถ้าทำมาเเล้วเจ๋งจริง ก็จะพิจารณาเป็นพิเศษ

"""
import turtle

def draw_concentric_circles():
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    turtle.bgcolor('black')
    turtle.speed(10)

    for i in range(50):
        turtle.color(colors[i % len(colors)])
        turtle.circle(5*i)
        turtle.left(10)

    turtle.hideturtle()
    turtle.done()

# Run the function to see the stunning pattern
draw_concentric_circles()