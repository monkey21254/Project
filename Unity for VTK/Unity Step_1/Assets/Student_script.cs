using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.Linq;


public class Student_script : MonoBehaviour
{
    private int this_obj_index; // 이번 단계 object index

    private bool flag_to_go = false; // 출첵 플래그
    private bool flag_to_back = false; // 퇴첵 플래그
    private bool flag_to_bus = false; // 마지막 역방향 이동
    public static bool select_flag = false; // 학생 선택 시 활성화되는 플래그
    public List<Vector3> this_student_list; // 이 학생의 경로가 저장된 리스트
    public bool only_1play_flag = false; // 리스트 값을 한 번만 출력하기 위해 사용한 플래그
    private int index = 0;
    public float Speed = 1f;

    // 책상의 flag: bool + list<vec3> 에 접근하도록 변수 설정해야 함


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
        /* 필요 */
        // Student_script.warning_flag = true;
        // 업데이트 시 StudentClass
        

        if ((DeskScript.flag1 == true || DeskScript2.flag2 == true) && BeaconBtn.students_list[Students.student_index].student_box == gameObject)
        {
            if (only_1play_flag == false)
            {
                foreach(Vector3 element in DeskClass.vec3_desk_sumlist)
                {
                    this_student_list.Add(new Vector3(element.x, element.y, element.z));
                }
                DeskClass.vec3_desk_sumlist.Clear();
                only_1play_flag = true;
                
                foreach(Vector3 element in this_student_list)
                {
                    Debug.Log(element);
                }
            }
            
            if (transform.position == this_student_list[index + 1])
            {
                ++index;
                if (index > this_student_list.Count - 2)
                {
                    index = this_student_list.Count - 1;
                    if (DeskScript.flag1 == true)
                    {
                        DeskScript.flag1 = false;
                    }
                    if (DeskScript2.flag2 == true)
                    {
                        DeskScript2.flag2 = false;
                    }
                    flag_to_back = true;
                    //Students.student_index = -1;
                }
            }
            else if (index < this_student_list.Count - 1)
            {
                transform.position = Vector3.MoveTowards(transform.position, this_student_list[index + 1], Speed * Time.deltaTime * 10);
            }
        }
        else if (flag_to_bus == true && BeaconBtn.students_list[Students.student_index].student_box == gameObject)
        {
            if (transform.position == this_student_list[index])
            {
                --index;
                if (index < 0)
                {
                    index = 0;
                    flag_to_bus = false;
                    //Students.student_index = -1;
                }
            }
            else if (index >= 0)
            {
                transform.position = Vector3.MoveTowards(transform.position, this_student_list[index], Speed * Time.deltaTime * 10);
            }
        }


            /*
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

    void OnMouseDown()
    {      
        this_obj_index = BeaconBtn.students_list.FindIndex(x => x.student_box == gameObject);
        if (flag_to_go == false && flag_to_back == false)
        {
            if (Students.student_index != this_obj_index) // 한 학생이 지정되었다가 모든 행위가 진행된 이후에 또 똑같은 인덱스에서 클릭하는 경우 오류 생길 수 있으므로 그에 대한 처리가 필요
            {
            
                BeaconBtn.students_list[this_obj_index].student_box.transform.Translate(0, 3, 0);
                if (Students.student_index != -1)
                {
                    BeaconBtn.students_list[Students.student_index].student_box.transform.Translate(0, -3, 0); // ... 내려가는거 고쳐야함.
                }
                Students.student_index = this_obj_index; // 나중에 처리가 끝난 후 -1로 바꿔서 다른 객체로 이동할 수 있도록 해야 함
                Student_script.select_flag = true;
            }
        }
        else if (flag_to_go == false && flag_to_back == true)
        {
            flag_to_bus = true;
        }
    }

    
    void OnMouseUp()
    {

    }
}