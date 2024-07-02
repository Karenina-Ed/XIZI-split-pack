from utils import *

boxLength=12000
boxWidth=2566
scale_factor = 1
elevation_height = 11500
truss_height = 982
height = 1018
lower_slope_length = 2025
upper_extension_length = 0
lower_extension_length = 0
degree = 30
num=2 # 梯数
if __name__ == "__main__":
    # 初始化显示
    display, start_display, add_menu, add_function_to_menu = init_display()
    boxNum=2
    boxes=[]
    for _ in range(boxNum):
        boxes.append(Box(12000, 2000, 2566))
    # elevations=[]
    elevation = Elevation(elevation_height, height, truss_height, upper_extension_length, lower_extension_length, degree, scale_factor)
    elevation.shape = cs(elevation_height, height, truss_height, upper_extension_length, lower_extension_length, degree, scale_factor)

    #每个梯子要分割的点的索引
    elevationSplit={}  # 记载所有扶梯的分割块 字典形式记录
    split_points=splitElevation(elevation, elevationSplit, 0)  # 这个传的是实际切的点
    # display.DisplayShape(elevationSplit[0][1],color="green",update=True,transparency=0.2)  # i个梯子的上半部
    if(len(split_points)==2):
        threePack(elevationSplit[0], display, boxes)
    if(len(split_points)==0):
        midPack(elevationSplit[0])# 这里写直接装进去的
    # bestLongPack(elevationSplit[0])
    if(len(split_points)==1):  
        midPack(elevationSplit[0])
    for box in boxes:
        display.DisplayShape(box.shape, color='blue', transparency=0.9)  # 箱子半透明显示
    display.View.SetScale(0.05)  #视图缩小
    # 启动显示
    start_display()