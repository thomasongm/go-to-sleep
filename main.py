def on_gesture_shake():
    basic.show_icon(IconNames.SAD)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_forever():
    if input.light_level() == 0:
        basic.show_icon(IconNames.ASLEEP)
    else:
        basic.show_icon(IconNames.HAPPY)
basic.forever(on_forever)
