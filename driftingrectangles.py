def drift_rectangles(rectangles):
    output_rectangle_list = []
    for rectangle in rectangles["rectangles"]:
        output_rectangle_list.append(drift_rectangle(rectangle))
    return {
        "rectangles": output_rectangle_list
        }

def drift_rectangle(rectangle):
    return rectangle
