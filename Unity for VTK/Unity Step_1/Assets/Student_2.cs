using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Student_2 : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        // transform.Translate(30, 0, 16); // version 1
    }

    public float mX = 0, mY = 0, mZ = 0; // version 2
    // Update is called once per frame
    void Update()
    {
        if(mX < 30.0f){ // version 2
            mX += Time.deltaTime * 10.0f;
            transform.position = new Vector3(mX - 20, 1, -10);
        } else if (mX >= 30.0f & mZ < 16.0f) {
            mZ += Time.deltaTime * 5.0f;
            transform.position = new Vector3(mX - 20, 1, mZ - 10);
        }
    }
}
