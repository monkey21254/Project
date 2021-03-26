using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;


public class Students
{
    static public string gText = "None";
    static public int total_student_count = 0; // 전체 나무 개수 카운트
}


// Students Class
public class StudentsClass
{
    private GameObject studentObject;
    public GameObject student_box;
    
    public static int students_name = 0; // 이름 용도

    private float for_count; // 위치 계산
    private Vector3 vector_init = new Vector3(0, 0, 0);
    public static List<Vector3> vector_list = new List<Vector3>(); // 벡터 정보
    public static List<int> flag_list = new List<int>(); // Flag 정보

    // 메소드
    private void getIndex() { ++StudentsClass.students_name; }
    private void setPosition()
    {
        for_count = (Students.total_student_count - 1) * 2;
        
        vector_init.x = for_count - 30;
        vector_init.y = 3;
        vector_init.z = -20;

        this.student_box.transform.position = vector_init;
        vector_list.Add(vector_init);
        flag_list.Add(0);
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
    public static List<StudentsClass> students_list = new List<StudentsClass>();
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

        Debug.Log(StudentsClass.students_name);
    }

    private void OnMouseUp()
    {
        
    }
}
