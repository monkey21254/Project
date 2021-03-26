using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Student_text : MonoBehaviour
{
    public TextMesh mTm_students;
    // Start is called before the first frame update
    void Start()
    {
        mTm_students = GetComponent<TextMesh>();
        mTm_students.text = StudentsClass.students_name.ToString();
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
