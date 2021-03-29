using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.Linq;


public class Student_script : MonoBehaviour
{
    private int this_obj_index; // �̹� �ܰ� object index
    public static int selected_index; // ���� ������ object index (�ٸ� Ŭ�������� Ȱ��Ǿ�� ��)

    private bool flag_to_go, flag_to_back; // ��ý �� ��ý �÷���
    public static bool select_flag = false; 
    //public static bool warning_flag = false; 
    
    
    
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
        if (flag_to_go == true)
        {
            /* �ʿ� */
            // Student_script.warning_flag = true;
            // ������Ʈ �� StudentClass
            




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
        
    }

    void OnMouseDown()
    {      
        this_obj_index = BeaconBtn.students_list.FindIndex(x => x.student_box == gameObject);
        if (Students.student_index != this_obj_index) // �� �л��� �����Ǿ��ٰ� ��� ������ ����� ���Ŀ� �� �Ȱ��� �ε������� Ŭ���ϴ� ��� ���� ���� �� �����Ƿ� �׿� ���� ó���� �ʿ�
        {
            
            BeaconBtn.students_list[this_obj_index].student_box.transform.Translate(0, 3, 0);
            if (Students.student_index != -1)
            {
                BeaconBtn.students_list[Students.student_index].student_box.transform.Translate(0, -3, 0);
            }
            Students.student_index = this_obj_index;

            Student_script.selected_index = this_obj_index; // ����� this_obj_index�� static���� �ξ ���� �ȵ����� ���߿� �ٽ� ����ؾ� ��.

            Student_script.select_flag = true;
        }
    }

    
    void OnMouseUp()
    {

    }
}