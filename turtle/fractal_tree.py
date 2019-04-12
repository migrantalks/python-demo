import turtle


# 树枝大小、颜色
def draw_color_branch(branch_length):
    if branch_length < 40:
        turtle.color('green')
        turtle.pensize(1)
    else:
        turtle.color('brown')
        turtle.pensize(2)


# 画树枝
def draw_branch(branch_length):
    if branch_length > 5:

        draw_color_branch(branch_length)

        # 绘制右侧的树枝
        print('向前', branch_length)
        turtle.forward(branch_length)

        print('右转 20')
        turtle.right(20)
        draw_branch(branch_length - 15)

        # 绘制左侧的树枝
        print('左转 40')
        turtle.left(40)
        draw_branch(branch_length - 15)

        draw_color_branch(branch_length)

        # 返回之前的树枝上
        print('右转 20')
        turtle.right(20)

        print('返回', branch_length)
        turtle.backward(branch_length)


# 主函数
def main():
    turtle.left(90)
    turtle.penup()
    turtle.backward(240)
    turtle.pendown()
    turtle.color('red')

    draw_branch(120)

    turtle.exitonclick()


if __name__ == '__main__':
    main()
