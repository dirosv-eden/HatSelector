from pprint import pprint
import random 
from statistics import mean
import names


def generate_house(numbers_of_houses):
    house = []
    for num in range(numbers_of_houses):
        house.append([])
    return house


def selected_children(children_name,numbers_of_house): # เลือกนักเรียนว่าเหมาะสมกับบ้านไหน
    sum_value = 0
    # แปลงตัวอักษรเป็นตัวเลข
    for char in children_name:
        sum_value += (ord(char)) 
    list_sequence_selector_house = [] # สร้างตัวแปรไว้เก็บบ้านตามลำดับความเหมาะสม

    while(True): # วนลูปสุ่มไปเรื่อยๆ จนกว่าจะได้ลำดับบ้านที่ครบทุกหลัง

        # แปลงชื่อเป็นตัวเลขแล้วทำการบวกกับค่าบางค่าแล้ว MOD ด้วย จำนวนบ้าน
        house_index = (sum_value + random.randint(0,20))% numbers_of_house 

        # เช็คว่าบ้านที่ถูกเลือกนั้นอยู่ในลิสแล้วหรือไม่ หากยังไม่มีให้เพิ่มเข้าไปในลิส
        if house_index not in list_sequence_selector_house:
            list_sequence_selector_house.append(house_index)

        # ถ้าจัดลำดับบ้านเสร็จแล้วให้หยุดลูป
        if len(list_sequence_selector_house) == numbers_of_house:
            break

    return list_sequence_selector_house 


def enrolled_children(house,list_house_selected,chrildren):  # ลงทะเบีนนักเรียน

    list_number_of_children_in_house = []
    for index in house:
        list_number_of_children_in_house.append(len(index))

    max_chrildren_in_house = max(list_number_of_children_in_house)
    house_index_max_chrildren = list_number_of_children_in_house.index(max_chrildren_in_house)

    # วนลูปตามลำดับที่หมวกเลือก
    for house_selected in list_house_selected:
        # วนลูปตามลำดับที่หมวกเลือก
        if house_selected != house_index_max_chrildren:
            return house[house_selected].append(chrildren)
            break
    return house[house_selected].append(chrildren)


def queue_chrildern_auto(house_amount,children_amount):
    house = generate_house(house_amount)
    for x in range(children_amount):
        list_selected = selected_children(names.get_full_name(),house_amount)
        enrolled_children(house,list_selected,names.get_full_name())

    for index,x in enumerate(house):
        print("บ้านหลังที่ %s มีนักเรียน %s คน" % (index + 1,len(house[index])))


def queue_chrildern_manual(house_amount,children_amount):
    house = generate_house(house_amount)
    for x in range(children_amount):
        print("นักเรียนชื่อ : ")
        input_children = input()
        list_selected = selected_children(input_children,house_amount)
        enrolled_children(house,list_selected,names.get_full_name())

    for index,x in enumerate(house):
        print("บ้านหลังที่ %s มีนักเรียน %s คน" % (index + 1,len(house[index])))


def main():
    from pick import pick

    title = 'เลือกจำนวนบ้าน '
    options = ['1 หลัง', '2 หลัง','3 หลัง','4 หลัง','5 หลัง','6 หลัง','7 หลัง','8 หลัง','9 หลัง','10 หลัง']
    option_house, index_house = pick(options, title)
    NUMBER_OF_HOUSE = index_house + 1

    title = 'เลือกจำนวนนักเรียน '
    options = ['10','50', '100','200','400']
    option_children, index_children = pick(options, title)
    NUMBER_OF_CHILDREN = int(option_children)


    title = 'เลือกรูปแบบการป้อนข้อมูล'
    options = ['ดึงชุดชื่อนักเรียนแบบอัติโนมัติ', 'ป้อนชื่อนักเรียนด้วยตัวเอง']
    option, index = pick(options, title)
    if index == 0:
        queue_chrildern_auto(NUMBER_OF_HOUSE,NUMBER_OF_CHILDREN)
    if index == 1:
        queue_chrildern_manual(NUMBER_OF_HOUSE,NUMBER_OF_CHILDREN)



if __name__ == "__main__":
    main()