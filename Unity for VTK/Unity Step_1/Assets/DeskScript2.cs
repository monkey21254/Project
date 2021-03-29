using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public class DeskScript2 : MonoBehaviour
{
    public bool student_exist = false;
    public DeskScript another_desk;
    public List<Vector3> vec3_desk2_list = new List<Vector3>();
    public List<Vector3> vec3_desk2_list2 = new List<Vector3>();

    public static bool flag2 = false;

    // Start is called before the first frame update
    void Start()
    {
        another_desk = FindObjectOfType<DeskScript>();
    }


    // Update is called once per frame
    void Update()
    {

    }


    void OnMouseDown()
    {
        if (Student_script.select_flag == true) // 이후에 another_desk.student_exist: bool값을 기준으로 다른 리스트를 붙여서 사용해야 함.
        {
            DeskScript2.flag2 = true;
            DeskClass.from_start_to_middle();
            vector3_save(transform.position.z);

            // 학생 플래그 설정한 조건에 따라 분기로 나누어 처리해야함.
            DeskClass.vec3_desk_sumlist.AddRange(vec3_desk2_list);

            //foreach(Vector3 element in DeskClass.vec3_desk_sumlist)
            //{
            //   Debug.Log(element);
            //}
        }
    }


    void vector3_save(float flag)
    {
        if (vec3_desk2_list.Count >= 1) { vec3_desk2_list.Clear(); }
        if (vec3_desk2_list2.Count >= 1) { vec3_desk2_list2.Clear(); }
        student_exist = true;
        if (flag < 0)
        {
            vec3_desk2_list.Add(new Vector3(transform.position.x + 4, transform.position.y, DeskClass.middle_point1.z));
            vec3_desk2_list.Add(new Vector3(transform.position.x + 4, transform.position.y, transform.position.z));

            vec3_desk2_list2.Add(DeskClass.middle_point1);
            vec3_desk2_list2.Add(DeskClass.middle_point2);
            vec3_desk2_list2.Add(new Vector3(transform.position.x + 4, transform.position.y, DeskClass.middle_point2.z));
            vec3_desk2_list2.Add(new Vector3(transform.position.x + 4, transform.position.y, transform.position.z));
        }
        else if (flag > 0)
        {
            vec3_desk2_list.Add(DeskClass.middle_point1);
            vec3_desk2_list.Add(DeskClass.middle_point2);
            vec3_desk2_list.Add(new Vector3(transform.position.x + 4, transform.position.y, DeskClass.middle_point2.z));
            vec3_desk2_list.Add(new Vector3(transform.position.x + 4, transform.position.y, transform.position.z));

            vec3_desk2_list2.Add(DeskClass.middle_point1);
            vec3_desk2_list2.Add(DeskClass.middle_point3);
            vec3_desk2_list2.Add(new Vector3(transform.position.x + 4, transform.position.y, DeskClass.middle_point3.z));
            vec3_desk2_list2.Add(new Vector3(transform.position.x + 4, transform.position.y, transform.position.z));
        }
    }
}
