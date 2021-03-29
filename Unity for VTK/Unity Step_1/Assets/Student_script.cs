using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.Linq;


public class Student_script : MonoBehaviour
{
    private int this_obj_index; // �̹� �ܰ� object index

    private bool flag_to_go = false; // ��ý �÷���
    private bool flag_to_back = false; // ��ý �÷���
    private bool flag_to_bus = false; // ������ ������ �̵�
    public static bool select_flag = false; // �л� ���� �� Ȱ��ȭ�Ǵ� �÷���
    public List<Vector3> this_student_list; // �� �л��� ��ΰ� ����� ����Ʈ
    public bool only_1play_flag = false; // ����Ʈ ���� �� ���� ����ϱ� ���� ����� �÷���
    private int index = 0;
    public float Speed = 1f;

    // å���� flag: bool + list<vec3> �� �����ϵ��� ���� �����ؾ� ��


    //public static List<List<Vector3> > vectors = new List<List<Vector3> >();
   

    private int[,] plane_info; // ��� ����
    private float mX, mY, mZ; // �Ÿ� ���� ����
    private Vector3 temp; // �̵� ������
    private List<string> angle_list = new List<string>(); // ȸ������ �����
    

    // Start is called before the first frame update
    void Start()
    {

    }

    // Update is called once per frame
    void Update()
    {
        /* �ʿ� */
        // Student_script.warning_flag = true;
        // ������Ʈ �� StudentClass
        

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
                Student_script.warning_flag = false; // ���� �߿��� �ٸ� ��ü�� Ŭ���� �� ������ ����
                Students.student_index = -1; // �ʱ�ȭ

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
                totalStuVecList.Add(angle_list); // �ε��� ȣ���� ��� �����ؾ� ��

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
            if (Students.student_index != this_obj_index) // �� �л��� �����Ǿ��ٰ� ��� ������ ����� ���Ŀ� �� �Ȱ��� �ε������� Ŭ���ϴ� ��� ���� ���� �� �����Ƿ� �׿� ���� ó���� �ʿ�
            {
            
                BeaconBtn.students_list[this_obj_index].student_box.transform.Translate(0, 3, 0);
                if (Students.student_index != -1)
                {
                    BeaconBtn.students_list[Students.student_index].student_box.transform.Translate(0, -3, 0); // ... �������°� ���ľ���.
                }
                Students.student_index = this_obj_index; // ���߿� ó���� ���� �� -1�� �ٲ㼭 �ٸ� ��ü�� �̵��� �� �ֵ��� �ؾ� ��
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