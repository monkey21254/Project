using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DeskScript : MonoBehaviour
{
    public static bool student_exist = false;

    private int this_obj_index; // 이번 단계 object index
    public static bool move_student_flag = false;

    // 출발, 중간, 끝지점의 꼭지점좌표를 가지는 리스트
    public List<Vector3> vector3s = new List<Vector3>();
    private Vector3 middle_point1 = new Vector3(-30, 0, -10);


    private bool flag_to_go, flag_to_back; // 출첵 및 퇴첵 플래그
    private int cnt = 1; // 중간지점 인덱스용

    private Vector3 dest_point;


    // Start is called before the first frame update
    void Start()
    {
        //Debug.Log(gameObject.transform.position);
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    void OnMouseDown()
    {
        //this_obj_index = Desks_Base.desk_list.FindIndex(x => x.desk_box == gameObject);

        if (Student_script.select_flag == true)
        {
            Get_data_for_move_and_set(vector3s);
            foreach(Vector3 element in vector3s)
            {
                Debug.Log(element);
            }
        }

        /*
        if ((BeaconBtn.student_move_list[0] != null) && (Student_script.select_flag == true))
        {
            Debug.Log(BeaconBtn.student_move_list[0].student_box.transform.position);
            Debug.Log(gameObject.transform.position);
            //Get_data_for_move_and_set();
        }
        */

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


    // save_root: Vector3 List, angle_list: string List
    void Get_data_for_move_and_set(List<Vector3> _vector3s) // 몇 번째 리스트 인덱스를 사용할 것인지 // int index, 
    {
        _vector3s.Add(BeaconBtn.students_list[Student_script.selected_index].student_box.transform.position);
        _vector3s.Insert(cnt, _vector3s[0] + new Vector3(0, 0, 2));
        ++cnt;
        _vector3s.Insert(cnt, new Vector3(middle_point1.x, _vector3s[cnt - 1].y, _vector3s[cnt - 1].z));
        ++cnt;
        _vector3s.Insert(cnt, middle_point1);
        ++cnt;
        _vector3s.Insert(_vector3s.Count, gameObject.transform.position);
    }

}