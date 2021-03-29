using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public class DeskScript : MonoBehaviour
{
    public bool student_exist = false;
    public DeskScript2 another_desk;
    public List<Vector3> vec3_desk1_list = new List<Vector3>();

    public static bool flag1 = false;

    public static bool move_student_flag = false;
    private int this_obj_index; // 이번 단계 object index

    private bool flag_to_go, flag_to_back; // 출첵 및 퇴첵 플래그


    // Start is called before the first frame update
    void Start()
    {
        another_desk = FindObjectOfType<DeskScript2>();
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    void OnMouseDown()
    {
        if (Student_script.select_flag == true)
        {
            DeskScript.flag1 = true;
            
            DeskClass.from_start_to_middle();
            vector3_save(transform.position.z);

            DeskClass.vec3_desk_sumlist.AddRange(vec3_desk1_list);

            //foreach(Vector3 element in DeskClass.vec3_desk_sumlist)
            //{
            //   Debug.Log(element);
            //}

            //BeaconBtn.students_list[Students.student_index]
        }






            /*else if (DeskScript.move_student_flag == true)
            {
                gameObject.transform.position = StudentsClass.vector3s[0] + new Vector3(0, 0, 2);
                // 이동 시작 : Move(index 번호, 중간지점) & new Vector3(-30, 3, -10) Middle Point.  >>>>>>>>>>> 끝지점까지 연결시켜서 로직을 만들어야 함(이 함수 내에서).
                Get_data_for_move_and_set(StudentsClass.vector_list[Students.student_index], new Vector3(-30, 3, -10));

                --Students.total_student_count;
                StudentsClass.vector_list.RemoveAt(Students.total_student_count);
                // Student 리스트에서 제거 및 새로운 리스트에 삽입
                BeaconBtn.students_list.RemoveAt(this_obj_index);
                // 

                BeaconBtn.student_move_list.Add(gameObject);
                
                flag_to_go = true;
                Student_script.warning_flag = true;

                foreach (var it in BeaconBtn.students_list.Select((Value, Index) => new { Value, Index }))
                {
                    it.Value.student_box.transform.position = StudentsClass.vector_list[it.Index];
                }
            }*/

    }


    void vector3_save(float flag)
    {
        if (vec3_desk1_list.Count >= 1) { vec3_desk1_list.Clear(); }
        student_exist = true;
        if (flag < 0)
        {
            vec3_desk1_list.Add(new Vector3(transform.position.x + 4, DeskClass.middle_point1.y, DeskClass.middle_point1.z));
            vec3_desk1_list.Add(new Vector3(transform.position.x + 4, DeskClass.middle_point1.y, transform.position.z));
        }
        else if (flag > 0)
        {
            vec3_desk1_list.Add(DeskClass.middle_point1);
            vec3_desk1_list.Add(DeskClass.middle_point2);
            vec3_desk1_list.Add(new Vector3(transform.position.x + 4, DeskClass.middle_point2.y, DeskClass.middle_point2.z));
            vec3_desk1_list.Add(new Vector3(transform.position.x + 4, DeskClass.middle_point2.y, transform.position.z));
        }
    }
}