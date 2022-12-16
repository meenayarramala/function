def function(speed):
    if speed<=70:
        print("ok")
    if speed>70:
        i=70
        while i<=70:
            point=(speed-70)//5
            if point>12:
                print(point,speed,"License suspended")
            else:
                print(point,speed,"ok")
            i=i+1
speed=int(input("enter the number"))
function(speed)