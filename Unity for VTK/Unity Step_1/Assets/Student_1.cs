using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public class Cb1
{
    static public string gText = "None";
    static public Vector3 cb_vec1 = new Vector3();
    static public bool cb1_bool;
}


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
    public Vector3 temp1;
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
        // Debug.Log("pos x:" + transform.position.x) // x 좌표 표시

        // 좌표 저장 및 비교
        if (temp1 == transform.position) {
            Cb1.cb1_bool = false;
        } else {
            Cb1.cb1_bool = true;
        }

        temp1 = transform.position;

        // 좌표 값 할당
        Cb1.gText = transform.position.ToString();
        Cb1.cb_vec1 = transform.position;
    }

    void OnMouseDown() {

        Debug.Log("OnMouseDown");
    }

    void OnMouseUp() {
        Debug.Log("OnMouseUp");
    }
}
