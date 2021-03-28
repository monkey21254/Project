using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.Linq;


public class Student_script : MonoBehaviour
{
    private int this_obj_index; // 이번 단계 object index
    private bool flag_to_go, flag_to_back; // 출첵 및 퇴첵 플래그
    public static bool warning_flag = false;

    private float total_dis; // 출발지와 도착지 간의 거리 총합
    private Vector3 total_dis_vector = new Vector3(); // 출발지와 도착지 간의 상대 벡터
    private float x, y, z; // x, y, z 축에 대한 거리(절대값)
    private Vector3 start_points = new Vector3(); // 시작 Vector
    private int[,] plane_info; // 평면 정보
    private float mX, mY, mZ; // 거리 계산용 변수
    public Vector3 temp;

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        if (flag_to_go == true)
        {
            if(mX < x)
            {
                mX += Time.deltaTime * 5.0f;
                transform.position = new Vector3(start_points.x - mX, start_points.y, start_points.z);
                transform.rotation = Quaternion.Euler(0, 180, 0); // 0, 180, 0 : Vector3
                //Debug.Log(transform.rotation.eulerAngles);
            }
            else if (mX >= x & mZ < z)
            {
                mZ += Time.deltaTime * 5.0f;
                transform.position = new Vector3(start_points.x - mX, start_points.y, start_points.z + mZ);
                transform.rotation = Quaternion.Euler(0, -90, 0); // 0, 270, 0 : Vector3
                //Debug.Log(transform.rotation.eulerAngles);
            }
            else
            {
                transform.rotation = Quaternion.Euler(0, 0, 0); // 0, 0, 0 : Vector3
                flag_to_go = false;
                Student_script.warning_flag = false;
                Students.student_index = -1; // 초기화
                //Debug.Log(transform.rotation.eulerAngles);

            }

        }
        
    }

    void OnMouseDown()
    {      
        if (Student_script.warning_flag == false)
        {
            this_obj_index = BeaconBtn.students_list.FindIndex(x => x.student_box == gameObject);
            if (Students.student_index != this_obj_index) 
            {
                BeaconBtn.students_list[this_obj_index].student_box.transform.Translate(0, 3, 0);
                if (Students.student_index != -1)
                {
                    BeaconBtn.students_list[Students.student_index].student_box.transform.Translate(0, -3, 0);
                }
                Students.student_index = this_obj_index;
            }
            else
            {
                // 이동 시작 : Move(출발지점, 도착지점) & new Vector3(-30, 3, -10) Middle Point.
                Get_data_for_move_and_set(StudentsClass.vector_list[Students.student_index], new Vector3(-30, 3, -10));

                --Students.total_student_count;
                StudentsClass.vector_list.RemoveAt(Students.total_student_count);
                BeaconBtn.students_list.RemoveAt(this_obj_index);
                flag_to_go = true;
                Student_script.warning_flag = true;

                foreach (var it in BeaconBtn.students_list.Select((Value, Index) => new { Value, Index }))
                {
                    it.Value.student_box.transform.position = StudentsClass.vector_list[it.Index];
                }
            }
        }
    }

    
    void OnMouseUp()
    {

    }


    void Get_data_for_move_and_set(Vector3 start_point, Vector3 end_point)
    {
        // 초기 설정
        start_points = gameObject.transform.position = start_point + new Vector3(0, 0, 2);
        //Debug.Log(start_points);

        // 거리 계산
        total_dis_vector.x = gameObject.transform.position.x - end_point.x;
        total_dis_vector.y = gameObject.transform.position.y - end_point.y;
        total_dis_vector.z = gameObject.transform.position.z - end_point.z;
        //Debug.Log(total_dis_vector);
        //Debug.Log(Mathf.Abs(total_dis_vector.x) + Mathf.Abs(total_dis_vector.y) + Mathf.Abs(total_dis_vector.z));

        // 평면 초기화
        x = Mathf.Abs(total_dis_vector.x);
        y = Mathf.Abs(total_dis_vector.y);
        z = Mathf.Abs(total_dis_vector.z);
        total_dis = x + y + z;
        //Debug.Log(first_plane[Mathf.RoundToInt(x) - 1, Mathf.RoundToInt(z) - 1]);
        
    }

}