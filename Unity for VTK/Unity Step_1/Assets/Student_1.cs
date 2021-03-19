using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public class Student_1 : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        // transform.Translate(17, 0, 4); // version 1
        // Debug.Log("Start Log");
    }

    public float mX = 0, mY = 0, mZ = 0; // Unity 자체적으로 이 곳에 들어오는 멤버 변수를 초기화 값이 아닌 0으로 지정하기 때문에 유의해야 한다!!!
    public float student_1x = 0, student_1z = 0;
    // Update is called once per frame
    void Update()
    {
        // transform.Translate(0.001f, 0, 0); // version 1
        // Debug.Log("Update Log" + Time.deltaTime);
        
        if(mX < 17.5f){ // version 2
            mX += Time.deltaTime * 10.0f;
            transform.position = new Vector3(mX - 17.5f, 1, -10);
        } else if (mX >= 17.5f & mZ < 4.0f) {
            mZ += Time.deltaTime * 5.0f;
            transform.position = new Vector3(mX - 17.5f, 1, mZ - 10);
        }

        // if(mX >= 17.5f & mZ >= 4.0f) { // version 3
        //     student_1x = mX;
        //     student_1z = mZ;
        // }

        // if(student_1z > 0.0f) {
        //     if(student_1z <= 5.5f) {
        //         mZ += Time.deltaTime * 1.5f;
        //         transform.position = new Vector3(mX - 17.5f, 1, mZ - 10);                
        //     }
        //     else if(student_1z <= 5.5f) {
        //         mZ -= Time.deltaTime * 1.5f;
        //         transform.position = new Vector3(mX - 17.5f, 1, mZ - 10);
        //     }
        // }

    }
}
