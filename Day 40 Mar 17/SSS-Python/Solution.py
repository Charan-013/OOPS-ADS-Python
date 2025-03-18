from functools import cmp_to_key
import datetime

class Student:
    def __init__(self,name,dob,sub1,sub2,sub3,total,rc):
        self.name = name
        self.dob = datetime.datetime.strptime(dob, '%d-%m-%Y').date()
        self.sub1 = int(sub1)
        self.sub2 = int(sub2)
        self.sub3 = int(sub3)
        self.total = int(total)
        self.rc = rc

    def __str__(self):
        return f"{self.name},{self.total},{self.rc}"
    

def compare_decending_merit_order(student1,student2):
    
    if student1.total < student2.total:
        return 1
    elif student1.total > student2.total:
        return -1
    
    if student1.sub3 < student2.sub3:
        return 1
    elif student1.sub3 > student2.sub3:
        return -1
    
    if student1.sub2 < student2.sub2:
        return 1
    elif student1.sub2 > student2.sub2:
        return -1
    elif student1.total == student2.total:
        # if student1.name > student2.name:
        #     return 1
        # if student1.name < student2.name:
        #     return -1
        if student1.dob < student2.dob:
            return 1
        elif student1.dob > student2.dob:
            return -1
    elif student1.total == student2.total:
        if student1.name > student2.name:
            return 1
        if student1.name < student2.name:
            return -1
        # if student1.dob < student2.dob:
        #     return 1
        # elif student1.dob > student2.dob:
        #     return -1
    
    if student1.name < student2.name:
        return 1
    if student1.name > student2.name:
        return -1
    
    if student1.dob > student2.dob:
        return 1
    elif student1.dob < student2.dob:
        return -1

    else:
        return 0 

def fill_vacancies(students_list, total_vacancies, UR_vacancies, BC_vacancies, SC_vacancies, ST_vacancies):
    lst = []
    for i in range(UR_vacancies):
        lst.append(students_list[i])
    
    remaining_list = [ele for ele in students_list if ele not in lst]
    remaining_vacancies = total_vacancies - UR_vacancies
    for ele in remaining_list:
        if remaining_vacancies > 0:
            if ele.rc == "BC" and BC_vacancies > 0:
                lst.append(ele)
                BC_vacancies -= 1
                remaining_vacancies -= 1
            elif ele.rc == "SC" and SC_vacancies > 0:
                lst.append(ele)
                SC_vacancies -= 1
                remaining_vacancies -= 1
            elif ele.rc == "ST" and ST_vacancies > 0:
                lst.append(ele)
                ST_vacancies -= 1
                remaining_vacancies -= 1

    remaining_list = [ele for ele in students_list if ele not in lst]
    
    for ele in remaining_list:
        if remaining_vacancies <= 0:
            break
        lst.append(ele)
        remaining_vacancies -= 1
    return sorted(lst,key=cmp_to_key(compare_decending_merit_order))

# def fill_vacancies(students_list, total_vacancies, UR_vacancies, BC_vacancies, SC_vacancies, ST_vacancies):
#     lst = []
#     # Step 1: Fill unreserved vacancies (all candidates are eligible)
#     for i in range(UR_vacancies):
#         lst.append(students_list[i])
    
#     # Step 2: Allocate reserved category seats from the remaining candidates
#     remaining_list = [ele for ele in students_list if ele not in lst]
#     remaining_vacancies = total_vacancies - UR_vacancies
#     for ele in remaining_list:
#         if remaining_vacancies > 0:
#             if ele.rc == "BC" and BC_vacancies > 0:
#                 lst.append(ele)
#                 BC_vacancies -= 1
#                 remaining_vacancies -= 1
#             elif ele.rc == "SC" and SC_vacancies > 0:
#                 lst.append(ele)
#                 SC_vacancies -= 1
#                 remaining_vacancies -= 1
#             elif ele.rc == "ST" and ST_vacancies > 0:
#                 lst.append(ele)
#                 ST_vacancies -= 1
#                 remaining_vacancies -= 1

#     # Step 3: Fallback—fill any remaining vacancies from the overall list
#     remaining_list = [ele for ele in students_list if ele not in lst]
#     for ele in remaining_list:
#         if remaining_vacancies <= 0:
#             break
#         lst.append(ele)
#         remaining_vacancies -= 1

#     # ---- Additional replacement step ----
#     # This extra step checks if a reserved candidate (for, say, BC)
#     # from the remaining part of the list should replace the lowest-ranked
#     # open candidate in 'lst' to better honor reservation.
#     #
#     # (You can add similar logic for SC and ST as needed.)
#     bc_remaining = [s for s in students_list if s.rc == "BC" and s not in lst]
#     if bc_remaining:
#         # Since students_list is sorted overall, the first element is best
#         best_bc = bc_remaining[0]
#         # Among currently selected, consider only open-category candidates
#         open_candidates = [s for s in lst if s.rc == "Open"]
#         if open_candidates:
#             # Find the open candidate with the worst overall ranking
#             worst_open = max(open_candidates, key=lambda s: students_list.index(s))
#             # If the reserved candidate comes earlier (i.e. has better merit)
#             if students_list.index(best_bc) < students_list.index(worst_open):
#                 lst.remove(worst_open)
#                 lst.append(best_bc)
#     # -------------------------------------

#     return sorted(lst, key=cmp_to_key(compare_decending_merit_order))

def main():
    qualified_Students = int(input())
    total_vacancies = int(input())
    unreserved_vacancies = int(input())
    BC_vacancies = int(input())
    SC_vacancies = int(input())
    ST_vacancies = int(input())
    students = []
    for i in range(qualified_Students):
        inp = input()
        student_details = inp.split(",")
        students.append(Student(*student_details))
    
    students_in_merit_order = sorted(students,key =cmp_to_key(compare_decending_merit_order))

    for ele in students_in_merit_order:
        print(ele)
    
    print()
    
    filled = fill_vacancies(students_in_merit_order,total_vacancies,unreserved_vacancies,BC_vacancies,SC_vacancies,ST_vacancies)
    for ele in filled:
        print(f"{ele}")
    
    
main()