import Shapes

choice = input("Enter shape (circle/rectangle/triangle): ").lower()

if choice == "circle":
    r = float(input("Radius: "))
    print(f"Area: {Shapes.circle_area(r)}")
elif choice == "rectangle":
    l, w = float(input("Length: ")), float(input("Width: "))
    print(f"Area: {Shapes.rectangle_area(l, w)}")
elif choice == "triangle":
    b, h = float(input("Base: ")), float(input("Height: "))
    print(f"Area: {Shapes.triangle_area(b, h)}")
