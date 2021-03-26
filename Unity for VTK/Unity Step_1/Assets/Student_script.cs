using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.Linq;

public class Student_script : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        Debug.Log(Students.total_student_count);
    }

    // Update is called once per frame
    void Update()
    {

    }

    void OnMouseDown()
    {
        for (int i = 0; i != BeaconBtn.students_list.Count; ++i)
        {
            if (BeaconBtn.students_list[i].student_box == gameObject)
            {
                BeaconBtn.students_list[i].student_box.transform.Translate(0, 3, 0);
                StudentsClass.flag_list[i] = 1;
                break;
            }
        }

        //--Students.total_student_count;
        //StudentsClass.vector_list.RemoveAt(Students.total_student_count);

        //foreach (var it in BeaconBtn.students_list.Select((Value, Index) => new { Value, Index }))
        //{
        //    it.Value.student_box.transform.position = StudentsClass.vector_list[it.Index];
        //}
    }

    void OnMouseUp()
    {
        
    }
}
