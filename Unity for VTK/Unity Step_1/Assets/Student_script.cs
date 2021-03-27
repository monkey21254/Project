using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.Linq;


public class Student_script : MonoBehaviour
{
    private int this_obj_index;
    private bool flag_to_go, flag_to_back;

    private float total_dis; // 출발지와 도착지 간의 거리 총합
    private Vector3 total_dis_vector = new Vector3(); // 출발지와 도착지 간의 상대 벡터
    private float x, y, z;
    private Vector3 start_points = new Vector3(); // 시작 Vector
    private int[,] first_plane; // 이동 시 사용될 첫번째 평면
    private int[,] second_plane; // 이동 시 사용될 두번째 평면
    private float mX, mY, mZ;
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
                transform.rotation = Quaternion.Euler(0, 180, 0);
            }
            else if (mX >= x & mZ < z)
            {
                mZ += Time.deltaTime * 5.0f;
                transform.position = new Vector3(start_points.x - mX, start_points.y, start_points.z + mZ);
                transform.rotation = Quaternion.Euler(0, -90, 0);
            }
            else
            {
                transform.rotation = Quaternion.Euler(0, 0, 0);
                flag_to_go = false;
                Debug.Log("Stop");
            }

            // 좌표 저장 및 비교
            if (temp == transform.position)
            {
                
            }
            else
            {
                
            }
            temp = transform.position;

        }
        
    }

    void OnMouseDown()
    {      
        this_obj_index = BeaconBtn.students_list.FindIndex(x => x.student_box == gameObject);
        if (Students.student_index != this_obj_index) 
        {
            BeaconBtn.students_list[this_obj_index].student_box.transform.Translate(0, 3, 0);
            if (Students.student_index != -1)
            {
                StudentsClass.flag_list[Students.student_index] = 0;
            }
            StudentsClass.flag_list[this_obj_index] = 1;
            Students.student_index = this_obj_index;
        }
        else
        {
            // 이동 시작 : Move(출발지점, 도착지점) & new Vector3(-30, 3, -10) Middle Point.
            Get_data_for_move_and_set(StudentsClass.vector_list[Students.student_index], new Vector3(-30, 3, -10));
            flag_to_go = true;

            --Students.total_student_count;
            StudentsClass.vector_list.RemoveAt(Students.total_student_count);
            BeaconBtn.students_list.RemoveAt(this_obj_index);

            foreach (var it in BeaconBtn.students_list.Select((Value, Index) => new { Value, Index }))
            {
                it.Value.student_box.transform.position = StudentsClass.vector_list[it.Index];
            }
        }

    }

    
    void OnMouseUp()
    {

    }


    void Get_data_for_move_and_set(Vector3 start_point, Vector3 middle_point) //, Vector3 end_points) // int flag
    {
        // 초기 설정
        start_points = gameObject.transform.position = start_point + new Vector3(0, 0, 2);
        //Debug.Log(start_points);

        // 거리 계산
        total_dis_vector.x = gameObject.transform.position.x - middle_point.x;
        total_dis_vector.y = gameObject.transform.position.y - middle_point.y;
        total_dis_vector.z = gameObject.transform.position.z - middle_point.z;
        total_dis = Mathf.Abs(total_dis_vector.x) + Mathf.Abs(total_dis_vector.y) + Mathf.Abs(total_dis_vector.z);
        //Debug.Log(total_dis_vector);
        //Debug.Log(Mathf.Abs(total_dis_vector.x) + Mathf.Abs(total_dis_vector.y) + Mathf.Abs(total_dis_vector.z));

        // 평면 초기화
        x = Mathf.Abs(total_dis_vector.x);
        y = Mathf.Abs(total_dis_vector.y);
        z = Mathf.Abs(total_dis_vector.z);
        first_plane = new int[Mathf.RoundToInt(x), Mathf.RoundToInt(z)];
        //Debug.Log(first_plane[Mathf.RoundToInt(x) - 1, Mathf.RoundToInt(z) - 1]);
        
        
    }

}