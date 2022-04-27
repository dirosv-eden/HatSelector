from pprint import pprint
import random 
from statistics import mean


# CONFIG 

NUMBER_OF_HOUSE = 4


# INITIAL VARIABLE

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


    list_sequence_selector_house = [] # สร้างตัวแปรไว้เก็บบ้านตามลำดับความสำคัญ

    
    while(True): # วนลูปสุ่มไปเรื่อยๆ จนกว่าจะได้ลำดับบ้านที่ครบ 4 หลัง

        # แปลงชื่อเป็นตัวเลขแล้วทำการบวกกับค่าบางค่าแล้ว MOD ด้วย จำนวนบ้าน
        house_index = (sum_value + random.randint(0,20))% NUMBER_OF_HOUSE 

        # เช็คว่าบ้านที่ถูกเลือกนั้นอยู่ในลิสแล้วหรือไม่ หากยังไม่มีให้เพิ่มเข้าไปในลิส
        if house_index not in list_sequence_selector_house:
            list_sequence_selector_house.append(house_index)

        # ถ้าจัดลำดับบ้านเสร็จแล้วให้หยุดลูป
        if len(list_sequence_selector_house) == NUMBER_OF_HOUSE:
            break

    return list_sequence_selector_house 



def enroll_chrildren_in_house(list_house_selected,chrildren):
    # ลงทะเบียนนักเรียนลงบ้าน
    list_number_of_children_in_house = [len(house[0]),len(house[1]),len(house[2]),len(house[3])]
    max_chrildren_in_house = max(list_number_of_children_in_house)
    house_index_max_chrildren = list_number_of_children_in_house.index(max_chrildren_in_house)

    # วนลูปตามลำดับที่หมวกเลือก
    for house_selected in list_house_selected:
        # วนลูปตามลำดับที่หมวกเลือก
        if house_selected != house_index_max_chrildren:
            house[house_selected].append(chrildren)
            break
    return house_selected


def queue_chrildern(count_chrildren):
    # วนลูปรับค่านักเรียน
    for index in range(count_chrildren):
        print("ชื่อของนักเรียน : ")
        chrildren = input()
        list_house_selected = selector_rules(chrildren)
        house_chrildren = enroll_chrildren_in_house(list_house_selected,chrildren)
        print("%s ได้ถูกคัดเลือกไปบ้านหลังที่ %s" % (chrildren,house_chrildren + 1))

    for index in house:
        print("บ้านหลังที่ %s มีนักเรียน %s คน" % (index + 1,len(house[index])))



# def queue_chrildern_test(count_chrildren):
#     # วนลูปทดสอบ
#     for index in range(count_chrildren):
#         import names
#         chrildren = names.get_full_name()
#         list_house_selected = selector_rules(chrildren)
#         enroll_chrildren_in_house(list_house_selected,chrildren)

#     for index in house:
#         print("บ้านหลังที่ %s มีนักเรียน %s คน" % (index + 1,len(house[index])))

queue_chrildern(50)
