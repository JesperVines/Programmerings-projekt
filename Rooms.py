"""
MAP:
               0(balcony (key))
1(left wing)   2(ball room)     3(right wing)
4(bedroom)     5(dining room)   6(bedroom with secret door)
                                7(crawlspace)
12(skeleton)   11(cave room)    8(underground cave)
13(cave room)                   9(dead end)
14(room with door)              10(closed room))
15(the great outdoors)
"""


def rooms():

    room_list = []

    # room 0
    room = ["You are standing on a balcony. It's freezing outside.", None, None, 2, None, "r0.png"]
    room_list.append(room)

    # room 1
    room = ["You are standing in the left wing of the house.", None, 2, 4, None, "r1.png"]
    room_list.append(room)

    # room 2
    room = ["You are standing in a big ball room. Many parties have been held here.", 0, 3, 5, 1, "r2.png"]
    room_list.append(room)

    # room 3
    room = ["You are standing in the right wing of the house.", None, None, 6, 2, "r3.png"]
    room_list.append(room)

    # room 4
    room = ["You are standing in a bedroom. There is only one big bed here.", 1, 5, None, None, "r4.png"]
    room_list.append(room)

    # room 5
    room = ["You are standing in the dining room. There is still food on the table.", 2, 6, None, 4, "r5.png"]
    room_list.append(room)

    # room 6
    room = ["You are standing in a bedroom. There are two smaller beds here.", 3, None, 7, 5, "r6.png"]
    room_list.append(room)

    # room 7
    room = ["You are crawling through a small crawlspace. It's very dark here.", 6, None, 8, None, "r7.png"]
    room_list.append(room)

    # room 8
    room = ["You are standing in an big, underground cave room. It's dark and wet in here.", 7, None, 9, 11, "r8.png"]
    room_list.append(room)

    # room 9
    room = ["Yau are standing in a small cave room. It seems to be a dead end.", 8, None, 10, None, "r9.png"]
    room_list.append(room)

    # room 10
    room = ["You are standing in a small, secret room in the cave.", 9, None, None, None, "r10.png"]
    room_list.append(room)

    # room 11
    room = ["You are standing in a narrow, long cave room.", None, 8, None, 12, "r11.png"]
    room_list.append(room)

    # room 12
    room = ["You are standing in a big cave room. There's a pile of bones on the floor.", None, 11, 13, None, "r12.png"]
    room_list.append(room)

    # room 13
    room = ["You are standing in a big cave room. It smells bad in here.", None, None, None, None, "r13.png"]
    room_list.append(room)

    # room 14
    room = ["You are standing in a big cave room. You see a door n front of you.", None, None, None, None, "r14.png"]
    room_list.append(room)

    # room 15
    room = ["You are standing in a forest, in the great outdoors.", None, None, None, None, "r15.png"]
    room_list.append(room)

    return room_list

