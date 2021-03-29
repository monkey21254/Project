using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;


public class Students
{
    public static int total_student_count = 0; // 전체 학생 수 카운트
    public static int student_index = -1; // 학생 index 변수 & 초기값 -1
}


// Students Class
public class StudentsClass
{
    private GameObject studentObject;
    public GameObject student_box;
    
    public static int students_name = 0; // 이름 용도

    // 초기 생성자
    private float for_count = (Students.total_student_count - 1) * 2; // 위치 계산용
    public Vector3 vector_init = new Vector3(0, 0, 0); // 학생 초기 위치
    public static List<Vector3> vector_list = new List<Vector3>(); // 시작점이 저장된 벡터3 리스트


    // 메소드
    public void getIndex() { ++StudentsClass.students_name; }
    private void setPosition()
    {        
        vector_init.x = for_count - 25;
        vector_init.y = 1.5f;
        vector_init.z = -20;

        this.student_box.transform.position = vector_init;
    }

    // 생성자
    public StudentsClass(GameObject studentObject)
    {
        this.studentObject = studentObject;
        this.student_box = MonoBehaviour.Instantiate(this.studentObject);

        this.getIndex();
        this.setPosition();
    }
}


public class BeaconBtn : MonoBehaviour
{
    public StudentsClass custom_students;
    public static List<StudentsClass> students_list = new List<StudentsClass>(); // 출석용
    public static List<StudentsClass> student_move_list = new List<StudentsClass>(); // 퇴근용

    // Start is called before the first frame update
    void Start()
    {

    }

    // Update is called once per frame
    void Update()
    {
        
    }

    private void OnMouseDown()
    {
        ++Students.total_student_count;

        try
        {
            if ((Students.total_student_count <= 40) == false)
            {
                throw new Exception("Out of Range error....");
            }
            else
            {
                custom_students = new StudentsClass((GameObject)Resources.Load("Prefabs/Body"));
                custom_students.student_box.transform.parent = gameObject.transform;

                students_list.Add(custom_students);
            }
        }
        catch (Exception e)
        {
            Debug.LogError(e);
        }

        //Debug.Log(StudentsClass.students_name);
    }

    private void OnMouseUp()
    {
        
    }
}
