from pprint import pprint
import random 
house = dict()
house[0] = []
house[1] = []
house[2] = []
house[3] = []


def selector_rules(inputString):

    sum_value = 0

    # แปลงตัวอักษรเป็นตัวเลข
    for char in inputString:
        sum_value += (ord(char)) 

    # จัดลำดับบ้านที่ควรอยู่เป็นรูปแบบ list เรียงตามความเหมาะสม
    list_sequnce = []

    # สุ่มไปเรื่อยๆ จนกว่าจะได้ลำดับบ้านที่ครบ 4 หลัง
    while(True):
        house_index = (sum_value + random.randint(0,20))% 4
        if house_index not in list_sequnce:
            list_sequnce.append(house_index)
        if len(list_sequnce) == 4:
            break
    return list_sequnce




def enroll_chrildren_in_house(list_house_selected,chrildren):
    # ลงทะเบียนนักเรียนลงบ้าน
    list_house = [len(house[0]),len(house[1]),len(house[2]),len(house[3])]
    min_chrildren = list_house.index(min(list_house));

    # วนลูปตามลำดับที่หมวกเลือก
    for house_selected in list_house_selected:
        # วนลูปตามลำดับที่หมวกเลือก
        if house_selected == min_chrildren:
            house[min_chrildren].append(chrildren)


def queue_chrildern(count_chrildren):
    # วนลูปรับค่านักเรียน
    for index in range(count_chrildren):
        print("What is your name : ")
        chrildren = input()
        list_house_selected = selector_rules(chrildren)
        enroll_chrildren_in_house(list_house_selected,chrildren)
        pprint(house)



def queue_chrildern_test(count_chrildren):
    # วนลูปทดสอบ
    for index in range(count_chrildren):
        import names
        chrildren = names.get_full_name()
        list_house_selected = selector_rules(chrildren)
        enroll_chrildren_in_house(list_house_selected,chrildren)

    for index in house:
        print("บ้านหลังที่ %s มีนักเรียน %s คน" % (index,len(house[index])))


queue_chrildern_test(170)
