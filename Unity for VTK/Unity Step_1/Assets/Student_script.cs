using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.Linq;


public class Student_script : MonoBehaviour
{
    private int this_obj_index; // 이번 단계 object index
    public static int selected_index; // 최종 결정된 object index (다른 클래스에서 활용되어야 함)

    private bool flag_to_go, flag_to_back; // 출첵 및 퇴첵 플래그
    public static bool select_flag = false; 
    //public static bool warning_flag = false; 
    
    
    
    //public static List<List<Vector3> > vectors = new List<List<Vector3> >();


    private int[,] plane_info; // 평면 정보
    private float mX, mY, mZ; // 거리 계산용 변수
    private Vector3 temp; // 이동 검증용
    
    private List<string> angle_list = new List<string>(); // 회전형태 저장용
    

    // Start is called before the first frame update
    void Start()
    {

    }

    // Update is called once per frame
    void Update()
    {
        if (flag_to_go == true)
        {
            /* 필요 */
            // Student_script.warning_flag = true;
            // 업데이트 시 StudentClass
            




            /*
            if(mX < x)
            {
                mX += Time.deltaTime * 5.0f;

                transform.position = new Vector3(start_points.x - mX, start_points.y, start_points.z);
                transform.rotation = Quaternion.Euler(0, 180, 0); // 0, 180, 0 : Vector3

                temp = transform.rotation.eulerAngles;
                //Debug.Log(transform.rotation.eulerAngles);
            }
            else if (mX >= x & mZ < z)
            {
                mZ += Time.deltaTime * 5.0f;
                transform.position = new Vector3(start_points.x - mX, start_points.y, start_points.z + mZ);
                transform.rotation = Quaternion.Euler(0, -90, 0); // 0, 270, 0 : Vector3

                if (temp != transform.rotation.eulerAngles)
                {
                    //Debug.Log(transform.rotation.eulerAngles);
                    //Debug.Log(transform.rotation.eulerAngles.y - temp.y);
                    if (transform.rotation.eulerAngles.y - temp.y == 90 || transform.rotation.eulerAngles.y - temp.y == -270)
                    {
                        angle_list.Add("right");
                    }
                    else if (transform.rotation.eulerAngles.y - temp.y == 180 || transform.rotation.eulerAngles.y - temp.y == -180)
                    {
                        angle_list.Add("backward");
                    }
                    else if (transform.rotation.eulerAngles.y - temp.y == -90 || transform.rotation.eulerAngles.y - temp.y == 270)
                    {
                        angle_list.Add("left");
                    }
                }
                temp = transform.rotation.eulerAngles;
                //Debug.Log(transform.rotation.eulerAngles);
            }
            else
            {
                transform.rotation = Quaternion.Euler(0, 0, 0); // 0, 0, 0 : Vector3
                flag_to_go = false;
                Student_script.warning_flag = false; // 진행 중에는 다른 개체를 클릭할 수 없도록 지정
                Students.student_index = -1; // 초기화

                if (temp != transform.rotation.eulerAngles)
                {
                    //Debug.Log(transform.rotation.eulerAngles);
                    //Debug.Log(transform.rotation.eulerAngles.y - temp.y);
                    if (transform.rotation.eulerAngles.y - temp.y == 90 || transform.rotation.eulerAngles.y - temp.y == -270)
                    {
                        angle_list.Add("right");
                    }
                    else if (transform.rotation.eulerAngles.y - temp.y == 180 || transform.rotation.eulerAngles.y - temp.y == -180)
                    {
                        angle_list.Add("backward");
                    }
                    else if (transform.rotation.eulerAngles.y - temp.y == -90 || transform.rotation.eulerAngles.y - temp.y == 270)
                    {
                        angle_list.Add("left");
                    }
                }
                totalStuVecList.Add(angle_list); // 인덱스 호출할 방법 생각해야 함

                temp = transform.rotation.eulerAngles;
                //Debug.Log(transform.rotation.eulerAngles);
            }
            */
        }
        
    }

    void OnMouseDown()
    {      
        this_obj_index = BeaconBtn.students_list.FindIndex(x => x.student_box == gameObject);
        if (Students.student_index != this_obj_index) // 한 학생이 지정되었다가 모든 행위가 진행된 이후에 또 똑같은 인덱스에서 클릭하는 경우 오류 생길 수 있으므로 그에 대한 처리가 필요
        {
            
            BeaconBtn.students_list[this_obj_index].student_box.transform.Translate(0, 3, 0);
            if (Students.student_index != -1)
            {
                BeaconBtn.students_list[Students.student_index].student_box.transform.Translate(0, -3, 0);
            }
            Students.student_index = this_obj_index;

            Student_script.selected_index = this_obj_index; // 지우고 this_obj_index를 static으로 두어도 될지 안될지를 나중에 다시 고민해야 함.

            Student_script.select_flag = true;
        }
    }

    
    void OnMouseUp()
    {

    }
}